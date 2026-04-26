# Q1 — Show each employee's name, salary and the
#       MAXIMUM salary in their department
# Expected output:
#       name     dept  salary  dept_max
# 0    Alice       IT   50000     55000
# 1      Bob       HR   60000     80000
# 2  Charlie       IT   55000     55000
# 3    Diana  Finance   70000     70000
# 4      Eve       IT   45000     55000
# 5    Frank       HR   80000     80000


import sqlite3,pandas as pd

conn = sqlite3.connect('windowFunctions.db')
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



db = pd.read_sql('SELECT name,dept,salary,MAX(salary) OVER(PARTITION BY dept) AS dept_max FROM employees ORDER BY name ASC',conn)
print(db)


# Q2 — Rank ALL employees by salary (no partition, whole company)
#       using DENSE_RANK, highest salary = rank 1
# Expected output:
#       name  salary  rank
# 0    Frank   80000     1
# 1    Diana   70000     2
# 2      Bob   60000     3
# 3  Charlie   55000     4
# 4    Alice   50000     5
# 5      Eve   45000     6
print()
db = pd.read_sql('SELECT name,salary,dense_rank() over (ORDER BY salary DESC) AS rank FROM employees',conn)
print(db)



# Q3 — Show each employee's salary AND how much
#       MORE or LESS they earn vs their dept average
# Expected output:
#       name     dept  salary  dept_avg  diff
# 0    Alice       IT   50000   50000.0   0.0
# 1      Bob       HR   60000   70000.0 -10000.0
# 2  Charlie       IT   55000   50000.0  5000.0
# 3    Diana  Finance   70000   70000.0   0.0
# 4      Eve       IT   45000   50000.0 -5000.0
# 5    Frank       HR   80000   70000.0  10000.0
# hint: salary - AVG(salary) OVER(PARTITION BY dept)

print()
db = pd.read_sql('SELECT name,dept,salary,AVG(salary) OVER(PARTITION BY dept) AS dept_avg,salary-AVG(salary) OVER(PARTITION BY dept) AS diff FROM employees ORDER BY name ASC',conn)

print(db)