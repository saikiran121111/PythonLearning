import pandas as pd

employees = [
  (1, 'Alice', 'IT', 'Mumbai', 50000),
  (2, 'Bob', 'HR', 'Delhi', 60000),
  (3, 'Charlie', 'IT', 'Mumbai', 55000),
  (4, 'Diana', 'Finance', 'Chennai', 70000),
  (5, 'Eve', 'IT', 'Delhi', 45000),
  (6, 'Frank', 'HR', 'Hyderabad', 80000)
]

for i in employees:
    if i[4] > 55000:
        print(i[1])


list1 = [i[1] for i in employees]
print(list1)

list2 = ['id', 'name', 'dept', 'city', 'salary']

df = pd.DataFrame(employees,columns=list2)

print(df[(df['dept']=='IT')])