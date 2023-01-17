from bs4 import BeautifulSoup

from nlightreader.consts import URL_RULATE, DEFAULT_HEADERS
from nlightreader.items import Manga, Chapter, Image, RequestForm
from nlightreader.parsers.Parser import Parser
from nlightreader.utils.utils import get_html, create_item_id


class Rulate(Parser):
    catalog_name = 'Rulate'

    def __init__(self):
        self.url_api = URL_RULATE
        self.headers = DEFAULT_HEADERS
        self.catalog_id = 3

    def get_manga(self, manga: Manga) -> Manga:
        html = get_html(f"{self.url_api}/book/{manga.content_id}")
        if html and html.status_code == 200:
            soup = BeautifulSoup(html.text, "html.parser")
            hranobe = soup.find('div', style="margin: 20px 0 0 0")
            description = hranobe.findAll('p')[0].text
            manga.kind = 'ranobe'
            manga.description = description
        return manga

    def search_manga(self, params: RequestForm):
        ranobe = []
        params = {'t': params.search, 'cat': 12, 'Book_page': params.page, 'sort': 5}
        html = get_html(f"{self.url_api}/search", params=params)
        if html and html.status_code == 200:
            soup = BeautifulSoup(html.text, "html.parser")
            hranobe = soup.findAll('p', class_='book-tooltip')
            for i in hranobe:
                name_text = i.text.strip()
                name_items = name_text.split('/')
                name = name_text
                russian = ''
                if len(name_items) == 2:
                    name = name_items[0].strip()
                    russian = name_items[1].strip()
                ranobe_id = i.unwrap()['data-tooltip-content'].split('#book-tooltip-')[-1]
                ranobe.append(Manga(create_item_id(self.catalog_id, ranobe_id),
                                    ranobe_id, self.catalog_id, name, russian))
        return ranobe

    def get_chapters(self, manga: Manga):
        chapters = []
        html = get_html(f"{self.url_api}/book/{manga.content_id}")
        if html and html.status_code == 200:
            soup = BeautifulSoup(html.text, "html.parser")
            ranobe_chapters = soup.findAll('tr', class_='chapter_row')
            for chapter in ranobe_chapters:
                name: str = chapter.find('td', class_='t').text
                name = name.strip()
                chapter_id = chapter.unwrap()['data-id']
                chapters.append(Chapter(create_item_id(self.catalog_id, chapter_id),
                                        chapter_id, self.catalog_id, '', '', name, 'ru'))
            chapters.reverse()
        return chapters

    def get_images(self, manga: Manga, chapter: Chapter):
        url = f"{self.url_api}/book/{manga.content_id}/{chapter.content_id}/download?format=t&enc=UTF-8"
        return [Image('', 1, url)]

    def get_image(self, image: Image):
        html = get_html(image.img)
        return html

    def get_preview(self, manga: Manga):
        html = get_html(f"{self.url_api}/book/{manga.content_id}")
        if html and html.status_code == 200:
            soup = BeautifulSoup(html.text, "html.parser")
            himage = soup.find('meta', property="og:image")
            return get_html(himage['content'])

    def get_manga_url(self, manga: Manga) -> str:
        return f'{URL_RULATE}/book/{manga.content_id}'
