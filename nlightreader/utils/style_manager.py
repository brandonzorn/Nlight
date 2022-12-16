class StyleManager:
    @staticmethod
    def get_dark_style():
        style = open("data/styles/dark/widget_dark.qss").read()
        return style
