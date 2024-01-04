from PySide6.QtGui import QColor


class ItemsColors:
    READ = QColor("GREEN")
    UNREAD = QColor("RED")
    IN_LIBRARY = QColor("ORANGE")
    EMPTY = QColor(255, 255, 255, 0)


class StyleColors:
    DEFAULT_COLOR_BINDS = {
        "@scroll_bar_handle_hover": "rgba(114.000, 115.000, 115.000, 0.827)",
        "@scroll_bar_handle_pressed": "rgba(143.000, 145.000, 145.000, 0.933)",
    }
    DARK_COLOR_BINDS = {
        "@text_color": "#ffffff",
        "@window_background_color": "#202020",
        "@frame_background_color": "#2d2d2d",
        "@manga_item_frame_color": "#545656",
        "@manga_item_frame_active_color": "#727373",
        "@scroll_bar_color": "#292b2e",
        "@scroll_bar_handle_color": "rgba(84.000, 86.000, 86.000, 0.737)",
        "@button_border_color": "#ffffff",
        "@accent_color": "#008533",
    }

    LIGHT_COLOR_BINDS = {
        "@text_color": "#000000",
        "@window_background_color": "#ffffff",
        "@frame_background_color": "#e6e6e6",
        "@manga_item_frame_color": "#cccccc",
        "@manga_item_frame_active_color": "#7a7a7a",
        "@scroll_bar_color": "#e9e9e9",
        "@scroll_bar_handle_color": "#bababa",
        "@button_border_color": "#7a7a7a",
        "@accent_color": "#cccccc",
    }
