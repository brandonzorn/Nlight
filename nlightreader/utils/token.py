import json
from pathlib import Path
from typing import Any

from nlightreader.consts.paths import TOKEN_PATH


class TokenManager:
    @staticmethod
    def save_token(token: dict[str, Any], catalog_name: str) -> None:
        """
        Saves a token dictionary to disk.

        :param token: A dictionary containing
            authentication token data.
        :param catalog_name: The name of the parser
            for which the token is being saved.
        """
        path = Path(TOKEN_PATH, catalog_name)
        path.mkdir(parents=True, exist_ok=True)

        token_file_path = path / "token.json"
        with token_file_path.open("w", encoding="utf-8") as f:
            json.dump(token, f, ensure_ascii=False, indent=4)

    @staticmethod
    def load_token(catalog_name: str) -> dict[str, Any]:
        """
        Loads a token dictionary from a disk.

        :param catalog_name: The name of the parser for which
            the token is being loaded.
        :return: A dictionary containing authentication token data,
            or an empty dictionary if no token is found
            or if the file is corrupted.
        """
        path = Path(TOKEN_PATH, catalog_name)
        token_file_path = path / "token.json"
        if token_file_path.exists():
            with token_file_path.open("r", encoding="utf-8") as f:
                data = json.load(f)
                if data:
                    return data
        return {}


__all__ = ["TokenManager"]
