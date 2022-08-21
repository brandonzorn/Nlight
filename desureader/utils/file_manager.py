import os


def get_file(path, file_name):
    path = f'{os.getcwd()}/{path}/{file_name}'
    return path


def check_file_exists(path, file_name):
    return os.path.exists(f'{os.getcwd()}/{path}/{file_name}')


def save_file(path, file_name, file_content):
    path = f'{os.getcwd()}/{path}'
    if not os.path.exists(f'{path}/{file_name}'):
        os.makedirs(path, exist_ok=True)
        if file_content:
            with open(f'{path}/{file_name}', 'wb') as f:
                f.write(file_content.content)


def init_app_paths(paths: list[str]):
    for path in paths:
        path = f'{os.getcwd()}/{path}'
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)
