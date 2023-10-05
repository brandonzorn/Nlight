from nlightreader.consts.items.parser_items import ParserItems


class RulateItems(ParserItems):
    ORDERS = [
        {
            'value': '0',
            'name': 'By degree of readiness',
            'russian': 'По степени готовности',
        },
        {
            'value': '1',
            'name': 'Title in original language',
            'russian': 'По названию на языке оригинала',
        },
        {
            'value': '2',
            'name': 'By title in target language',
            'russian': 'По названию на языке перевода',
        },
        {
            'value': '3',
            'name': 'By creation date',
            'russian': 'По дате создания',
        },
        {
            'value': '4',
            'name': 'By last activity date',
            'russian': 'По дате последней активности',
        },
        {'value': '5', 'name': 'By views', 'russian': 'По просмотрам'},
        {'value': '6', 'name': 'By rating', 'russian': 'По рейтингу'},
        {
            'value': '7',
            'name': 'By number of translated chapters',
            'russian': 'По кол-ву переведённых глав',
        },
        {
            'value': '8',
            'name': 'By number of likes',
            'russian': 'По кол-ву лайков',
        },
        {
            'value': '10',
            'name': 'By number of pages',
            'russian': 'По кол-ву страниц',
        },
        {
            'value': '11',
            'name': 'By number of free chapters',
            'russian': 'По кол-ву бесплатных глав',
        },
        {
            'value': '12',
            'name': 'By number of reviews',
            'russian': 'По кол-ву рецензий',
        },
        {
            'value': '13',
            'name': 'By number in bookmarks',
            'russian': 'По кол-ву в закладках',
        },
        {
            'value': '14',
            'name': 'By number in favorites',
            'russian': 'По кол-ву в избранном',
        },
    ]
