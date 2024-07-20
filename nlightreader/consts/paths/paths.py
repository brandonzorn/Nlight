import platformdirs

from nlightreader.consts.app import APP_NAME


APP_DATA_PATH = platformdirs.user_data_path() / APP_NAME
TOKEN_PATH = APP_DATA_PATH / "tokens"
