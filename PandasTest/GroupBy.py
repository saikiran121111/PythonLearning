import pandas as pd

data = {
    'Name':   ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank'],
    'City':   ['Mumbai', 'Delhi', 'Mumbai', 'Chennai', 'Delhi', 'Mumbai'],
    'Dept':   ['IT', 'HR', 'IT', 'Finance', 'IT', 'HR'],
    'Salary': [50000, 60000, 55000, 70000, 45000, 52000],
    'Age':    [25, 32, 28, 35, 22, 29]
}
df = pd.DataFrame(data)
# Average salary per city
print(df.groupby('City')['Salary'].mean())

# Count of employees per city
print(df.groupby('City')['Name'].count())

#Pattern is always
# df.groupby('GROUP_BY_THIS_COLUMN')['TARGET_COLUMN'].aggregation() # for single aggregation

#Multiple Aggregations
#agg() is how you get multiple stats in a single call — use it instead of calling .mean() and .max() separately.
print(df.groupby('City')['Salary'].agg(['mean','min','max'])) # calls multiple aggregations atonce


#Group By multiple Columns

print(df.groupby(['City','Dept'])['Salary'].mean()) # Just pass a list in groupby

# After groupby, the group column becomes the index which looks messy.

print()
print(df.groupby('City')['Salary'].mean().reset_index()) # becomes new index which fixes the messed up indexes

#Sorting Results it sorts the values in order

result = df.groupby('City')['Salary'].mean().reset_index()

result = result.sort_values('Salary',ascending=False)
