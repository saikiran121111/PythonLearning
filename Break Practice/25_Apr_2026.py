# 1. Create a list of 5 numbers, print only even ones using a loop

list1 = [1,2,3,4,5]
list2 = []

for i in list1:
    if i%2 == 0:
        list2.append(i)

print(list2)

# 2. Write a function that takes a name and age,
#    returns "Alice is 25 years old"

def person(name,age):

    return f'{name} is {age} years old'

print(person('Alice',25))

# 3. Create a dictionary of 3 students with their marks,
#    print only students who scored above 80

dict1 = {
    'rahim':55,
    'sanjay':65,
    'Ruku':99
}

for i in dict1:
    if dict1[i] > 80:
        print(i)

# Q4 — List comprehension: squares of 1 to 10
# Expected output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

numbers = list(range(1,11))
numbers1 = []
for i in numbers:
    numbers1.append(i**2)

print(numbers1)


#Numpy

import numpy as np

arr = np.array([10,20,30,40,50])

# Q5 — Multiply every element by 2
# Expected output: [20 40 60 80 100]

print(arr*2)

# Q6 — Filter elements greater than 25
# Expected output: [30 40 50]

print(arr[(arr>25)])

# Q7 — Create a 3x3 matrix of zeros
# Expected output:
# [[0. 0. 0.]
#  [0. 0. 0.]
#  [0. 0. 0.]]

arr = np.zeros([3,3])
print(arr)

# Q8 — Find mean, max, min of arr
# Expected output:
# Mean: 30.0  Max: 50  Min: 10

arr = np.array([10,20,30,40,50])

print(f'Mean : {np.mean(arr)}')
print(f'Max : {np.max(arr)}')
print(f'Min : {np.min(arr)}')


###################Pandas##########################

import pandas as pd
data = {
    'Name':   ['Ruku', 'Sai', 'Kiran', 'Arjun', 'Meera'],
    'Dept':   ['IT', 'HR', 'IT', 'Finance', 'HR'],
    'Salary': [70000, 50000, 65000, 80000, 55000],
    'Age':    [25, None, 28, 35, None]
}

df = pd.DataFrame(data)

# Q9 — Print shape and column names
# Expected output:
# (5, 4)
# Index(['Name', 'Dept', 'Salary', 'Age'], dtype='object')

print(df.shape)
print(df.columns)


# Q10 — Fill missing Age with mean
# Mean of [25, 28, 35] = 29.33
# Expected output: Sai → 29.33, Meera → 29.33

df['Age'] = df['Age'].fillna(df['Age'].mean())

# Q11 — Add column 'Level'
# Expected output:
#     Name     Dept  Salary    Age    Level
# 0   Ruku       IT   70000   25.0   Senior
# 1    Sai       HR   50000  29.33   Junior
# 2  Kiran       IT   65000   28.0   Junior
# 3  Arjun  Finance   80000   35.0   Senior
# 4  Meera       HR   55000  29.33   Junior
df['Level'] = df['Salary'].apply(lambda x : 'Senior' if x > 65000 else 'Junior')


# Q12 — Filter IT department only
# Expected output:
#     Name Dept  Salary   Age   Level
# 0   Ruku   IT   70000  25.0  Senior
# 2  Kiran   IT   65000  28.0  Junior
print()
print(df[(df['Dept'] == 'IT')])
print()

print(df.groupby('Dept')['Salary'].mean())

print()
print(df)


##SQLLLLLLLL


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

cursor.execute("DROP TABLE IF EXISTS departments")
cursor.execute('''CREATE TABLE departments(
    dept_id INTEGER, dept_name TEXT, location TEXT)''')
cursor.executemany("INSERT INTO departments VALUES(?,?,?)",[
    (1, 'IT', 'Mumbai'),
    (2, 'HR', 'Delhi'),
    (3, 'Finance', 'Chennai'),
    (4, 'Marketing', 'Bangalore')   # ← no employees here
])
conn.commit()

