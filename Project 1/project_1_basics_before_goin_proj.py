import pandas as pd

messy_employees = [
  (1, 'Alice', 'IT', 'Mumbai', '50000'),    # Salary is a string
  (2, 'Bob', 'HR', 'Delhi', 60000),
  (3, 'Charlie', 'IT', None, 55000),        # City is missing (None)
  (4, 'Diana', 'Finance', 'Chennai', '70000'), # Salary is a string
  (5, 'Eve', 'IT', 'Delhi', None),          # Salary is missing (None)
  (6, 'Frank', 'HR', 'Hyderabad', 80000)
]

columns = ['id', 'name', 'dept', 'city', 'salary']

df = pd.DataFrame(messy_employees,columns=columns)

df['salary']=df['salary'].fillna(0).astype(int)
df['city']=df['city'].fillna('Unknown')

print(df['dept'].value_counts())
max_salary = df['salary'].max()

print(df[(df['salary']== max_salary)])

print(df.sort_values('salary',ascending=False))