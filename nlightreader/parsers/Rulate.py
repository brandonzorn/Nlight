from bs4 import BeautifulSoup

from nlightreader.consts import URL_RULATE, URL_EROLATE
from nlightreader.consts.items import RulateItems
from nlightreader.items import Manga, Chapter, Image, RequestForm, Order
from nlightreader.parsers.Parser import Parser
from nlightreader.utils.utils import get_html


class Rulate(Parser):
    catalog_name = 'Rulate'

    def __init__(self):
        super().__init__()
        self.url_api = URL_RULATE
        self.cookies = {"mature": "c3a2ed4b199a1a15f5a5483504c7a75a7030dc4bi%3A1%3B"}
        self.catalog_id = 3

    def get_manga(self, manga: Manga) -> Manga:
        html = get_html(f"{self.url_api}/book/{manga.content_id}", cookies=self.cookies)
        if html and html.status_code == 200:
            soup = BeautifulSoup(html.text, "html.parser")
            hranobe = soup.find('div', style="margin: 20px 0 0 0")
            if hranobe:
                description_text = hranobe.findAll('p')[0].text
                if description_text:
                    manga.description.update({'all': str(description_text)})
            manga.kind = 'ranobe'
        return manga

    def search_manga(self, form: RequestForm):
        ranobe = []
        params = {'t': form.search, 'cat': 12, 'Book_page': form.page, 'sort': form.order.content_id, 'adult': 0}
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
                ranobe.append(Manga(ranobe_id, self.catalog_id, name, russian))
        return ranobe

    def get_chapters(self, manga: Manga):
        chapters = []
        html = get_html(f"{self.url_api}/book/{manga.content_id}", cookies=self.cookies)
        if html and html.status_code == 200:
            soup = BeautifulSoup(html.text, "html.parser")
            ranobe_chapters = soup.findAll('tr', class_='chapter_row')
            for chapter in ranobe_chapters:
                if chapter.find('span', class_='disabled') or not chapter.find('input', class_='download_chapter'):
                    continue
                name: str = chapter.find('td', class_='t').text
                name = name.strip()
                chapter_id = chapter.unwrap()['data-id']
                chapters.append(Chapter(chapter_id, self.catalog_id, '', '', name, 'ru'))
            chapters.reverse()
        return chapters

    def get_images(self, manga: Manga, chapter: Chapter):
        url = f"{self.url_api}/book/{manga.content_id}/{chapter.content_id}/download?format=t&enc=UTF-8"
        return [Image('', 1, url)]

    def get_image(self, image: Image):
        html = get_html(image.img)
        return html.content

    def get_preview(self, manga: Manga):
        html = get_html(f"{self.url_api}/book/{manga.content_id}", cookies=self.cookies)
        if html and html.status_code == 200:
            soup = BeautifulSoup(html.text, "html.parser")
            himage = soup.find('meta', property="og:image")
            if himage:
                return get_html(str(himage['content'])).content

    def get_orders(self):
        return [Order(i['value'], self.catalog_id, i['name'], i['russian']) for i in RulateItems.ORDERS]

    def get_manga_url(self, manga: Manga) -> str:
        return f'{self.url_api}/book/{manga.content_id}'


class Erolate(Rulate):
    catalog_name = "Erolate"

    def __init__(self):
        super().__init__()
        self.url_api = URL_EROLATE
        self.cookies = {"mature": "7da3ee594b38fc5355692d978fe8f5adbeb3d17di%3A1%3B"}
        self.catalog_id = 5

    def search_manga(self, form: RequestForm):
        ranobe = []
        params = {'t': form.search, 'cat': 2, 'Book_page': form.page, 'sort': form.order.content_id, 'adult': 0}
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
                ranobe.append(Manga(ranobe_id, self.catalog_id, name, russian))
        return ranobe
