#GroupBy is nothing but if we have multiple same values we group them and find the avg of them sum mean min max etc
#finding min max mean avg etc called as aggergation
import sqlite3

import pandas as pd

conn = sqlite3.connect('lesson3.db')
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS employees")
cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
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

#Aggregating Functions without grouping
# db = pd.read_sql("""
#     SELECT COUNT(*) AS total,
#            AVG(salary) AS avg_sal,
#            MAX(salary) AS max_sal,
#            MIN(salary) AS min_sal
#     FROM employees
# """, conn)
#Any column in SELECT that is NOT inside an aggregate function MUST be in GROUP BY.
# Here dept is not in Agg function so added in groupby
# -- ❌ wrong — name is not in GROUP BY or aggregate
# SELECT name, dept, AVG(salary) FROM employees GROUP BY dept;
db = pd.read_sql('SELECT dept,AVG(salary) AS avg_salary FROM employees GROUP BY dept',conn)


print(db)


db = pd.read_sql('SELECT dept,AVG(salary) AS avg_salary FROM employees GROUP BY dept ORDER BY avg_salary DESC',conn)
print(db)

#Having is used for filtering after Grouping
#It does something like WHERE but after groupBY

db = pd.read_sql('SELECT dept,AVG(salary) AS avg_salary FROM employees GROUP BY dept HAVING avg_salary>50000',conn)
print(db)


# -- WHERE filters BEFORE grouping (filters individual rows)
# SELECT dept, AVG(salary) FROM employees
# WHERE age > 25                   -- ← removes young employees first
# GROUP BY dept;
#
# -- HAVING filters AFTER grouping (filters entire groups)
# SELECT dept, AVG(salary) FROM employees
# GROUP BY dept
# HAVING AVG(salary) > 55000;     -- ← removes low-salary departments


# SELECT   dept, AVG(salary)   -- 1. what to show
# FROM     employees           -- 2. which table
# WHERE    age > 25            -- 3. filter rows first
# GROUP BY dept                -- 4. group remaining rows
# HAVING   AVG(salary) > 50000 -- 5. filter groups
# ORDER BY AVG(salary) DESC    -- 6. sort result