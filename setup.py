# setup.py

import sqlite3



# Create tables if not exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        release_year INTEGER,
        genre_id INTEGER,
        FOREIGN KEY (genre_id) REFERENCES genre(id)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS genre (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
''')

# Sample data for testing
cursor.execute("INSERT INTO genre (name) VALUES ('Action')")
cursor.execute("INSERT INTO genre (name) VALUES ('Drama')")
cursor.execute("INSERT INTO movies (title, release_year, genre_id) VALUES ('Movie 1', 2020, 1)")
cursor.execute("INSERT INTO movies (title, release_year, genre_id) VALUES ('Movie 2', 2021, 2)")

conn.commit()