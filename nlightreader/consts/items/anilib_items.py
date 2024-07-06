from nlightreader.consts.items.lib_base_items import (
    LibBaseItems,
)
from nlightreader.consts.items.preset_items import (
    PresetKinds as Pk,
    PresetOrders as Po,
)


class AniLibItems(LibBaseItems):
    ORDERS = [
        {"value": None} | Po.POPULARITY,
        {"value": "rate_avg"} | Po.RATING,
        {"value": "views"} | Po.VIEWS,
        {"value": "episodes_count"} | Po.EPISODES_COUNT,
        {"value": "releaseDate"} | Po.AIRED_ON,
        {"value": "last_episode_at"} | Po.UPDATED,
        {"value": "created_at"} | Po.CREATED,
        {"value": "name"} | Po.NAME,
        {"value": "rus_name"} | Po.RUS_NAME,
    ]

    KINDS = [
        {"value": 16} | Pk.TV,
        {"value": 17} | Pk.MOVIE,
        {
            "value": 18,
            "name": "Short film",
            "russian": "Короткометражка",
        },
        {"value": 19} | Pk.SPECIAL,
        {"value": 20} | Pk.OVA,
        {"value": 21} | Pk.ONA,
        {"value": 22} | Pk.MUSIC,
    ]
