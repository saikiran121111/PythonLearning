import pandas as pd

data = {
    'Name':   ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'City':   ['Mumbai', 'Delhi', 'Mumbai', 'Chennai', 'Delhi'],
    'Salary': [50000, 60000, 55000, 70000, 45000],
    'Age':    [25, 32, 28, 35, 22]
}
df = pd.DataFrame(data)

print(df[(df['Salary']>50000) & (df['Age']<33) ])

#LOC ILOC Impppp

#These are the two main ways to access rows and columns precisely.
#LOC is mostly by key name

print(df.loc[(df['City']== 'Mumbai')])

print(df.loc[(df['Salary']>55000),['Name','Age']]) # Prints the specified rows with condition


# ILOC is mostly by index list index

print(df.iloc[0:2,0:2]) # rows columns

#loc  → use when you know the NAME  (column name, condition)
#iloc → use when you know the NUMBER (row 0, column 1)


#isin()

# This filters list via values

print(df[df['City'].isin(['Mumbai','Delhi'])])