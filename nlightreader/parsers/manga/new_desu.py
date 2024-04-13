import json
import re

from nlightreader.consts.enums import Nl
from nlightreader.consts.items import DesuItems
from nlightreader.items import Manga, Chapter, Image, Genre, RequestForm
from nlightreader.parsers.catalogs_base import AbstractMangaCatalog
from nlightreader.utils.utils import get_html, get_data



class Config:
    def __init__(self):
        self.config = self.load_config()

    @staticmethod
    def load_config():
        with open('data/parsers/desu.json', 'r') as f:
            return json.load(f)

    def get_global_const(self, key: str):
        return self.config["consts"][key]

    def get_config_const(self, config_name: str, key: str, obj=None):
        return self.process_consts(self.config["config"][config_name][key], obj=obj)

    def process_consts(self, raw_data: str, *, obj: object = None):
        pattern1 = r"\${([^}]*)}"
        pattern2 = r"\$([^$^\s^{]+)"
        pattern3 = r"\%{([^}]*)}"
        if matches := re.findall(pattern2, raw_data):
            return self.get_global_const(matches[0])
        processed_data = re.sub(pattern1, lambda m: self.get_global_const(m.group(1)), raw_data)
        if obj:
            processed_data = re.sub(pattern3, lambda m: str(obj.__getattribute__(m.group(1))), processed_data)
        return processed_data

    def get_search_params(self, req_form: RequestForm):
        params = {}
        raw_data = self.config["config"]["search"]["params"]
        for i in raw_data:
            param_data = raw_data[i]
            param_name = param_data["name"]
            param_type = param_data["type"]
            if i == "limit":
                params[param_name] = req_form.limit
            elif i == "search":
                params[param_name] = req_form.search
            elif i == "page":
                params[param_name] = req_form.page
            elif i == "genres":
                if param_type == "comma":
                    params[param_name] = ",".join([i.content_id for i in req_form.genres])
            elif i == "orders":
                if param_type == "comma":
                    pass
                elif param_type == "value":
                    params[param_name] = req_form.order.content_id
            elif i == "kinds":
                if param_type == "comma":
                    params[param_name] = ",".join([i.content_id for i in req_form.kinds])
        return params

    def get_search_const(self, key):
        return self.process_consts(self.config["config"]["search"][key])


class NewDesu(AbstractMangaCatalog):
    CATALOG_ID = 11
    CATALOG_NAME = "NewDesu"

    def __init__(self):
        super().__init__()
        self.config = Config()
        self.items = DesuItems

    def get_manga(self, manga: Manga):
        url = f"{self.url_api}/{manga.content_id}"
        response = get_html(url, headers=self.headers, content_type="json")
        if response:
            data = get_data(response, ["response"], {})
            manga.genres = [Genre(i.get("id"), self.CATALOG_ID, i.get("text"), i.get("russian"))
                            for i in data.get("genres")]
            manga.score = data.get("score")
            manga.kind = Nl.MangaKind.from_str(data.get("kind"))
            manga.volumes = data.get("chapters").get("last").get("vol")
            manga.chapters = data.get("chapters").get("last").get("ch")
            manga.status = data.get("status")

            manga.add_description(Nl.Language.undefined, data.get("description"))
        return manga

    def search_manga(self, form: RequestForm):
        url = self.config.get_search_const("url")
        headers = self.config.get_search_const("headers")
        params = self.config.get_search_params(form)
        response = get_html(
            url, headers=headers, params=params, content_type=self.config.get_search_const("content_type"),
        )
        manga = []
        if response:
            for i in get_data(response, ["response"]):
                manga.append(
                    Manga(
                        i.get("id"), self.CATALOG_ID, i.get("name"), i.get("russian"),
                    ),
                )
        return manga

    def get_chapters(self, manga: Manga):
        url = f"{self.url_api}/{manga.content_id}"
        response = get_html(url, headers=self.headers, content_type="json")
        chapters = []
        if response:
            for i in get_data(response, ["response", "chapters", "list"]):
                vol = i.get("vol")
                ch = i.get("ch")
                vol = str(vol) if vol is not None else vol
                ch = str(ch) if ch is not None else ch
                chapter = Chapter(i.get("id"), self.CATALOG_ID, vol, ch, i.get("title"))
                chapter.language = Nl.Language.ru
                chapters.append(chapter)
        return chapters

    def get_images(self, manga: Manga, chapter: Chapter):
        url = f"{self.url_api}/{manga.content_id}/chapter/{chapter.content_id}"
        response = get_html(url, headers=self.headers, content_type="json")
        images = []
        if response:
            for i in get_data(response, ["response", "pages", "list"]):
                image_id = i.get("id")
                page = i.get("page")
                img: str = i.get("img")
                img = img.replace("desu.me", "desu.win")
                images.append(Image(image_id, page, img))
        return images

    def get_image(self, image: Image):
        headers = self.headers | {"Referer": f"{self.url}/"}
        return get_html(image.img, headers=headers, content_type="content")

    def get_preview(self, manga: Manga):
        config_name = "preview"
        url = self.config.get_config_const(config_name, "url", obj=manga)
        return get_html(url, content_type=self.config.get_config_const(config_name, "content_type"))

    def get_manga_url(self, manga: Manga) -> str:
        config_name = "manga_url"
        return self.config.get_config_const(config_name, "url", obj=manga)
