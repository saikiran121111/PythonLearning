import sqlite3
import pandas as pd

conn = sqlite3.connect('lesson2.db')
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS employees")
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id      INTEGER PRIMARY KEY,
        name    TEXT,
        city    TEXT,
        salary  INTEGER,
        age     INTEGER
    )
''')

employees = [
    (1, 'Alice',   'Mumbai',    50000, 25),
    (2, 'Bob',     'Delhi',     60000, 32),
    (3, 'Charlie', 'Mumbai',    55000, 28),
    (4, 'Diana',   'Chennai',   70000, 35),
    (5, 'Eve',     'Delhi',     45000, 22),
    (6, 'Frank',   'Hyderabad', 80000, 40),
    (7, 'Arjun',   'Mumbai',    52000, 29),
    (8, 'Meera',   'Delhi',     48000, 26)
]
cursor.executemany("INSERT INTO employees VALUES (?,?,?,?,?)", employees)


df = pd.read_sql("SELECT * FROM employees WHERE city = 'Mumbai' AND salary > 52000",conn)
print(df)
conn.commit()
conn.close()

#Range filter
#SELECT FROM TABLE_NAME WHERE col BETWEEN 50 AND 100; etc
# Instead of using OR multiple times
#SELECT * FROM employees WHERE city = 'Mumbai' OR city = 'Delhi' OR city = 'Chennai';
#USE IN
#SELECT * FROM employees WHERE city IN ('Mumbai', 'Delhi', 'Chennai');
#Exclude
#SELECT * FROM employees WHERE city NOT IN ('Mumbai', 'Delhi');

#-- Names starting with 'A'
#SELECT * FROM employees WHERE name LIKE 'A%';

#SELECT → FROM → WHERE → ORDER BY   -> Remember THis