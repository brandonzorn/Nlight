import re

from PySide6.QtWidgets import QApplication


class TextFormatter:
    """
    A class for formatting text with spoilers, character names, and URLs.

    Args:
        text (str): The text to be formatted.
        show_spoilers (bool, optional): Whether or not to show spoiler text. Defaults to False.

    Methods:
        replace_spoilers(): Replaces spoiler tags in the text with HTML span tags.
        replace_characters(): Replaces character tags in the text with HTML span tags.
        replace_urls(): Replaces URL tags in the text with HTML anchor tags.
        to_html_text(): Formats the text and returns it as HTML text.
    """

    def __init__(self, text: str, show_spoilers=False):
        self._text = " ".join(text.splitlines())
        self._show_spoilers = show_spoilers

    def replace_spoilers(self):
        for i, spoiler_text in re.findall(r"\[spoiler=(\w+)](.+?)\[/spoiler]", self._text, re.DOTALL):
            spoiler = spoiler_text
            if not self._show_spoilers:
                spoiler = ""
            self._text = self._text.replace(
                f"[spoiler={i}]{spoiler_text}[/spoiler]", f'<span style=" color:#951a00;">{spoiler}</span>',
            )
        for spoiler_text in re.findall(r"\[spoiler](.+?)\[/spoiler]", self._text, re.DOTALL):
            spoiler = spoiler_text
            if not self._show_spoilers:
                spoiler = ""
            self._text = self._text.replace(
                f"[spoiler]{spoiler_text}[/spoiler]", f'<span style=" color:#951a00;">{spoiler}</span>',
            )

    def replace_characters(self):
        for ch_id, name in re.findall(r"\[character=(\w+)](.+?)\[/character]", self._text, re.DOTALL):
            self._text = self._text.replace(
                f"[character={ch_id}]{name}[/character]", f'<span style=" color:#177e00;">{name}</span>',
            )
        for ch_id, name in re.findall(r"\[character=(\w+) (.+?)]", self._text, re.DOTALL):
            self._text = self._text.replace(
                f"[character={ch_id} {name}]", f'<span style=" color:#177e00;">{name}</span>',
            )

    def replace_urls(self):
        for url, url_text in re.findall(r"\[url=(.+?)](.+?)\[/url]", self._text, re.DOTALL):
            self._text = self._text.replace(
                f"[url={url}]{url_text}[/url]",
                f'<a href="{url}">' f'<span style="text-decoration: underline;color:#0000ff;">{url_text}</span></a>',
            )

    def to_html_text(self) -> str:
        self.replace_urls()
        self.replace_characters()
        self.replace_spoilers()
        return self._text


def description_to_html(text: str, show_spoilers=False) -> str:
    if not text:
        return ""
    text = TextFormatter(text, show_spoilers).to_html_text()
    return text


def translate(context, string):
    """
    Translates a string using the current translation context.

    Args:
        context: The context in which the string appears.
        string: The string to be translated.

    Returns:
        A translated version of the input string.
    """
    return QApplication.translate(context, string, None)


def get_status(status: str) -> str:
    """
    Translates the status of a manga.

    Args:
        status (str or None): The status of the manga.

    Returns:
        A translation of the status if it is 'ongoing', 'completed', or 'released'.
        Otherwise, returns the original status.
    """
    if status is None:
        return ""
    match status:
        case "ongoing":
            return translate("Status", status.capitalize())
        case "completed" | "released":
            return translate("Status", "completed".capitalize())
        case _:
            return status.capitalize()
