from keys import KODIK_TOKEN
from nlightreader.core.utils.types import RequestParams
from nlightreader.utils.utils import (
    dd_get,
    make_request,
)


class KodikTranslator:
    def __init__(
        self,
        content_id: str,
        kodik_url: str,
        episodes: int,
        translator: str,
        tr_type: str,
    ) -> None:
        self.content_id = content_id
        self.kodik_url = kodik_url
        self.episodes = int(episodes)
        self.translator = translator
        self.tr_type = tr_type

    @property
    def translator_text(self) -> str:
        return f"{self.translator} ({self.tr_type})"


class Kodik:
    URL_API = "https://kodik-api.com"

    @classmethod
    def search(cls, shikimori_id: str) -> list[KodikTranslator]:
        translators: list[KodikTranslator] = []
        url = f"{cls.URL_API}/search"
        params: RequestParams = {
            "token": KODIK_TOKEN,
            "shikimori_id": shikimori_id,
        }
        response = make_request(url, "GET", params=params, content_type="json")
        if not isinstance(response, dict):
            return translators
        translators_data = response.get("results")
        if not isinstance(translators_data, list):
            return translators
        for data in translators_data:
            if not isinstance(data, dict):
                continue
            content_id = data.get("id")
            if not isinstance(content_id, str):
                continue

            url = data.get("link")
            episodes = data.get("last_episode")
            if not isinstance(episodes, int):
                episodes = 1

            translator = dd_get(data, "translation.title")
            if not isinstance(translator, str):
                translator = ""
            tr_type = dd_get(data, "translation.type")
            if not isinstance(tr_type, str):
                tr_type = ""
            translators.append(
                KodikTranslator(
                    content_id=content_id,
                    kodik_url=url,
                    episodes=episodes,
                    translator=translator,
                    tr_type=tr_type,
                ),
            )
        return translators


__all__ = ["Kodik"]
