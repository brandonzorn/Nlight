from items import Manga, Chapter, Image, User, RequestForm, Genre, Kind, Order


class Parser:
    catalog_name = 'CATALOG'

    def get_manga(self, manga: Manga) -> Manga:
        return manga

    def search_manga(self, params: RequestForm) -> list[Manga]:
        return []

    def get_chapters(self, manga: Manga) -> list[Chapter]:
        return []

    def get_images(self, manga: Manga, chapter: Chapter) -> list[Image]:
        return []

    def get_image(self, image: Image):
        return

    def get_preview(self, manga: Manga):
        return

    def get_genres(self) -> list[Genre]:
        return []

    def get_kinds(self) -> list[Kind]:
        return []

    def get_orders(self) -> list[Order]:
        return []

    def get_user(self) -> User:
        return User()
