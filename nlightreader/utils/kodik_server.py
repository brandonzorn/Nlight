import json
from http.server import BaseHTTPRequestHandler

from nlightreader.items import HistoryNote
from nlightreader.utils.database import Database


class KodikHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)

        manga_id = data.get("manga_id", "")
        chapter_id = data.get("chapter_id", "")
        # player_cur_time = data.get("player_cur_time", "")
        # player_max_time = data.get("player_max_time", "")
        is_completed = bool(data.get("is_completed", False))

        db = Database()
        manga = db.get_manga(manga_id)
        chapter = db.get_chapter(chapter_id)
        note = HistoryNote(chapter, manga, is_completed)
        db.add_history_note(note)

        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

        self.send_response(200)
        self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()


__all__ = [
    "KodikHTTPRequestHandler",
]
