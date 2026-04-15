import pandas as pd
import numpy as np

data = {
    'Name':   ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Age':    [25, np.nan, 28, 35, np.nan],
    'Salary': [50000, 60000, np.nan, 70000, 45000],
    'City':   ['Mumbai', 'Delhi', np.nan, 'Chennai', 'Delhi']
}

df = pd.DataFrame(data)

def change_value():
    return 0
# This is the first thing we run on datasets
print(df.isnull().sum()) # Use this to count the no of missing values

# Becareful with Dropna you can loose alot of data

## Dropping the missing values
#This drops the whole row even if one value is nan
#df.dropna(inplace=True)

#This drops the row when all values are NaN
#df.dropna(how='all',inplace=True)

#This drops only on the specific column
#df.dropna(subset=['Salary'],inplace=True)

#Filling can be the best way instead of dropna

df['City'] = df['City'].fillna('Unknown') # This is how we fill the blank values for the respective columns for all Nan
df['Age'] = df['Age'].fillna(df['Age'].mean()) # Can do some validations for Nan
df['Salary'] = df['Salary'].fillna('Unknown')

print(df.isnull().sum())


print()
print(df)