conn.commit()
print()
db = pd.read_sql('SELECT name,city FROM employees WHERE dept = "IT"',conn)
db = pd.read_sql('SELECT name,city FROM employees WHERE city IN ("Mumbai","Chennai") ORDER BY name ASC',conn)
print(db)

#3. Show employees whose name ends with 'e'

db = pd.read_sql('SELECT name,city FROM employees WHERE name LIKE "%e" ',conn)
print(db)

#GroupBY vs HAVING

#1. Show total salary spent per department

df = pd.read_sql('SELECT dept,SUM(salary) AS dept_salary FROM employees GROUP BY dept',conn)

print(df)

#2. Show only cities that have more than 1 employee
#   (hint: GROUP BY city, HAVING COUNT > 1)

df = pd.read_sql('SELECT city,COUNT(*) AS total_Count FROM employees GROUP BY city HAVING COUNT(*) > 1',conn)
print(df.head())

#3. Show each department's highest and lowest salary
#   in the same row
#   (hint: SELECT dept, MAX(...), MIN(...))

db = pd.read_sql('SELECT dept,MAX(salary) AS max_salary,MIN(salary) AS min_salary FROM employees GROUP BY dept ',conn)
print(db)

#SUBQUERIES
#1. Find employees whose salary is LESS than the average salary

db = pd.read_sql('SELECT name,salary FROM employees WHERE salary < (SELECT AVG(salary) FROM employees)',conn)

print(db)

# Q2 — Find employees who work in the same city as 'Frank'
# (Frank is in Hyderabad)
# Expected output:
#     name       city
# 0  Frank  Hyderabad

db = pd.read_sql('SELECT name,city FROM employees WHERE city = (SELECT city FROM employees WHERE name = "Frank")',conn)
print(db)

# Q3 — Find the department with the HIGHEST average salary
# avg per dept: Finance=70000, HR=70000, IT=50000
# Expected output:
#       dept  avg_salary
# 0  Finance     70000.0
# 1       HR     70000.0
# (both Finance and HR tie at 70000 — both should appear)

db = pd.read_sql('SELECT dept,avg_sal FROM (SELECT dept,AVG(salary) AS avg_sal FROM employees GROUP BY dept) WHERE avg_sal > 60000',conn)
print()
print(db)


#JOINNN #######################################

# Q1 — INNER JOIN: show each employee's name, salary and dept location
# Expected output:
#       name  salary location
# 0    Alice   50000   Mumbai
# 1      Bob   60000    Delhi
# 2  Charlie   55000   Mumbai
# 3    Diana   70000  Chennai
# 4      Eve   45000   Mumbai
# 5    Frank   80000    Delhi

db = pd.read_sql('SELECT e.name,e.salary,d.location FROM employees e INNER JOIN departments d WHERE e.dept = d.dept_name',conn)

print()
print(db)


# Q2 — LEFT JOIN: show ALL departments and count of employees in each
# (departments with 0 employees should show 0, not disappear)
# Expected output:
#    dept_name  employee_count
# 0    Finance               1
# 1         HR               2
# 2         IT               3
# 3  Marketing               0

db = pd.read_sql('SELECT d.dept_name, COUNT(e.name) AS emp_count FROM employees e RIGHT JOIN departments d ON e.dept = d.dept_name GROUP BY d.dept_name',conn)

print()
print(db)



# Q3 — INNER JOIN + WHERE: show only employees in dept located in 'Mumbai'
# Expected output:
#       name  salary dept_name
# 0    Alice   50000        IT
# 1  Charlie   55000        IT
# 2      Eve   45000        IT

db = pd.read_sql('''
        SELECT e.name,e.salary,d.dept_name
        FROM employees e
        INNER JOIN departments d
        ON e.dept = d.dept_name
        WHERE d.dept_name = 'IT'
        ''',conn)

print(db)