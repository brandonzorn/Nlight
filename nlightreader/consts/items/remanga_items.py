from nlightreader.consts.items.parser_items import ParserItems


class RemangaItems(ParserItems):
    KINDS = [
        {'value': 0, 'name': 'Manga', 'russian': 'Манга'},
        {'value': 1, 'name': 'Manhwa', 'russian': 'Манхва'},
        {'value': 2, 'name': 'Manhua', 'russian': 'Маньхуа'},
        {'value': 3, 'name': 'Western comic', 'russian': 'Западный комикс'},
        {'value': 4, 'name': 'Rucomics', 'russian': 'Рукомикс'},
        {
            'value': 5,
            'name': 'Indonesian comic',
            'russian': 'Индонезийский комикс',
        },
        {'value': 6, 'name': 'Other', 'russian': 'Другое'},
    ]

    ORDERS = [
        {'value': '-id', 'name': 'By date added', 'russian': 'По новизне'},
        {
            'value': '-chapter_date',
            'name': 'By update date',
            'russian': 'По последним обновлениям',
        },
        {
            'value': '-rating',
            'name': 'By popularity',
            'russian': 'По популярности',
        },
        {'value': '-votes', 'name': 'By likes', 'russian': 'По лайкам'},
        {'value': '-views', 'name': 'By views', 'russian': 'По просмотрам'},
        {
            'value': '-count_chapters',
            'name': 'By number of chapters',
            'russian': 'По кол-ву глав',
        },
        {'value': '-random', 'name': 'Random', 'russian': 'Мне повезет'},
    ]
