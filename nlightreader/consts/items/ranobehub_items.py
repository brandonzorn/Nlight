from nlightreader.consts.items.parser_items import (
    ParserItems,
)
from nlightreader.consts.items.preset_items import (
    PresetOrders as Po,
)


class RanobehubItems(ParserItems):
    ORDERS = [
        {"value": ""} | Po.UPDATED,
        {"value": "created_at"} | Po.CREATED,
        {"value": "name_rus"} | Po.NAME,
        {"value": "views"} | Po.VIEWS,
        {"value": "computed_rating"} | Po.RATING,
        {"value": "count_chapters"} | Po.CHAPTERS_COUNT,
        {"value": "count_of_symbols"} | Po.TRANSLATION_VOLUME,
    ]

    GENRES = [
        {
            "value": "1",
            "name": "Horror",
            "russian": "Ужасы",
        },
        {
            "value": "2",
            "name": "Mystery",
            "russian": "Мистика",
        },
        {
            "value": "3",
            "name": "Thriller",
            "russian": "Триллер",
        },
        {
            "value": "5",
            "name": "Seinen",
            "russian": "Сэйнэн",
        },
        {
            "value": "7",
            "name": "Drama",
            "russian": "Драма",
        },
        {
            "value": "8",
            "name": "Fantasy",
            "russian": "Фэнтези",
        },
        {
            "value": "9",
            "name": "Romance",
            "russian": "Романтика",
        },
        {
            "value": "11",
            "name": "Adventure",
            "russian": "Приключение",
        },
        {
            "value": "12",
            "name": "Military",
            "russian": "Милитари",
        },
        {
            "value": "13",
            "name": "Sci-Fi",
            "russian": "Научная фантастика",
        },
        {
            "value": "14",
            "name": "Action",
            "russian": "Экшн",
        },
        {
            "value": "15",
            "name": "Shoujo",
            "russian": "Сёдзё",
        },
        {
            "value": "17",
            "name": "Comedy",
            "russian": "Комедия",
        },
        {
            "value": "18",
            "name": "Psychological",
            "russian": "Психология",
        },
        {
            "value": "19",
            "name": "Tragedy",
            "russian": "Трагедия",
        },
        {
            "value": "20",
            "name": "Supernatural",
            "russian": "Сверхъестественное",
        },
        {
            "value": "21",
            "name": "School Life",
            "russian": "Школьная жизнь",
        },
        {
            "value": "22",
            "name": "Martial Arts",
            "russian": "Боевые искусства",
        },
        {
            "value": "23",
            "name": "Shoujo Ai",
            "russian": "Сёдзё-ай",
        },
        {
            "value": "24",
            "name": "Mecha",
            "russian": "Меха",
        },
        {
            "value": "93",
            "name": "Slice of Life",
            "russian": "Повседневность",
        },
        {
            "value": "101",
            "name": "Historical",
            "russian": "Исторический",
        },
        {
            "value": "114",
            "name": "Harem",
            "russian": "Гарем",
        },
        {
            "value": "115",
            "name": "Mature",
            "russian": "Для взрослых",
        },
        {
            "value": "189",
            "name": "Shounen",
            "russian": "Сёнэн",
        },
        {
            "value": "216",
            "name": "Josei",
            "russian": "Дзёсэй",
        },
        {
            "value": "242",
            "name": "Xuanhuan",
            "russian": "Сюаньхуа",
        },
        {
            "value": "246",
            "name": "Gender Bender",
            "russian": "Гендер бендер",
        },
        {
            "value": "258",
            "name": "Adult",
            "russian": "Для взрослых",
        },
        {
            "value": "327",
            "name": "Ecchi",
            "russian": "Эччи",
        },
        {
            "value": "364",
            "name": "Xianxia",
            "russian": "Сянься",
        },
        {
            "value": "420",
            "name": "Sports",
            "russian": "Спорт",
        },
        {
            "value": "638",
            "name": "Lolicon",
            "russian": "Лоликон",
        },
        {
            "value": "680",
            "name": "Shounen Ai",
            "russian": "Сёнэн-ай",
        },
        {
            "value": "682",
            "name": "Yaoi",
            "russian": "Яой",
        },
        {
            "value": "691",
            "name": "Yuri",
            "russian": "Юри",
        },
        {
            "value": "720",
            "name": "Wuxia",
            "russian": "Уся",
        },
        {
            "value": "747",
            "name": "Smut",
            "russian": "Непристойность",
        },
        {
            "value": "907",
            "name": "eastern fantasy",
            "russian": "eastern fantasy",
        },
        {
            "value": "922",
            "name": "magical realism",
            "russian": "Магический реализм",
        },
        {
            "value": "993",
            "name": "video games",
            "russian": "video games",
        },
        {
            "value": "999",
            "name": "isekai",
            "russian": "isekai",
        },
    ]


__all__ = [
    "RanobehubItems",
]
