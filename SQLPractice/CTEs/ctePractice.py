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


# Q1 — Using a CTE, find employees who earn LESS than
#       their department's average salary
# Expected output:
#     name     dept  salary     dept_avg
# 0    Bob       HR   60000      70000.0
# 1  Alice       IT   50000      50000.0  ← equal, not less
# 2    Eve       IT   45000      50000.0
# (only Bob and Eve are strictly below dept avg)


db = pd.read_sql('''
    
    WITH salary_val AS 
    (SELECT name,dept,salary,AVG(salary) OVER(PARTITION BY dept) AS dept_avg FROM employees)

    SELECT name,dept,salary,dept_avg FROM salary_val
    WHERE salary < dept_avg
''',conn)

print(db)


# Q2 — Using a CTE + window function, show each employee's
#       salary rank within their dept (DENSE_RANK)
# Expected output:
#       name     dept  salary  dept_rank
# 0    Diana  Finance   70000          1
# 1    Frank       HR   80000          1
# 2      Bob       HR   60000          2
# 3  Charlie       IT   55000          1
# 4    Alice       IT   50000          2
# 5      Eve       IT   45000          3


#Don't forget the space after AS

db = pd.read_sql('''
    WITH ranking AS
    (SELECT name,dept,salary,dense_rank() over (PARTITION BY dept ORDER BY salary DESC) AS dept_rank FROM employees)
    SELECT * FROM ranking
    
''',conn)

print()
print(db)


# Q3 — Using TWO CTEs, show each dept's
#       average salary AND total salary in same row
# Expected output:
#       dept    avg_sal  total_sal
# 0  Finance  70000.000      70000
# 1       HR  70000.000     140000
# 2       IT  50000.000     150000

db = pd.read_sql('''
    
    WITH average AS (
    SELECT dept,AVG(salary) AS avg_sal FROM employees GROUP BY dept),
    totalsum AS (
    SELECT dept,SUM(salary) AS total_sal FROM employees GROUP BY dept)

    SELECT a.dept,a.avg_sal,t.total_sal FROM average a INNER JOIN totalsum t ON a.dept = t.dept

''',conn)

print()
print(db)