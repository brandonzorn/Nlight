from nlightreader.consts.items.parser_items import ParserItems


class ShikimoriItems(ParserItems):
    ORDERS = [{'value': 'popularity', 'name': 'popularity', 'russian': 'Популярность'},
              {'value': 'name', 'name': 'name', 'russian': 'Название'},
              {'value': 'aired_on', 'name': 'aired_on', 'russian': 'Дата выхода'},
              {'value': 'volumes', 'name': 'volumes', 'russian': 'Тома'},
              {'value': 'chapters', 'name': 'chapters', 'russian': 'Главы'},
              {'value': 'status', 'name': 'status', 'russian': 'Статус'}]

    KINDS = [{'value': 'manga', 'name': 'manga', 'russian': 'Манга'},
             {'value': 'manhwa', 'name': 'manhwa', 'russian': 'Манхва'},
             {'value': 'manhua', 'name': 'manhua', 'russian': 'Маньхуа'},
             {'value': 'one_shot', 'name': 'one_shot', 'russian': 'Ваншот'},
             {'value': 'doujin', 'name': 'doujin', 'russian': 'Додзинси'}]
