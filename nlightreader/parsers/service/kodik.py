from keys import KODIK_TOKEN
from nlightreader.utils.utils import get_html


class KodikTranslator:
    def __init__(self, content_id: str, kodik_url: str, episodes, translator: str, tr_type: str):
        self.content_id = content_id
        self.kodik_url = kodik_url
        self.episodes = int(episodes)
        self.translator = translator
        self.tr_type = tr_type


class Kodik:
    URL_API = "https://kodikapi.com"

    @classmethod
    def search(cls, shikimori_id) -> list[KodikTranslator]:
        translators: list[KodikTranslator] = []
        url = f"{cls.URL_API}/search"
        params = {
            "token": KODIK_TOKEN,
            "shikimori_id": shikimori_id,
        }
        response = get_html(url, params=params, content_type="json")
        if response and (results := response.get("results")):
            for data in results:
                translators.append(
                    KodikTranslator(
                        data["id"], data["link"], data["last_episode"] if "last_episode" in data else 1,
                        data["translation"]["title"], data["translation"]["type"],
                    ),
                )
        return translators
