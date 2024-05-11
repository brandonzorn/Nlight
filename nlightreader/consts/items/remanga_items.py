from nlightreader.consts.items.parser_items import ParserItems
from nlightreader.consts.items.preset_items import PresetKinds as Pk, PresetOrders as Po


class RemangaItems(ParserItems):
    ORDERS = [
        {"value": "-id"} | Po.CREATED,
        {"value": "-chapter_date"} | Po.UPDATED,
        {"value": "-rating"} | Po.POPULARITY,
        {"value": "-votes"} | Po.LIKES_NUM,
        {"value": "-views"} | Po.VIEWS,
        {"value": "-count_chapters"} | Po.CHAPTERS_COUNT,
        {"value": "-random"} | Po.RANDOM,
    ]

    KINDS = [
        {"value": 0} | Pk.MANGA,
        {"value": 1} | Pk.MANHWA,
        {"value": 2} | Pk.MANHUA,
        {"value": 3} | Pk.WESTERN_COMIC,
        {"value": 4} | Pk.RU_COMIC,
        {"value": 5} | Pk.INDONESIAN_COMIC,
        {"value": 6} | Pk.OTHER,
    ]
