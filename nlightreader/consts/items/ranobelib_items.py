from nlightreader.consts.items.lib_base_items import (
    LibBaseItems,
)
from nlightreader.consts.items.preset_items import (
    PresetOrders as Po,
)


class RanobeLibItems(LibBaseItems):
    ORDERS = [
        {"value": None} | Po.POPULARITY,
        {"value": "rate_avg"} | Po.RATING,
        {"value": "views"} | Po.VIEWS,
        {"value": "chap_count"} | Po.CHAPTERS_COUNT,
        {"value": "releaseDate"} | Po.AIRED_ON,
        {"value": "last_chapter_at"} | Po.UPDATED,
        {"value": "created_at"} | Po.CREATED,
        {"value": "name"} | Po.NAME,
        {"value": "rus_name"} | Po.RUS_NAME,
    ]

    KINDS = [
        {
            "value": 10,
            "name": "Japan",
            "russian": "Япония",
        },
        {
            "value": 11,
            "name": "Korea",
            "russian": "Корея",
        },
        {
            "value": 12,
            "name": "China",
            "russian": "Китай",
        },
        {
            "value": 13,
            "name": "English",
            "russian": "Английский",
        },
        {
            "value": 14,
            "name": "Original",
            "russian": "Авторский",
        },
        {
            "value": 15,
            "name": "Fanfiction",
            "russian": "Фанфик",
        },
    ]


__all__ = [
    "RanobeLibItems",
]
