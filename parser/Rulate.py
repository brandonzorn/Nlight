from bs4 import BeautifulSoup

from const import URL_RULATE, DEFAULT_HEADERS
from items import Manga, Chapter, Image, RequestForm
from parser.Parser import Parser
from utils import get_html


class Rulate(Parser):
    catalog_name = 'Rulate'

    def __init__(self):
        self.url_api = URL_RULATE
        self.headers = DEFAULT_HEADERS
        self.catalog_id = 3

    def get_manga(self, manga: Manga) -> Manga:
        html = get_html(f"{self.url_api}/book/{manga.id}")
        soup = BeautifulSoup(html.text, "html.parser")
        hranobe = soup.find('div', style="margin: 20px 0 0 0")
        description = hranobe.findAll('p')[0].text
        manga.description = description
        return manga

    def search_manga(self, params: RequestForm):
        params = {'t': params.search, 'cat': 12, 'Book_page': params.page, 'sort': 5}
        html = get_html(f"{self.url_api}/search", params=params)
        soup = BeautifulSoup(html.text, "html.parser")
        hranobe = soup.findAll('p', class_='book-tooltip')
        ranobe = []
        for i in hranobe:
            name = i.text.strip()
            ranobe_id = i.unwrap()['data-tooltip-content'].split('#book-tooltip-')[-1]
            data = {'id': ranobe_id, 'name': name, 'catalog_id': self.catalog_id, 'kind': 'ranobe'}
            ranobe.append(Manga(data))
        return ranobe

    def get_chapters(self, manga: Manga):
        chapters = []
        a = get_html(f"{self.url_api}/book/{manga.id}")
        soup = BeautifulSoup(a.text, "html.parser")
        ranobe_chapters = soup.findAll('tr', class_='chapter_row')
        for chapter in ranobe_chapters:
            name: str = chapter.find('td', class_='t').text
            name = name.strip()
            chapter_id = chapter.unwrap()['data-id']
            chapters.append(Chapter(chapter_id, None, None, name, 'ru'))
        chapters.reverse()
        return chapters

    def get_images(self, manga: Manga, chapter: Chapter):
        url = f"{self.url_api}/book/{manga.id}/{chapter.id}/download?format=t&enc=UTF-8"
        return [Image('', 1, url)]

    def get_image(self, image: Image):
        a = get_html(image.img)
        return a

    def get_preview(self, manga: Manga):
        a = get_html(f"{self.url_api}/book/{manga.id}")
        soup = BeautifulSoup(a.text, "html.parser")
        himage = soup.find('meta', property="og:image")
        return get_html(himage['content'])
