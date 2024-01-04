import platformdirs

from nlightreader.consts.app import APP_NAME

TOKEN_PATH = f"{platformdirs.user_data_dir()}/{APP_NAME}/tokens"
