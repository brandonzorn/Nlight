import json
from pathlib import Path

from nlightreader.consts.paths import TOKEN_PATH


class TokenManager:
    @staticmethod
    def save_token(token: dict, catalog_name: str):
        """
        Saves a token dictionary to disk.

        :param token: A dictionary containing
            authentication token data.
        :param catalog_name: The name of the parser
            for which the token is being saved.
        """
        path = Path(TOKEN_PATH, catalog_name)
        token_file_path = path / "token.json"
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)
        with token_file_path.open("w") as f:
            f.write(json.dumps(token))

    @staticmethod
    def load_token(catalog_name):
        """
        Loads a token dictionary from disk.

        :param catalog_name:
            The name of the parser for which the token is being loaded.
        :return:
            A dictionary containing authentication token data,
            or an empty dictionary if no token is found.
        """
        path = Path(TOKEN_PATH, catalog_name)
        token_file_path = path / "token.json"
        if token_file_path.exists():
            with token_file_path.open() as f:
                data = json.load(f)
                if data:
                    return data
        return {}
