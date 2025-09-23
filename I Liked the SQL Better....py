"""
Create an SQLite3 database /tmp/movies.db

Your database should have a table named MOVIES that contains the following data:

Name	Year	Rating
Rise of the Planet of the Apes	2011	77
Dawn of the Planet of the Apes	2014	91
Alien	1979	97
Aliens	1986	98
Mad Max	1979	95
Mad Max 2: The Road Warrior	1981	100
In Haskell, both of the persistent and esqueleto modules are available...

You will be expected to create a monadic action mkMoviesDB :: IO ()
"""

# Create a database /tmp/movies.db using SQLite3
# Create a table in it called "MOVIES"
# Insert data

import sqlite3

conn = sqlite3.connect('/tmp/movies.db')

cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS MOVIES (
              id INTEGER PRIMARY KEY,
              name TEXT NOT NULL,
              year INTEGER NOT NULL,
              rating INTEGER NOT NULL) """)

mv = [
    ("Rise of the Planet of the Apes", 2011, 77),
    ("Dawn of the Planet of the Apes", 2014, 91),
    ("Alien", 1979, 97),
    ("Aliens", 1986, 98),
    ("Mad Max", 1979, 95),
    ("Mad Max 2: The Road Warrior", 1981, 100)
]

cursor.executemany("INSERT INTO MOVIES (name, year, rating) VALUES (?,?,?)", mv)

conn.commit()