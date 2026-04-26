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

#db = pd.read_sql('SELECT name,city FROM employees WHERE salary > (SELECT AVG(salary) FROM employees)',conn)
# normal name = Frank select the frank row here it fetches the frank's city assign it to ci
#db = pd.read_sql('SELECT name,city FROM employees WHERE city = (SELECT city FROM employees WHERE name = "Frank")',conn)
# Find employees in the top 2 highest paid departments
# db = pd.read_sql("""
#     SELECT name, dept, salary
#     FROM employees
#     WHERE dept IN (
#         SELECT dept FROM employees
#         GROUP BY dept
#         ORDER BY AVG(salary) DESC
#         LIMIT 2
#     )
# """, conn)

#Subquery in SELECT (Calculated Column)
# db = pd.read_sql("""
#     SELECT name, salary,
#            (SELECT AVG(salary) FROM employees) AS company_avg
#     FROM employees
# """, conn)
#Subquery as a Table (FROM clause)
# First get dept averages, then filter from THAT result
db = pd.read_sql("""
    SELECT dept, avg_salary
    FROM (
        SELECT dept, AVG(salary) AS avg_salary
        FROM employees
        GROUP BY dept
    ) AS dept_summary
    WHERE avg_salary > 55000
""", conn)
#      dept  avg_salary
# 0      HR     70000.0
# 1 Finance     61000.0
#The inner query creates a temporary table called dept_summary — the outer query filters from it.

print(db)

#The 3 Places a Subquery Can Live
# -- 1. In WHERE → filter rows
# SELECT * FROM employees
# WHERE salary > (SELECT AVG(salary) FROM employees);
#
# -- 2. In SELECT → add a calculated column
# SELECT name, salary, (SELECT MAX(salary) FROM employees) AS max_sal
# FROM employees;
#
# -- 3. In FROM → use as a temporary table
# SELECT * FROM (SELECT name, salary FROM employees WHERE salary > 50000) AS rich
# WHERE rich.salary < 70000;