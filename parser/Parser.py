from items import Manga, Chapter, Image, User, RequestForm


class Parser:
    catalog_name = 'CATALOG'

    def get_manga(self, manga: Manga) -> Manga:
        return manga

    def search_manga(self, params: RequestForm) -> [Manga]:
        return []

    def get_chapters(self, manga: Manga) -> [Chapter]:
        return []

    def get_images(self, manga: Manga, chapter: Chapter) -> [Image]:
        return []

    def get_image(self, image: Image):
        pass

    def get_preview(self, manga: Manga):
        return

    def get_genres(self):
        return []

    def get_user(self) -> User:
        return User()
