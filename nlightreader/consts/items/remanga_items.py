from nlightreader.consts.items.parser_items import (
    ParserItems,
)
from nlightreader.consts.items.preset_items import (
    PresetKinds as Pk,
    PresetOrders as Po,
)


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
        {"value": 1} | Pk.MANGA,
        {"value": 2} | Pk.MANHWA,
        {"value": 3} | Pk.MANHUA,
        {"value": 4} | Pk.WESTERN_COMIC,
        {"value": 5} | Pk.RU_COMIC,
        {"value": 6} | Pk.INDONESIAN_COMIC,
        {"value": 7} | Pk.OTHER,
    ]
