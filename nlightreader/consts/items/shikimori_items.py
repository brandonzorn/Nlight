from nlightreader.consts.items.parser_items import (
    ParserItems,
)
from nlightreader.consts.items.preset_items import (
    PresetKinds as Pk,
    PresetOrders as Po,
)


class ShikimoriItems(ParserItems):
    ORDERS = [
        {"value": "ranked"} | Po.RATING,
        {"value": "popularity"} | Po.POPULARITY,
        {"value": "name"} | Po.NAME,
        {"value": "aired_on"} | Po.AIRED_ON,
        {"value": "volumes"} | Po.VOLUMES_COUNT,
        {"value": "chapters"} | Po.CHAPTERS_COUNT,
        {"value": "status"} | Po.STATUS,
        {"value": "id"} | Po.ID,
    ]

    KINDS = [
        {"value": "manga"} | Pk.MANGA,
        {"value": "manhwa"} | Pk.MANHWA,
        {"value": "manhua"} | Pk.MANHUA,
        {"value": "one_shot"} | Pk.ONESHOT,
        {"value": "doujin"} | Pk.DOUJIN,
    ]


class ShikimoriAnimeItems(ParserItems):
    ORDERS = [
        {"value": "ranked"} | Po.RATING,
        {"value": "popularity"} | Po.POPULARITY,
        {"value": "name"} | Po.NAME,
        {"value": "aired_on"} | Po.AIRED_ON,
        {"value": "status"} | Po.STATUS,
        {"value": "id"} | Po.ID,
    ]

    KINDS = [
        {"value": "tv"} | Pk.TV,
        {"value": "ova"} | Pk.OVA,
        {"value": "ona"} | Pk.ONA,
        {"value": "special"} | Pk.SPECIAL,
        {"value": "tv_special"} | Pk.TV_SPECIAL,
        {"value": "music"} | Pk.MUSIC,
        {"value": "pv"} | Pk.PV,
        {"value": "cm"} | Pk.CM,
    ]


__all__ = [
    "ShikimoriAnimeItems",
    "ShikimoriItems",
]
