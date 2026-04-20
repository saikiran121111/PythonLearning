import sqlite3

conn = sqlite3.connect('create.db')

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS employees")
#Create table if it doesn't exists
cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees ( 
            id  INTEGER PRIMARY KEY,
            name    TEXT,
            city    TEXT,
            salary  INTEGER,
            age INTEGER)
               ''')

employees = [
    (1, 'Alice',   'Mumbai',  50000, 25),
    (2, 'Bob',     'Delhi',   60000, 32),
    (3, 'Charlie', 'Mumbai',  55000, 28),
    (4, 'Diana',   'Chennai', 70000, 35),
    (5, 'Eve',     'Delhi',   45000, 22),
    (6, 'Ruku',  'Hyderabad', 500000,24)
]

cursor.executemany("INSERT INTO employees VALUES (?,?,?,?,?)",employees)

cursor.execute("SELECT name, city FROM employees")

rows = cursor.fetchall()

for i in rows:
    print(i)

conn.commit()
conn.close()