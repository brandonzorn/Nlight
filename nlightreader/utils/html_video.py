from render_html import render_in_browser

from nlightreader.models import Chapter, Manga


def start_html_video(manga: Manga, chapter: Chapter):
    src_url = chapter.__getattribute__("url")
    render_in_browser(
        f"""
        <html lang="ru">
        <head>
            <title>{manga.get_name()}</title>
        </head>
        <body style="background-color:black;">
        <iframe id="player" src="{src_url}&hide_selectors=true" width="100%"
                height="100%" frameborder="0"
                allowfullscreen allow="autoplay *; fullscreen *">
        </iframe>
        <script type="text/javascript">
            const player = document.getElementById('player');
            const manga_id = '{manga.id}';
            const chapter_id = '{chapter.id}';

            let max_time = 0;
            let cur_time = 0;

            let is_completed = false;

            function sendPostRequest() {{
                const data = {{
                    manga_id: manga_id,
                    chapter_id: chapter_id,
                    player_cur_time: cur_time,
                    player_max_time: max_time,
                    is_completed: is_completed
                }};

                fetch('http://localhost:8000', {{
                    method: 'POST',
                    headers: {{
                        'Content-Type': 'application/json'
                    }},
                    body: JSON.stringify(data)
                }});
                console.log('post', data);
            }}

            function kodikMessageListener(message) {{
                if (message.data.key === 'kodik_player_time_update') {{
                    let messageTime = message.data.value;
                    cur_time = messageTime;
                    if (max_time - messageTime < 300 && !is_completed) {{

                        is_completed = true;
                        console.log("completed=", is_completed);
                        sendPostRequest();
                    }}
                    else if (max_time - messageTime > 300 && is_completed) {{
                        is_completed = false;
                        console.log("completed=", is_completed);
                        sendPostRequest();
                    }}
                }}
                else if (
                message.data.key === 'kodik_player_duration_update'
                ) {{
                    max_time = message.data.value;
                }}
                else if (message.data.key === 'kodik_player_video_ended') {{
                    window.close();
                }}
            }}
            if (window.addEventListener) {{
                window.addEventListener('message', kodikMessageListener);
            }} else {{
                window.attachEvent('onmessage', kodikMessageListener);
            }}
        </script>
        </body>
        </html>
        """,
    )


__all__ = [
    "start_html_video",
]
