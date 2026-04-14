from unittest.mock import inplace

import pandas as pd

data = {
    'Name':   ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'City':   ['Mumbai', 'Delhi', 'Mumbai', 'Chennai', 'Delhi'],
    'Salary': [50000, 60000, 55000, 70000, 45000],
    'Age':    [25, 32, 28, 35, 22]
}
df = pd.DataFrame(data)

df['Country'] = 'India' # Adding new Columns
df['Tax'] = df['Salary'] // 1.5 # Adding new Columns
# Can do multiple Add or anything the same way as adding things in dictionary

#Modifying Existing Column
df['Salary'] = df['Salary'] * 2.8 # Modified the existing Column


#Renaming Column

df = df.rename(columns={'Salary':'AnnualSalary'}) # Renaming the Key
df = df.rename(columns={'Age':'Year','Name':'FullName'})

#Dropping Columns

df = df.drop(columns=['Tax','Country']) # This will remove the columns
#There is other way instead of assigning inplace can also be used

df.drop(columns=['Year'],inplace=True)

#Dropping Rows

df.drop(index=2,inplace=True) # This will remove the row 2 that is charlie
# df = df.drop(index=[0, 2]) # To remove multiple rows
print(df)
print()
# apply() Do anything to the column

def salary_label(salary):
    if salary > 55000*2.8:
        return 'High'
    else:
        return 'Low'

df['level'] = df['AnnualSalary'].apply(salary_label)


#We can use this apply to do anything
# Other way is to we can use lambda function

df['Authority'] = df['AnnualSalary'].apply(lambda x : 'Manager' if x>55000*2.8 else 'Slave')
print(df[['FullName','AnnualSalary','City','level','Authority']])


