import requests

HEADERS = {'User-Agent': 'Desu'}


def get_html(url: str, params=None):
    try:
        return requests.get(url, headers=HEADERS, params=params)
    except Exception as e:
        print(e)
