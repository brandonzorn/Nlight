import json
from pathlib import Path

from nlightreader.consts.paths import TOKEN_PATH


class TokenManager:
    @staticmethod
    def save_token(token, catalog_name):
        """
        Saves a token dictionary to disk.

        :param token: A dictionary containing authentication token data.
        :param catalog_name: The name of the parser for which the token is being saved.
        """
        path = Path(f"{TOKEN_PATH}/{catalog_name}")
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)
        with Path(f"{path}/token.json").open("w") as f:
            f.write(json.dumps(token))

    @staticmethod
    def load_token(catalog_name):
        """
        Loads a token dictionary from disk.

        :param catalog_name: The name of the parser for which the token is being loaded.
        :return: A dictionary containing authentication token data, or an empty dictionary if no token is found.
        """
        path = f"{TOKEN_PATH}/{catalog_name}"
        if Path(f"{path}/token.json").exists():
            with Path(f"{path}/token.json").open() as f:
                data = json.load(f)
                if data:
                    return data
        return {}
