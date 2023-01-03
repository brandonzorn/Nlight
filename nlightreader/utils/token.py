import json
import os

from nlightreader.consts import TOKEN_PATH


class TokenManager:
    @staticmethod
    def save_token(token, catalog_name='Shikimori'):
        path = f'{TOKEN_PATH}/{catalog_name}'
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)
        with open(f'{path}/token.json', 'w') as f:
            f.write(json.dumps(token))

    @staticmethod
    def load_token(catalog_name):
        path = f'{TOKEN_PATH}/{catalog_name}'
        if os.path.exists(f'{path}/token.json'):
            with open(f'{path}/token.json') as f:
                data = json.load(f)
                if data:
                    return data
        return {}
