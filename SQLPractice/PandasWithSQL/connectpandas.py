import sqlite3
import pandas as pd

from SQLPractice.sqlpractice import cursor

conn = sqlite3.connect('pandas.db')

cursor = conn.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS employee(
            id      INTEGER PRIMARY KEY,
            name    TEXT,
            city    TEXT,
            salary  INTEGER,
            age     INTEGER)
    ''')


employees = [
    (1, 'Alice',   'Mumbai',  50000, 25),
    (2, 'Bob',     'Delhi',   60000, 32),
    (3, 'Charlie', 'Mumbai',  55000, 28),
    (4, 'Diana',   'Chennai', 70000, 35),
    (5, 'Eve',     'Delhi',   45000, 22),
    (6, 'Ruku',  'Hyderabad', 500000,24)
]

cursor.executemany('INSERT INTO employee VALUES(?,?,?,?,?)',employees)

db = pd.read_sql('SELECT * FROM employee',conn)

print(db[db['name']=='Alice'])

conn.close()