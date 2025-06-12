from nlightreader.consts.items.parser_items import (
    ParserItems,
)


class MangaDexItems(ParserItems):
    ORDERS = [
        {
            "value": "relevance",
            "name": "Best Match",
            "russian": "",
        },
        {
            "value": "latestUploadedChapter",
            "name": "Latest Upload",
            "russian": "",
        },
        {
            "value": "title",
            "name": "Title Descending",
            "russian": "",
        },
        {
            "value": "rating",
            "name": "Highest Rating",
            "russian": "",
        },
        {
            "value": "followedCount",
            "name": "Most Follows",
            "russian": "",
        },
        {
            "value": "createdAt",
            "name": "Recently Added",
            "russian": "",
        },
        {
            "value": "year",
            "name": "Year Descending",
            "russian": "",
        },
    ]


__all__ = [
    "MangaDexItems",
]
