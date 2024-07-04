import platformdirs

from nlightreader.consts.app import APP_NAME

TOKEN_PATH = platformdirs.user_data_path() / APP_NAME / "tokens"
