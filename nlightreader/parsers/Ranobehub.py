import base64
from bs4 import BeautifulSoup

from nlightreader.consts import URL_RANOBEHUB_API, URL_RANOBEHUB
from nlightreader.consts.items import RanobehubItems
from nlightreader.items import RequestForm, Manga, Chapter, Image
from nlightreader.parsers.Parser import Parser
from nlightreader.utils.utils import get_html, get_data


class Ranobehub(Parser):
    catalog_name = 'Ranobehub'

    def __init__(self):
        super().__init__()
        self.url_api = URL_RANOBEHUB_API
        self.catalog_id = 4
        self.items = RanobehubItems

    def get_manga(self, manga: Manga) -> Manga:
        url = f'{self.url_api}/ranobe/{manga.content_id}'
        html = get_html(url, self.headers)
        if html and html.status_code == 200 and html.json():
            data = html.json().get('data')
            manga.kind = "ranobe"
            manga.score = data.get('rating')
            manga.description.update({'all': data.get('description')})
        return manga

    def search_manga(self, form: RequestForm):
        url = f'{self.url_api}/search'
        params = {'title-contains': form.search, 'page': form.page, 'sort': form.order.content_id,
                  'tags:positive[]': [int(i) for i in form.get_genre_id()]}
        html = get_html(url, self.headers, params)
        manga = []
        if html and html.status_code == 200 and html.json():
            for i in html.json().get('resource'):
                manga_id = i.get('id')
                name = i.get('names').get('eng')
                russian = i.get('names').get('rus')
                manga.append(Manga(manga_id, self.catalog_id, name, russian))
        return manga

    def get_chapters(self, manga: Manga) -> list[Chapter]:
        url = f'{self.url_api}/ranobe/{manga.content_id}/contents'
        html = get_html(url, self.headers)
        chapters = []
        if html and html.status_code == 200 and html.json():
            for i in get_data(html.json(), ['volumes']):
                volume_num = i.get('num')
                for chapter_data in get_data(i, ['chapters']):
                    chapters.append(Chapter(chapter_data.get('id'), self.catalog_id, volume_num,
                                            chapter_data.get('num'), chapter_data.get('name'), 'ru'))
            chapters.reverse()
        return chapters

    def get_images(self, manga: Manga, chapter: Chapter) -> list[Image]:
        url = f"https://ranobehub.org/ranobe/{manga.content_id}/{chapter.vol}/{chapter.ch}"
        return [Image('', 1, url)]

    def get_image(self, image: Image):
        def get_chapter_content_image(media_id):
            url = f'https://ranobehub.org/api/media/{media_id}'
            chapter_image = get_html(url, self.headers).content
            str_equivalent_image = base64.b64encode(chapter_image).decode()
            return f"data:image/png;base64,{str_equivalent_image}"
        html = get_html(image.img)
        content = ""
        if html and html.status_code == 200:
            soup = BeautifulSoup(html.text, "html.parser")
            try:
                header = soup.find('div', class_="title-wrapper")
                content += f"<h1>{header.find('h1', class_='ui header').text}</h1>"
            except Exception as e:
                print("Header not found", e)
            text_containers = soup.findAll("div", {'class': "ui text container"})
            for i in text_containers:
                if i.has_attr("data-container"):
                    for p in i.findAll('p'):
                        if p.find('img'):
                            content += f'<p>' \
                                       f'<img src="{get_chapter_content_image(p.find("img")["data-media-id"])}">' \
                                       f'</p>'
                        else:
                            content += str(p)
                    break
        return content

    def get_preview(self, manga: Manga):
        url = f'{self.url_api}/ranobe/{manga.content_id}'
        html = get_html(url, self.headers)
        if html and html.status_code == 200 and html.json():
            img = html.json().get('data').get('posters').get('big')
            return get_html(img).content

    def get_manga_url(self, manga: Manga) -> str:
        return f'{URL_RANOBEHUB}/ranobe/{manga.content_id}'
