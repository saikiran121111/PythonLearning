import sqlite3
import pandas as pd

#
#
# conn = sqlite3.connect('assignment.db')
#
# cursor = conn.cursor()
#
# cursor.execute('DROP TABLE IF EXISTS students')
#
# cursor.execute('''
#
#         CREATE TABLE IF NOT EXISTS students(
#             id      INTEGER PRIMARY KEY,
#             name    TEXT,
#             subject TEXT,
#             marks   INTEGER,
#             grade   TEXT)
#         ''')
#
# students = [
#     (1,'Ruku','Maths',99,'A+'),
#     (2,'Sai','Maths',98,'A+'),
#     (3,'Karim','Maths',1,'F+'),
#     (4,'Rajiv','Maths',70,'B'),
#     (5,'Sanjay','Maths',80,'A')
# ]
#
# cursor.executemany("INSERT INTO students VALUES(?,?,?,?,?)",students)
#
# cursor.execute("SELECT * FROM students")
#
# print(cursor.fetchall())
#
# cursor.execute('DROP TABLE IF EXISTS employees')
#
# cursor.execute('''
#         CREATE TABLE IF NOT EXISTS employees(
#             id      INTEGER PRIMARY KEY,
#             name    TEXT,
#             city    TEXT,
#             salary  INTEGER,
#             age     INTEGER
#
#         )
#
#         ''')
#
# employees = [
#     (1, 'Alice',   'Mumbai',  50000, 25),
#     (2, 'Bob',     'Delhi',   60000, 32),
#     (3, 'Charlie', 'Mumbai',  55000, 28),
#     (4, 'Diana',   'Chennai', 70000, 35),
#     (5, 'Eve',     'Delhi',   45000, 22),
#     (6, 'Ruku',  'Hyderabad', 500000,24)
# ]
#
# cursor.executemany("INSERT INTO employees VALUES(?,?,?,?,?)",employees)
#
# cursor.execute('SELECT name,salary FROM employees')
#
# print(cursor.fetchall())
#
# cursor.execute('SELECT city FROM employees')
# print(cursor.fetchall())
#
# cursor.execute('SELECT * FROM employees')
# print(cursor.fetchall())
#
# cursor.execute('SELECT city AS location,name AS full_name FROM employees')
# print(cursor.fetchall())
#
# cursor.execute('SELECT DISTINCT city FROM employees')
# print(cursor.fetchall())
#
# cursor.execute('SELECT city FROM employees ORDER BY salary ASC')
# print(cursor.fetchall())
#
# cursor.execute('SELECT city FROM employees ORDER BY salary DESC')
# print(cursor.fetchall())
#
# conn.close()
#


conn = sqlite3.connect('EmployeeDb.db')

cursor = conn.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS employee(
        id      INTEGER PRIMARY KEY,
        name    TEXT,
        city    TEXT,
        salary  INTEGER,
        age     INTEGER)''')

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

cursor.executemany("INSERT INTO employee VALUES(?,?,?,?,?)",employees)
#db = pd.read_sql('SELECT * FROM employee WHERE salary BETWEEN 50000 AND 70000',conn)
#db = pd.read_sql('SELECT * FROM employee WHERE city IN ("Mumbai","Chennai")',conn)
#db = pd.read_sql('SELECT * FROM employee WHERE name LIKE "A%"',conn)
#db = pd.read_sql('SELECT * FROM employee WHERE city NOT IN ("Delhi") AND salary ORDER BY salary DESC',conn)
#This is the right approach 'SELECT * FROM employee WHERE city NOT IN ("Delhi") ORDER BY salary DESC'
#db = pd.read_sql('SELECT * FROM employee WHERE age BETWEEN 25 AND 30',conn)
cursor.execute('UPDATE employee SET salary = 90000 WHERE name IN ("Frank")')
db = pd.read_sql('SELECT * FROM employee',conn)
print(db)
conn.close()