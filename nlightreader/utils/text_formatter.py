import re


class TextFormatter:
    _RE_SPOILER = re.compile(
        r"\[(?P<tag>spoiler(?:_block)?)(?:=[^]]+)?](.*?)\[/(?P=tag)]",
        re.DOTALL,
    )
    _RE_CHAR_PAIR = re.compile(
        r"\[character=[^]]+](.*?)\[/character]",
        re.DOTALL,
    )
    _RE_CHAR_SINGLE = re.compile(
        r"\[character=[^\s\]]+\s+([^]]+)]",
        re.DOTALL,
    )
    _RE_URL = re.compile(
        r"\[url=([^]]+)](.*?)\[/url]",
        re.DOTALL,
    )

    _COLOR_SPOILER = "#951a00"
    _COLOR_CHARACTER = "#177e00"
    _COLOR_URL = "#0000ff"

    def __init__(self, text: str, show_spoilers: bool = False) -> None:
        self._text = text
        self._show_spoilers = show_spoilers

    def _replace_spoilers(self, text: str) -> str:
        replacement = rf'<span style="color:{self._COLOR_SPOILER};">\2</span>'

        if not self._show_spoilers:
            return self._RE_SPOILER.sub("", text)
        return self._RE_SPOILER.sub(replacement, text)

    def _replace_characters(self, text: str) -> str:
        replacement = (
            rf'<span style="color:{self._COLOR_CHARACTER};">\1</span>'
        )

        text = self._RE_CHAR_PAIR.sub(replacement, text)
        return self._RE_CHAR_SINGLE.sub(replacement, text)

    def _replace_urls(self, text: str) -> str:
        replacement = (
            r'<a href="\1">'
            r'<span style="'
            r"text-decoration:underline;"
            rf'color:{self._COLOR_URL};">'
            r"\2"
            r"</span></a>"
        )

        return self._RE_URL.sub(
            replacement,
            text,
        )

    def to_html_text(self) -> str:
        if not self._text:
            return ""
        html_text = self._text.replace("\n", "<br>")
        html_text = self._replace_urls(html_text)
        html_text = self._replace_characters(html_text)
        return self._replace_spoilers(html_text)


def description_to_html(text: str, show_spoilers: bool = False) -> str:
    if not text:
        return ""
    return TextFormatter(text, show_spoilers).to_html_text()


__all__ = [
    "TextFormatter",
    "description_to_html",
]
