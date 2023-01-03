import re

from PySide6.QtWidgets import QApplication


def description_to_html(text: str, show_spoilers=False) -> str:
    if not text:
        return ""
    text = ' '.join(text.splitlines())
    for ch_id, name in re.findall(r"\[character=(\w+)](.+?)\[/character]", text):
        text = text.replace(f"[character={ch_id}]{name}[/character]",
                            f'<span style=" color:#177e00;">{name}</span>')
    for i, spoiler_text in re.findall(r"\[spoiler=(\w+)](.+?)\[/spoiler]", text):
        spoiler = spoiler_text
        if not show_spoilers:
            spoiler = ""
        text = text.replace(f"[spoiler={i}]{spoiler_text}[/spoiler]",
                            f'<span style=" color:#951a00;">{spoiler}</span>')
    for url, url_text in re.findall(r"\[url=(.+?)](.+?)\[/url]", text):
        text = text.replace(f"[url={url}]{url_text}[/url]",
                            f'<a href="{url}">'
                            f'<span style="text-decoration: underline;color:#0000ff;">{url_text}</span></a>')
    return text


def translate(context, string):
    return QApplication.translate(context, string, None)


def get_status(status: str) -> str:
    match status:
        case 'ongoing':
            return translate("Other", status.capitalize())
        case 'completed' | 'released':
            return translate("Other", 'completed'.capitalize())
        case _:
            if status:
                return status.capitalize()
