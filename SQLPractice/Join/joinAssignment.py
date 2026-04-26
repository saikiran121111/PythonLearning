import pandas as pd
import sqlite3

conn = sqlite3.connect('joinAssignment.db')
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
conn.commit()


#db = pd.read_sql('SELECT e.name,e.salary,d.dept_name FROM employees e INNER JOIN departments d ON e.dept_id = d.id',conn)
#db = pd.read_sql('SELECT e.name,e.salary,d.dept_name FROM employees e LEFT JOIN departments d ON e.dept_id = d.id',conn)
#db = pd.read_sql('SELECT e.name,e.salary,d.dept_name FROM employees e RIGHT JOIN departments d ON e.dept_id = d.id',conn)
#db = pd.read_sql('SELECT e.name,e.salary,d.dept_name FROM employees e INNER JOIN departments d ON e.dept_id = d.id WHERE dept_name = "HR"',conn)
db = pd.read_sql('SELECT d.dept_name,SUM(e.salary) AS total_salary FROM employees e INNER JOIN departments d ON e.dept_id = d.id GROUP BY d.dept_name ORDER BY total_salary DESC',conn)
print(db) 