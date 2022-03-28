import requests
from const import HEADERS


def get_html(url: str, params=None):
    try:
        return requests.get(url, headers=HEADERS, params=params)
    except Exception as e:
        print(e)
