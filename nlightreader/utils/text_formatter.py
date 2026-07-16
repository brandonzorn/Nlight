import re


class TextFormatter:
    def __init__(self, text: str, show_spoilers: bool = False) -> None:
        self._text = text
        self._show_spoilers = show_spoilers

    def _replace_spoilers(self, text: str) -> str:
        pattern = r"\[spoiler(?:=[^\]]+)?\](.*?)\[/spoiler\]"

        def repl(match: re.Match) -> str:
            spoiler_content = match.group(1) if self._show_spoilers else ""
            return f'<span style="color:#951a00;">{spoiler_content}</span>'

        return re.sub(pattern, repl, text, flags=re.DOTALL)

    def _replace_characters(self, text: str) -> str:
        text = re.sub(
            r"\[character=[^]]+](.*?)\[/character]",
            r'<span style="color:#177e00;">\1</span>',
            text,
            flags=re.DOTALL,
        )
        return re.sub(
            r"\[character=[^ ]+ ([^]]+)]",
            r'<span style="color:#177e00;">\1</span>',
            text,
            flags=re.DOTALL,
        )

    def _replace_urls(self, text: str) -> str:
        return re.sub(
            r"\[url=([^]]+)](.*?)\[/url]",
            r'<a href="\1">'
            r'<span style="text-decoration:underline;color:#0000ff;">\2</span>'
            r"</a>",
            text,
            flags=re.DOTALL,
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
