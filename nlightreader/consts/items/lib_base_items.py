from nlightreader.consts.items.parser_items import (
    ParserItems,
)


class LibBaseItems(ParserItems):
    GENRES = [
        {
            "value": 32,
            "name": "Арт",
            "russian": "Арт",
        },
        {
            "value": 91,
            "name": "Безумие",
            "russian": "Безумие",
        },
        {
            "value": 34,
            "name": "Боевик",
            "russian": "Боевик",
        },
        {
            "value": 35,
            "name": "Боевые искусства",
            "russian": "Боевые искусства",
        },
        {
            "value": 36,
            "name": "Вампиры",
            "russian": "Вампиры",
        },
        {
            "value": 89,
            "name": "Военное",
            "russian": "Военное",
        },
        {
            "value": 37,
            "name": "Гарем",
            "russian": "Гарем",
        },
        {
            "value": 38,
            "name": "Гендерная интрига",
            "russian": "Гендерная интрига",
        },
        {
            "value": 39,
            "name": "Героическое фэнтези",
            "russian": "Героическое фэнтези",
        },
        {
            "value": 81,
            "name": "Демоны",
            "russian": "Демоны",
        },
        {
            "value": 40,
            "name": "Детектив",
            "russian": "Детектив",
        },
        {
            "value": 88,
            "name": "Детское",
            "russian": "Детское",
        },
        {
            "value": 41,
            "name": "Дзёсэй",
            "russian": "Дзёсэй",
        },
        {
            "value": 43,
            "name": "Драма",
            "russian": "Драма",
        },
        {
            "value": 44,
            "name": "Игра",
            "russian": "Игра",
        },
        {
            "value": 79,
            "name": "Исекай",
            "russian": "Исекай",
        },
        {
            "value": 45,
            "name": "История",
            "russian": "История",
        },
        {
            "value": 46,
            "name": "Киберпанк",
            "russian": "Киберпанк",
        },
        {
            "value": 76,
            "name": "Кодомо",
            "russian": "Кодомо",
        },
        {
            "value": 47,
            "name": "Комедия",
            "russian": "Комедия",
        },
        {
            "value": 83,
            "name": "Космос",
            "russian": "Космос",
        },
        {
            "value": 85,
            "name": "Магия",
            "russian": "Магия",
        },
        {
            "value": 48,
            "name": "Махо-сёдзё",
            "russian": "Махо-сёдзё",
        },
        {
            "value": 90,
            "name": "Машины",
            "russian": "Машины",
        },
        {
            "value": 49,
            "name": "Меха",
            "russian": "Меха",
        },
        {
            "value": 50,
            "name": "Мистика",
            "russian": "Мистика",
        },
        {
            "value": 80,
            "name": "Музыка",
            "russian": "Музыка",
        },
        {
            "value": 51,
            "name": "Научная фантастика",
            "russian": "Научная фантастика",
        },
        {
            "value": 77,
            "name": "Омегаверс",
            "russian": "Омегаверс",
        },
        {
            "value": 86,
            "name": "Пародия",
            "russian": "Пародия",
        },
        {
            "value": 52,
            "name": "Повседневность",
            "russian": "Повседневность",
        },
        {
            "value": 82,
            "name": "Полиция",
            "russian": "Полиция",
        },
        {
            "value": 53,
            "name": "Постапокалиптика",
            "russian": "Постапокалиптика",
        },
        {
            "value": 54,
            "name": "Приключения",
            "russian": "Приключения",
        },
        {
            "value": 55,
            "name": "Психология",
            "russian": "Психология",
        },
        {
            "value": 56,
            "name": "Романтика",
            "russian": "Романтика",
        },
        {
            "value": 57,
            "name": "Самурайский боевик",
            "russian": "Самурайский боевик",
        },
        {
            "value": 58,
            "name": "Сверхъестественное",
            "russian": "Сверхъестественное",
        },
        {
            "value": 59,
            "name": "Сёдзё",
            "russian": "Сёдзё",
        },
        {
            "value": 60,
            "name": "Сёдзё-ай",
            "russian": "Сёдзё-ай",
        },
        {
            "value": 61,
            "name": "Сёнэн",
            "russian": "Сёнэн",
        },
        {
            "value": 62,
            "name": "Сёнэн-ай",
            "russian": "Сёнэн-ай",
        },
        {
            "value": 63,
            "name": "Спорт",
            "russian": "Спорт",
        },
        {
            "value": 87,
            "name": "Супер сила",
            "russian": "Супер сила",
        },
        {
            "value": 64,
            "name": "Сэйнэн",
            "russian": "Сэйнэн",
        },
        {
            "value": 65,
            "name": "Трагедия",
            "russian": "Трагедия",
        },
        {
            "value": 66,
            "name": "Триллер",
            "russian": "Триллер",
        },
        {
            "value": 67,
            "name": "Ужасы",
            "russian": "Ужасы",
        },
        {
            "value": 68,
            "name": "Фантастика",
            "russian": "Фантастика",
        },
        {
            "value": 69,
            "name": "Фэнтези",
            "russian": "Фэнтези",
        },
        {
            "value": 70,
            "name": "Школа",
            "russian": "Школа",
        },
        {
            "value": 71,
            "name": "Эротика",
            "russian": "Эротика",
        },
        {
            "value": 72,
            "name": "Этти",
            "russian": "Этти",
        },
        {
            "value": 73,
            "name": "Юри",
            "russian": "Юри",
        },
        {
            "value": 74,
            "name": "Яой",
            "russian": "Яой",
        },
    ]


__all__ = [
    "LibBaseItems",
]
