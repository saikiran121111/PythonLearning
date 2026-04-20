import sqlite3


conn = sqlite3.connect('assignment.db')

cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS students')

cursor.execute('''
        
        CREATE TABLE IF NOT EXISTS students(
            id      INTEGER PRIMARY KEY,
            name    TEXT,
            subject TEXT,
            marks   INTEGER,
            grade   TEXT)
        ''')

students = [
    (1,'Ruku','Maths',99,'A+'),
    (2,'Sai','Maths',98,'A+'),
    (3,'Karim','Maths',1,'F+'),
    (4,'Rajiv','Maths',70,'B'),
    (5,'Sanjay','Maths',80,'A')
]

cursor.executemany("INSERT INTO students VALUES(?,?,?,?,?)",students)

cursor.execute("SELECT * FROM students")

print(cursor.fetchall())

cursor.execute('DROP TABLE IF EXISTS employees')

cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees(
            id      INTEGER PRIMARY KEY,
            name    TEXT,
            city    TEXT,
            salary  INTEGER,
            age     INTEGER
        
        )
        
        ''')

employees = [
    (1, 'Alice',   'Mumbai',  50000, 25),
    (2, 'Bob',     'Delhi',   60000, 32),
    (3, 'Charlie', 'Mumbai',  55000, 28),
    (4, 'Diana',   'Chennai', 70000, 35),
    (5, 'Eve',     'Delhi',   45000, 22),
    (6, 'Ruku',  'Hyderabad', 500000,24)
]

cursor.executemany("INSERT INTO employees VALUES(?,?,?,?,?)",employees)

cursor.execute('SELECT name,salary FROM employees')

print(cursor.fetchall())

cursor.execute('SELECT city FROM employees')
print(cursor.fetchall())

cursor.execute('SELECT * FROM employees')
print(cursor.fetchall())

cursor.execute('SELECT city AS location,name AS full_name FROM employees')
print(cursor.fetchall())

cursor.execute('SELECT DISTINCT city FROM employees')
print(cursor.fetchall())

cursor.execute('SELECT city FROM employees ORDER BY salary ASC')
print(cursor.fetchall())

cursor.execute('SELECT city FROM employees ORDER BY salary DESC')
print(cursor.fetchall())

conn.close()

