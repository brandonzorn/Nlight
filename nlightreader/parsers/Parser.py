from nlightreader.consts import DEFAULT_HEADERS
from nlightreader.consts.items.parser_items import ParserItems
from nlightreader.items import (
    Manga,
    Chapter,
    Image,
    RequestForm,
    Genre,
    Kind,
    Order,
    Character,
    User,
    UserRate,
)


class Parser:
    CATALOG_NAME = 'CATALOG'
    CATALOG_ID = -1
    is_primary = False

    def __init__(self):
        self.headers = DEFAULT_HEADERS
        self.cookies = None
        self.items = ParserItems

    def get_manga(self, manga: Manga) -> Manga:
        return manga

    def get_character(self, character: Character) -> Character:
        return character

    def search_manga(self, form: RequestForm) -> list[Manga]:
        return []

    def get_chapters(self, manga: Manga) -> list[Chapter]:
        return []

    def get_images(self, manga: Manga, chapter: Chapter) -> list[Image]:
        return []

    def get_image(self, image: Image):
        return

    def get_preview(self, manga: Manga):
        return

    def get_character_preview(self, character: Character):
        return

    def get_genres(self):
        return [
            Genre(i['value'], self.CATALOG_ID, i['name'], i['russian'])
            for i in self.items.GENRES
        ]

    def get_kinds(self) -> list[Kind]:
        return [
            Kind(i['value'], self.CATALOG_ID, i['name'], i['russian'])
            for i in self.items.KINDS
        ]

    def get_orders(self) -> list[Order]:
        return [
            Order(i['value'], self.CATALOG_ID, i['name'], i['russian'])
            for i in self.items.ORDERS
        ]

    def get_relations(self, manga: Manga) -> list[Manga]:
        return []

    def get_characters(self, manga: Manga) -> list[Character]:
        return []

    def get_manga_url(self, manga: Manga) -> str:
        pass


class LibParser:
    def __init__(self):
        pass

    def search_manga(self, params: RequestForm) -> list[Manga]:
        return []

    def get_user(self) -> User:
        return User(None, 'Войти', None)

    def create_user_rate(self, manga: Manga):
        pass

    def check_user_rate(self, manga: Manga):
        pass

    def delete_user_rate(self, user_rate: UserRate):
        pass

    def get_user_rate(self, manga: Manga) -> UserRate:
        pass

    def update_user_rate(self, user_rate: UserRate):
        pass
