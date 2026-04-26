import sqlite3
import pandas as pd

conn = sqlite3.connect('lesson5.db')
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS employees")
cursor.execute('''CREATE TABLE employees (
    id INTEGER PRIMARY KEY, name TEXT, city TEXT,
    dept TEXT, salary INTEGER, age INTEGER)''')

employees = [
    (1,'Alice','Mumbai','IT',50000,25),
    (2,'Bob','Delhi','HR',60000,32),
    (3,'Charlie','Mumbai','IT',55000,28),
    (4,'Diana','Chennai','Finance',70000,35),
    (5,'Eve','Delhi','IT',45000,22),
    (6,'Frank','Hyderabad','HR',80000,40),
    (7,'Arjun','Mumbai','Finance',52000,29),
    (8,'Meera','Delhi','IT',48000,26)
]
cursor.executemany("INSERT INTO employees VALUES(?,?,?,?,?,?)", employees)
conn.commit()

# db = pd.read_sql('''
#         SELECT name,salary FROM employees
#         WHERE salary > (SELECT AVG(salary) FROM employees)
#         ''',conn)

# db = pd.read_sql('''
#     SELECT name,salary FROM employees
#     WHERE salary = (SELECT MAX(salary) FROM employees)
#     ''',conn)

# db = pd.read_sql('''SELECT name,
#                            salary,
#                            salary - (SELECT AVG(salary) FROM employees) AS diff_salary
#                     FROM employees''',conn)

# db = pd.read_sql('''
#         SELECT name,dept FROM employees
#         WHERE dept = (SELECT dept FROM employees WHERE name = 'Diana')''',conn)

db = pd.read_sql('''
    SELECT name, dept, salary
    FROM (
        SELECT name, dept, salary FROM employees WHERE dept = 'IT'
    ) AS it_employees
    WHERE salary > 50000
''', conn)
#You forgot this don't do that

print(db)