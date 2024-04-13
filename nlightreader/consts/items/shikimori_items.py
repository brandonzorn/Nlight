from nlightreader.consts.items.parser_items import ParserItems
from nlightreader.consts.items.preset_items import PresetKinds as Pk, PresetOrders as Po


class ShikimoriItems(ParserItems):
    ORDERS = [
        {"value": "popularity"} | Po.POPULARITY,
        {"value": "name"} | Po.NAME,
        {"value": "aired_on"} | Po.AIRED_ON,
        {"value": "volumes"} | Po.VOLUMES_COUNT,
        {"value": "chapters"} | Po.CHAPTERS_COUNT,
        {"value": "status"} | Po.STATUS,
    ]

    KINDS = [
        {"value": "manga"} | Pk.MANGA,
        {"value": "manhwa"} | Pk.MANHWA,
        {"value": "manhua"} | Pk.MANHUA,
        {"value": "one_shot"} | Pk.ONESHOT,
        {"value": "doujin"} | Pk.DOUJIN,
    ]
