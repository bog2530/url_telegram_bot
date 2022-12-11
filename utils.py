import sqlite3
import logging
import os
import time

import pandas
from numpy import nan


def download_file(file, user):
    os.makedirs('media', exist_ok=True)
    unix_time = int(time.time())
    file_name = os.path.join('media', f'{user}_{unix_time}.xlsx')
    file.download(file_name)
    return file_name


def open_file(file_name):
    try:
        excel_data = pandas.read_excel(
            file_name,
            usecols=['Name', 'URL', 'Xpath'],
        )
    except ValueError:
        return 0
    url_list = excel_data.to_dict(orient='records', )
    if not url_list:
        return -1
    for url in url_list:
        if nan in url.values():
            return -2

    return excel_data.to_dict(orient='records',)


def save_db(records):
    try:
        sqlite_connection = sqlite3.connect('db.db')
        cursor = sqlite_connection.cursor()
        query = '''
        INSERT INTO DB
        (name, url, xpath)
        VALUES (:Name, :URL, :Xpath);
        '''

        cursor.executemany(query, records)
        sqlite_connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        logging.error(error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
