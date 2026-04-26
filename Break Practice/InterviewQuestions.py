# Q20 — The classic interview question:
# Find the TOP earner in EACH department
# using ROW_NUMBER() — show only row_num = 1

# Expected output:
#     name     dept  salary  row_num
# 0  Diana  Finance   70000        1
# 1  Frank       HR   80000        1
# 2  Charlie    IT   55000        1

# Hint: you need a subquery — window functions
# can't be used directly in WHERE clause!

# SELECT * FROM (
#     SELECT name, dept, salary,
#            ROW_NUMBER() OVER(...) AS row_num
#     FROM employees
# ) WHERE row_num = 1

import sqlite3,pandas as pd

conn = sqlite3.connect('sql_lessons.db')
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS employees")
cursor.execute('''CREATE TABLE employees(
    id INTEGER, name TEXT, dept TEXT,
    city TEXT, salary INTEGER)''')

cursor.executemany("INSERT INTO employees VALUES(?,?,?,?,?)",[
    (1,'Alice','IT','Mumbai',50000),
    (2,'Bob','HR','Delhi',60000),
    (3,'Charlie','IT','Mumbai',55000),
    (4,'Diana','Finance','Chennai',70000),
    (5,'Eve','IT','Delhi',45000),
    (6,'Frank','HR','Hyderabad',80000)
])

conn.commit()

db = pd.read_sql('''
        SELECT * FROM 
        (SELECT name,dept,salary, ROW_NUMBER() over (PARTITION BY dept ORDER BY salary DESC) AS row_num FROM employees) AS top_earner
        WHERE row_num=1
''',conn)

print(db)