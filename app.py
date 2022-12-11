import sqlite3


def create_bd():
    connection = sqlite3.connect('db.db')
    cursor = connection.cursor()
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS DB
        (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT,
        url TEXT,
        xpath Text)
        '''
    )

    connection.commit()
    connection.close()


if __name__ == '__main__':
    create_bd()
