from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import logging
from string import Template
import threading
from threading import Thread
import webbrowser

from nlightreader.items import HistoryNote
from nlightreader.models import Chapter, Manga
from nlightreader.utils.database import Database

logger = logging.getLogger(__name__)


_CONTENT_TEMPLATE = Template(r"""
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>$title</title>
    <style>
        html, body {
            margin: 0;
            padding: 0;
            width: 100%;
            height: 100%;
            background: black;
            overflow: hidden;
        }
        iframe {
            width: 100%;
            height: 100%;
            border: none;
        }
    </style>
</head>
<body>
<iframe
    id="player"
    src="$src_url&hide_selectors=true"
    allowfullscreen allow="autoplay; fullscreen"
></iframe>

<script>
    const anime_id = '$anime_id';
    const episode_id = '$episode_id';

    const completion_min_time = 300;

    let max_time = 0;
    let cur_time = 0;
    let is_completed = false;
    let last_sent_time = 0;

    function sendProgressUpdate() {
        const data = {
            anime_id: anime_id,
            episode_id: episode_id,
            player_cur_time: Math.floor(cur_time),
            player_max_time: Math.floor(max_time),
            is_completed: is_completed
        };

        fetch('http://localhost:$server_port', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        }).catch(err => console.error('Reporting failed:', err));
    }

    window.addEventListener('message', function(message) {
        if (!message.data || typeof message.data !== 'object') return;

        switch (message.data.key) {
            case 'kodik_player_time_update':
                cur_time = message.data.value;
                const remaining = max_time - cur_time;
                if (remaining < completion_min_time && !is_completed) {
                    is_completed = true;
                    sendProgressUpdate();
                } else if (remaining >= completion_min_time && is_completed) {
                    is_completed = false;
                    sendProgressUpdate();
                }

                if (Math.abs(cur_time - last_sent_time) >= 5) {
                    last_sent_time = cur_time;
                    sendProgressUpdate();
                }
                break;

            case 'kodik_player_duration_update':
                max_time = message.data.value;
                break;

            case 'kodik_player_video_ended':
                is_completed = true;
                sendProgressUpdate();
                break;
        }
    });
</script>
</body>
</html>
""")


class KodikPlayerHttpRequestHandler(BaseHTTPRequestHandler):
    _SERVER_PORT = 8000

    _active_html = ""
    _track_progress = False

    def do_GET(self) -> None:
        if not self._active_html:
            self.send_error_response(404, "No active video session")
            return

        response_data = self._active_html.encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(response_data)))
        self.end_headers()
        self.wfile.write(response_data)

    def do_POST(self) -> None:
        if not self._track_progress:
            self.send_error_response(403, "Metrics is disabled")
        try:
            content_length = int(self.headers.get("Content-Length", 0))
            if content_length == 0:
                self.send_error_response(400, "Empty body")
                return

            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)

            anime_id = data.get("anime_id", "")
            episode_id = data.get("episode_id", "")
            is_completed = bool(data.get("is_completed", False))
            player_cur_time = data.get("player_cur_time", 0)

            if not anime_id or not episode_id:
                self.send_error_response(400, "Missing anime_id or episode_id")
                return

            db = Database()
            manga = db.get_manga(anime_id)
            chapter = db.get_chapter(episode_id)

            note = HistoryNote(chapter, manga, is_completed)
            db.add_history_note(note)

            logger.debug(
                "Anime %s, Episode %s: progress %s sec",
                anime_id,
                episode_id,
                player_cur_time,
            )

            response_data = json.dumps({"status": "success"}).encode("utf-8")
            self.set_cors_headers(200, len(response_data))
            self.wfile.write(response_data)

        except json.JSONDecodeError:
            self.send_error_response(400, "Invalid JSON format")
        except Exception as e:
            logger.exception("Internal error in Player Server")
            self.send_error_response(500, f"Internal Server Error: {str(e)}")

    def do_OPTIONS(self) -> None:
        self.set_cors_headers(200, 0)

    def set_cors_headers(self, status_code: int, content_length: int) -> None:
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(content_length))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS, GET")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def send_error_response(self, code: int, message: str) -> None:
        response_data = json.dumps(
            {"status": "error", "message": message},
        ).encode("utf-8")
        self.set_cors_headers(code, len(response_data))
        self.wfile.write(response_data)


def get_local_server(
    server_port: int,
    track_progress: bool,
) -> Thread:
    KodikPlayerHttpRequestHandler._track_progress = track_progress
    _server_instance = HTTPServer(
        ("localhost", server_port),
        KodikPlayerHttpRequestHandler,
    )
    return threading.Thread(target=_server_instance.serve_forever, daemon=True)


def start_html_video(anime: Manga, episode: Chapter) -> None:
    src_url = getattr(episode, "url", None)
    if not src_url:
        logger.error(
            "Attempted to play episode %s without valid stream URL",
            episode.id,
        )
        return

    KodikPlayerHttpRequestHandler._active_html = _CONTENT_TEMPLATE.substitute(
        title=anime.get_name(),
        anime_id=anime.id,
        episode_id=episode.id,
        src_url=src_url,
        server_port=KodikPlayerHttpRequestHandler._SERVER_PORT,
    )

    webbrowser.open(
        f"http://localhost:{KodikPlayerHttpRequestHandler._SERVER_PORT}/play",
    )


__all__ = [
    "get_local_server",
    "start_html_video",
]
