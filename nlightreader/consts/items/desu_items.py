from nlightreader.consts.items.parser_items import ParserItems
from nlightreader.consts.items.preset_items import PresetKinds as Pk, PresetOrders as Po


class DesuItems(ParserItems):
    ORDERS = [
        {"value": "popular"} | Po.POPULARITY,
        {"value": "name"} | Po.NAME,
        {"value": "updated"} | Po.UPDATED,
    ]

    KINDS = [
        {"value": "manga"} | Pk.MANGA,
        {"value": "manhwa"} | Pk.MANHWA,
        {"value": "manhua"} | Pk.MANHUA,
        {"value": "one_shot"} | Pk.ONESHOT,
        {"value": "comics"} | Pk.COMIC,
    ]

    GENRES = [
        {
            "value": "Dementia",
            "name": "Dementia",
            "russian": "Безумие",
        },
        {
            "value": "Martial Arts",
            "name": "Martial Arts",
            "russian": "Боевые искусства",
        },
        {
            "value": "Color",
            "name": "Color",
            "russian": "В цвете",
        },
        {
            "value": "Vampire",
            "name": "Vampire",
            "russian": "Вампиры",
        },
        {
            "value": "Web",
            "name": "Web",
            "russian": "Веб",
        },
        {
            "value": "Harem",
            "name": "Harem",
            "russian": "Гарем",
        },
        {
            "value": "Heroic Fantasy",
            "name": "Heroic Fantasy",
            "russian": "Героическое фэнтези",
        },
        {
            "value": "Demons",
            "name": "Demons",
            "russian": "Демоны",
        },
        {
            "value": "Mystery",
            "name": "Mystery",
            "russian": "Детектив",
        },
        {
            "value": "Josei",
            "name": "Josei",
            "russian": "Дзёсей",
        },
        {
            "value": "Drama",
            "name": "Drama",
            "russian": "Драма",
        },
        {
            "value": "Yonkoma",
            "name": "Yonkoma",
            "russian": "Ёнкома",
        },
        {
            "value": "Game",
            "name": "Game",
            "russian": "Игры",
        },
        {
            "value": "Isekai",
            "name": "Isekai",
            "russian": "Исекай",
        },
        {
            "value": "Historical",
            "name": "Historical",
            "russian": "Исторический",
        },
        {
            "value": "Comedy",
            "name": "Comedy",
            "russian": "Комедия",
        },
        {
            "value": "Space",
            "name": "Space",
            "russian": "Космос",
        },
        {
            "value": "LitRPG",
            "name": "LitRPG",
            "russian": "ЛитRPG",
        },
        {
            "value": "Magic",
            "name": "Magic",
            "russian": "Магия",
        },
        {
            "value": "Mecha",
            "name": "Mecha",
            "russian": "Меха",
        },
        {
            "value": "Mystic", "name": "Mystic", "russian": "Мистика",
        },
        {
            "value": "Music", "name": "Music", "russian": "Музыка",
        },
        {
            "value": "Sci-Fi", "name": "Sci-Fi", "russian": "Научная фантастика",
        },
        {
            "value": "Parody", "name": "Parody", "russian": "Пародия",
        },
        {
            "value": "Slice of Life",
            "name": "Slice of Life",
            "russian": "Повседневность",
        },
        {
            "value": "Post Apocalyptic",
            "name": "Post Apocalyptic",
            "russian": "Постапокалиптика",
        },
        {
            "value": "Adventure",
            "name": "Adventure",
            "russian": "Приключения",
        },
        {
            "value": "Psychological",
            "name": "Psychological",
            "russian": "Психологическое",
        },
        {
            "value": "Romance",
            "name": "Romance",
            "russian": "Романтика",
        },
        {
            "value": "Samurai",
            "name": "Samurai",
            "russian": "Самураи",
        },
        {
            "value": "Supernatural",
            "name": "Supernatural",
            "russian": "Сверхъестественное",
        },
        {
            "value": "Shoujo",
            "name": "Shoujo",
            "russian": "Сёдзе",
        },
        {
            "value": "Shoujo Ai",
            "name": "Shoujo Ai",
            "russian": "Сёдзе Ай",
        },
        {
            "value": "Seinen",
            "name": "Seinen",
            "russian": "Сейнен",
        },
        {
            "value": "Shounen",
            "name": "Shounen",
            "russian": "Сёнен",
        },
        {
            "value": "Shounen Ai",
            "name": "Shounen Ai",
            "russian": "Сёнен Ай",
        },
        {
            "value": "Gender Bender",
            "name": "Gender Bender",
            "russian": "Смена пола",
        },
        {
            "value": "Sports",
            "name": "Sports",
            "russian": "Спорт",
        },
        {
            "value": "Super Power",
            "name": "Super Power",
            "russian": "Супер сила",
        },
        {
            "value": "Tragedy",
            "name": "Tragedy",
            "russian": "Трагедия",
        },
        {
            "value": "Thriller",
            "name": "Thriller",
            "russian": "Триллер",
        },
        {
            "value": "Horror",
            "name": "Horror",
            "russian": "Ужасы",
        },
        {
            "value": "Fiction",
            "name": "Fiction",
            "russian": "Фантастика",
        },
        {
            "value": "Fantasy",
            "name": "Fantasy",
            "russian": "Фэнтези",
        },
        {
            "value": "Hentai",
            "name": "Hentai",
            "russian": "Хентай",
        },
        {
            "value": "School",
            "name": "School",
            "russian": "Школа",
        },
        {
            "value": "Action",
            "name": "Action",
            "russian": "Экшен",
        },
        {
            "value": "Ecchi",
            "name": "Ecchi",
            "russian": "Этти",
        },
        {
            "value": "Yuri",
            "name": "Yuri",
            "russian": "Юри",
        },
        {
            "value": "Yaoi",
            "name": "Yaoi",
            "russian": "Яой",
        },
    ]
