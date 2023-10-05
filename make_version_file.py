from nlightreader.consts import APP_VERSION, APP_NAME

import pyinstaller_versionfile

pyinstaller_versionfile.create_versionfile(
    output_file='pkg_res/version_info.txt',
    version=APP_VERSION,
    company_name='brandonzorn',
    file_description=f'{APP_NAME} - Manga Reader',
    internal_name=APP_NAME,
    legal_copyright='Copyright (c) 2022 brandonzorn',
    original_filename=f'{APP_NAME}.exe',
    product_name=APP_NAME,
)
