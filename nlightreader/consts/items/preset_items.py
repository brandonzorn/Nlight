from typing import ClassVar


class PresetKinds:
    MANGA: ClassVar = {
        "name": "Manga",
        "russian": "Манга",
    }
    OEL_MANGA: ClassVar = {
        "name": "OEL-manga",
        "russian": "OEL-манга",
    }
    RU_MANGA: ClassVar = {
        "name": "Rumanga",
        "russian": "Руманга",
    }
    MANHWA: ClassVar = {
        "name": "Manhwa",
        "russian": "Манхва",
    }
    MANHUA: ClassVar = {
        "name": "Manhua",
        "russian": "Маньхуа",
    }
    ONESHOT: ClassVar = {
        "name": "Oneshot",
        "russian": "Ваншот",
    }
    COMIC: ClassVar = {
        "name": "Comic",
        "russian": "Комикс",
    }
    WESTERN_COMIC: ClassVar = {
        "name": "Western comic",
        "russian": "Западный комикс",
    }
    RU_COMIC: ClassVar = {
        "name": "Rucomic",
        "russian": "Рукомикс",
    }
    INDONESIAN_COMIC: ClassVar = {
        "name": "Indonesian comic",
        "russian": "Индонезийский комикс",
    }
    DOUJIN: ClassVar = {
        "name": "doujin",
        "russian": "Додзинси",
    }
    OTHER: ClassVar = {
        "name": "Other",
        "russian": "Другое",
    }

    TV: ClassVar = {
        "name": "TV Series",
        "russian": "TV Сериал",
    }
    TV_13: ClassVar = {
        "name": "Short",
        "russian": "Короткие",
    }
    TV_24: ClassVar = {
        "name": "Medium",
        "russian": "Средние",
    }
    TV_48: ClassVar = {
        "name": "Long",
        "russian": "Длинные",
    }
    MOVIE: ClassVar = {
        "name": "Movie",
        "russian": "Фильм",
    }
    OVA: ClassVar = {
        "name": "OVA",
        "russian": "OVA",
    }
    ONA: ClassVar = {
        "name": "ONA",
        "russian": "ONA",
    }
    SPECIAL: ClassVar = {
        "name": "Special",
        "russian": "Спецвыпуск",
    }
    TV_SPECIAL: ClassVar = {
        "name": "TV Special",
        "russian": "TV Спецвыпуск",
    }
    MUSIC: ClassVar = {
        "name": "Clip",
        "russian": "Клип",
    }
    PV: ClassVar = {
        "name": "Promo clip",
        "russian": "Проморолик",
    }
    CM: ClassVar = {
        "name": "Advertising",
        "russian": "Реклама",
    }


class PresetOrders:
    ID: ClassVar = {
        "name": "By ID",
        "russian": "По ID",
    }
    NAME: ClassVar = {
        "name": "By name",
        "russian": "По названию",
    }
    RUS_NAME: ClassVar = {
        "name": "By name",
        "russian": "По названию на русском",
    }
    POPULARITY: ClassVar = {
        "name": "By popularity",
        "russian": "По популярности",
    }
    LIKES_NUM: ClassVar = {
        "name": "By likes",
        "russian": "По лайкам",
    }
    VIEWS: ClassVar = {
        "name": "By views",
        "russian": "По просмотрам",
    }
    STATUS: ClassVar = {
        "name": "By status",
        "russian": "По статусу",
    }
    RATING: ClassVar = {
        "name": "By rating",
        "russian": "По рейтингу",
    }
    RANDOM: ClassVar = {
        "name": "By random",
        "russian": "Мне повезет",
    }

    UPDATED: ClassVar = {
        "name": "By update date",
        "russian": "По дате обновления",
    }
    CREATED: ClassVar = {
        "name": "By date added",
        "russian": "По дате добавления",
    }
    AIRED_ON: ClassVar = {
        "name": "By release date",
        "russian": "По дате выхода",
    }

    CHAPTERS_COUNT: ClassVar = {
        "name": "By number of chapters",
        "russian": "По количеству глав",
    }
    EPISODES_COUNT: ClassVar = {
        "name": "By number of episodes",
        "russian": "По количеству эпизодов",
    }
    VOLUMES_COUNT: ClassVar = {
        "name": "By number of volumes",
        "russian": "По количеству томов",
    }
    RATE_COUNT: ClassVar = {
        "name": "By number of ratings",
        "russian": "По количеству оценок",
    }

    TRANSLATION_VOLUME: ClassVar = {
        "name": "By volume of translation",
        "russian": "По объему перевода",
    }


__all__ = [
    "PresetKinds",
    "PresetOrders",
]
