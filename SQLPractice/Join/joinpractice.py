import pandas as pd
import sqlite3


conn = sqlite3.connect('lesson4.db')
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS employees")
cursor.execute("DROP TABLE IF EXISTS departments")

cursor.execute('''CREATE TABLE employees (
    id INTEGER PRIMARY KEY, name TEXT,
    dept_id INTEGER, salary INTEGER)''')

cursor.execute('''CREATE TABLE departments (
    id INTEGER PRIMARY KEY,
    dept_name TEXT, location TEXT)''')

employees = [
    (1, 'Alice',  1, 50000),
    (2, 'Bob',    2, 60000),
    (3, 'Charlie',1, 55000),
    (4, 'Diana',  3, 70000),
    (5, 'Eve',    2, 45000),
    (6, 'Frank',  None, 80000)   # ← no department assigned!
]

departments = [
    (1, 'IT',      'Mumbai'),
    (2, 'HR',      'Delhi'),
    (3, 'Finance', 'Chennai'),
    (4, 'Marketing', 'Pune')     # ← no employees here!
]

cursor.executemany("INSERT INTO employees VALUES(?,?,?,?)", employees)
cursor.executemany("INSERT INTO departments VALUES(?,?,?)", departments)

#1 Inner join checks the condition and joins the same values if null IT doesn't gonna print
#db = pd.read_sql('SELECT e.name,e.salary,d.dept_name,d.location FROM employees e INNER JOIN departments d ON e.dept_ID=d.id',conn)

#2 Left Join all from left matches from right that means all left values will come even left table row doesn't have right connection

#db = pd.read_sql('SELECT e.name,e.salary,d.dept_name,d.location FROM employees e LEFT JOIN departments d ON e.dept_ID=d.id',conn)


#3 Right join matches the right values to left here right table has market which is not assigned to anyone

db = pd.read_sql('SELECT e.name,e.salary,d.dept_name,d.location FROM employees e RIGHT JOIN departments d ON e.dept_ID=d.id',conn)
print(db)