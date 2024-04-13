from nlightreader.consts.items.parser_items import ParserItems
from nlightreader.consts.items.preset_items import PresetKinds as Pk, PresetOrders as Po


class MangaLibItems(ParserItems):
    ORDERS = [
        {"value": "rating_score"} | Po.RATING,
        {"value": "rate"} | Po.RATE_COUNT,
        {"value": "views"} | Po.VIEWS,
        {"value": "created_at"} | Po.CREATED,
        {"value": "last_chapter_at"} | Po.UPDATED,
        {"value": "chap_count"} | Po.CHAPTERS_COUNT,
    ]

    KINDS = [
        {"value": 1} | Pk.MANGA,
        {"value": 5} | Pk.MANHWA,
        {"value": 8} | Pk.RU_MANGA,
        {"value": 9} | Pk.WESTERN_COMIC,
        {"value": 4} | Pk.OEL_MANGA,
        {"value": 6} | Pk.MANHUA,
    ]
