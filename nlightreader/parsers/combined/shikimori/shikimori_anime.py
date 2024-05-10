from nlightreader.consts.enums import Nl
from nlightreader.consts.urls import URL_SHIKIMORI_API, URL_SHIKIMORI, SHIKIMORI_HEADERS
from nlightreader.items import Manga, Character, RequestForm, Chapter
from nlightreader.parsers.catalogs_base import AbstractAnimeCatalog
from nlightreader.parsers.service.kodik import Kodik
from nlightreader.utils.utils import get_html


class ShikimoriAnime(AbstractAnimeCatalog):
    CATALOG_ID = 11
    CATALOG_NAME = "Shikimori(Anime)"

    def __init__(self):
        super().__init__()
        self.url = URL_SHIKIMORI
        self.url_api = URL_SHIKIMORI_API
        self.headers = SHIKIMORI_HEADERS

    def setup_manga(self, data: dict) -> Manga:
        return Manga(data.get("id"), self.CATALOG_ID, data.get("name"), data.get("russian"))

    def get_manga(self, manga: Manga) -> Manga:
        url = f"{self.url_api}/animes/{manga.content_id}"
        response = get_html(url, headers=self.headers, content_type="json")
        if response:
            data = response
            # manga.kind = Nl.MangaKind.from_str(data.get("kind"))
            manga.score = float(data.get("score"))
            manga.status = data.get("status")
            if data.get("volumes"):
                manga.volumes = int(data.get("volumes"))
            if data.get("chapters"):
                manga.chapters = int(data.get("chapters"))

            manga.add_description(Nl.Language.undefined, data.get("description"))
        return manga

    def search_manga(self, form: RequestForm):
        url = f"{self.url_api}/animes"
        params = {
            "limit": form.limit,
            "search": form.search,
            "page": form.page,
            # "order": form.get_order_id(),
            # "genre": ",".join(form.get_genre_ids()),
            # "kind": ",".join(form.get_kind_ids()),
        }
        response = get_html(url, headers=self.headers, params=params, content_type="json")
        mangas = []
        if response:
            for i in response:
                mangas.append(self.setup_manga(i))
        return mangas

    def get_chapters(self, manga: Manga) -> list[Chapter]:
        translators = Kodik.search(manga.content_id)
        chapters = []
        for translator in translators:
            vol = "1"
            for i in range(translator.episodes, 0, -1):
                ch = str(i)
                chapter = Chapter(ch, self.CATALOG_ID, vol, ch, translator.translator)
                chapter.__setattr__("url", f"http:{translator.kodik_url}")
                chapter.language = Nl.Language.ru
                chapters.append(chapter)
        return chapters

    def get_character(self, character: Character) -> Character:
        url = f"{self.url_api}/characters/{character.content_id}"
        response = get_html(url, headers=self.headers, content_type="json")
        if response:
            character.description = response.get("description")
        return character

    def get_preview(self, manga: Manga):
        return get_html(f"{self.url}/system/animes/preview/{manga.content_id}.jpg", content_type="content")

    def get_character_preview(self, character: Character):
        return get_html(f"{self.url}/system/characters/preview/{character.content_id}.jpg").content

    # def get_genres(self):
    #    url = f"{self.url_api}/genres"
    #    response = get_html(url, headers=self.headers, content_type="json")
    #    if response:
    #        return [Genre(str(i.get("id")), self.CATALOG_ID, i.get("name"), i.get("russian")) for i in response]
    #    return []

    # def get_orders(self) -> list[Order]:
    #    return [Order(i["value"], self.CATALOG_ID, i["name"], i["russian"]) for i in ShikimoriItems.ORDERS]

    def get_characters(self, manga: Manga) -> list[Character]:
        characters = []
        url = f"{self.url_api}/animes/{manga.content_id}/roles"
        response = get_html(url, headers=self.headers, content_type="json")
        if response:
            for i in response:
                if i.get("roles"):
                    role = i.get("roles")[0]
                    if role in ["Supporting", "Main"]:
                        data = i.get("character")
                        if data:
                            characters.append(Character(data.get("id"), self.CATALOG_ID, data.get("name"),
                                                        data.get("russian"), "", role))
            characters.sort(key=lambda x: x.role)
        return characters

    def get_manga_url(self, manga: Manga) -> str:
        return f"{self.url}/animes/{manga.content_id}"
