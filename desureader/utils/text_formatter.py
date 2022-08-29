import re


class TextFormatter:
    @staticmethod
    def description_to_html(text: str) -> str:
        if not text:
            return ""
        for ch_id, name in re.findall(r"\[character=(\w+)](.+?)\[/character]", text):
            text = text.replace(f"[character={ch_id}]{name}[/character]",
                                f'<span style=" color:#177e00;">{name}</span>')
        return text
