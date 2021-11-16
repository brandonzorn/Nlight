import requests
import sqlite3
import os

HEADERS = {'User-Agent': 'Desu'}


def get_html(url: str, params=None):
    try:
        return requests.get(url, headers=HEADERS, params=params)
    except Exception as e:
        print(e)
        return None


def manga_add(data: dict):
    wd = os.getcwd()
    con = sqlite3.connect(f'{wd}/Desu/data.db')
    cur = con.cursor()
    a = cur.execute(f"SELECT favorites FROM manga WHERE id = {data.get('id')}").fetchall()
    if a and a[0][0]:
        a = True
    else:
        a = None
    cur.execute("INSERT INTO manga VALUES(?, ?, ?, ?, ?, ?, ?);",
                (data.get('id'), data.get('name'), data.get('russian'),
                 data.get('kind'), data.get('description'), a, data.get('score')))
    con.commit()
    con.close()


def chapters_add(data: dict, manga_id: int, index: int):
    wd = os.getcwd()
    con = sqlite3.connect(f'{wd}/Desu/data.db')
    cur = con.cursor()
    cur.execute("INSERT INTO chapters VALUES(?, ?, ?, ?, ?, ?);",
                (data.get('id'), data.get('vol'), data.get('ch'), data.get('title'), manga_id, index))
    con.commit()
    con.close()


def chapters_get(manga_id: int) -> list:
    wd = os.getcwd()
    con = sqlite3.connect(f'{wd}/Desu/data.db')
    cur = con.cursor()
    a = cur.execute(f"SELECT * FROM chapters WHERE manga_id = {manga_id} ORDER by index_n").fetchall()
    con.commit()
    con.close()
    return [{'id': i[0], 'vol': i[1], 'ch': i[2], 'title': i[3]} for i in a[::-1]]


def images_add(data: dict, chapter_id: int, index: int):
    wd = os.getcwd()
    con = sqlite3.connect(f'{wd}/Desu/data.db')
    cur = con.cursor()
    cur.execute("INSERT INTO images VALUES(?, ?, ?, ?, ?, ?, ?);",
                (data.get('id'), data.get('page'), data.get('width'),
                 data.get('height'), data.get('img'), chapter_id, index))
    con.commit()
    con.close()


def images_get(chapter_id: int) -> list:
    wd = os.getcwd()
    con = sqlite3.connect(f'{wd}/Desu/data.db')
    cur = con.cursor()
    a = cur.execute(f"SELECT * FROM images WHERE chapter_id = {chapter_id} ORDER by index_n").fetchall()
    con.commit()
    con.close()
    return [{'id': i[0], 'page': i[1], 'width': i[2], 'height': i[3], 'img': i[4]} for i in a]


def manga_favorites_add(manga_id: int):
    wd = os.getcwd()
    con = sqlite3.connect(f'{wd}/Desu/data.db')
    cur = con.cursor()
    cur.execute(f"UPDATE manga SET favorites = True WHERE id = {manga_id};")
    con.commit()
    con.close()


def manga_favorites_get():
    wd = os.getcwd()
    con = sqlite3.connect(f'{wd}/Desu/data.db')
    cur = con.cursor()
    a = cur.execute(f"SELECT * FROM manga WHERE favorites not Null;").fetchall()
    con.commit()
    con.close()
    return [{'id': i[0], 'name': i[1], 'russian': i[2], 'kind': i[3],
             'description': i[4], 'score': i[6]} for i in a[::-1]]


def manga_favorites_check(manga_id: int) -> bool:
    wd = os.getcwd()
    con = sqlite3.connect(f'{wd}/Desu/data.db')
    cur = con.cursor()
    a = cur.execute(f"SELECT favorites FROM manga WHERE id = {manga_id};").fetchall()
    con.commit()
    con.close()
    if a and a[0][0]:
        return True
    return False


def manga_favorites_rem(manga_id: int):
    wd = os.getcwd()
    con = sqlite3.connect(f'{wd}/Desu/data.db')
    cur = con.cursor()
    cur.execute(f"UPDATE manga SET favorites = Null WHERE id = {manga_id};")
    con.commit()
    con.close()
