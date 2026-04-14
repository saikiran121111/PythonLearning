import pandas as pd
data = {
    'Name' : ['Alice','Bob','Charlie','Diana'],
    'City' : ['Mumbai','Delhi','Hyderabad','Chennai'],
    'Salary' : [50000,60000,55000,70000]
}
df = pd.DataFrame(data)
print(df)

print(df.shape)
print(df[['Name','Salary']])
print(df.info())


#################################################################

data = {
    'Name':   ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'City':   ['Mumbai', 'Delhi', 'Mumbai', 'Chennai', 'Delhi'],
    'Salary': [50000, 60000, 55000, 70000, 45000],
    'Age':    [25, 32, 28, 35, 22]
}
df = pd.DataFrame(data)

print(df[df['Age']>25])
print()
print(df[(df['City'] == 'Delhi') & (df['Salary']>50000)])
print()
print(df.loc[df['Salary']>52000,['Name','Age']])
print()
print(df.iloc[3:5,0:2])
print()
print(df[df['City'].isin(['Mumbai','Chennai'])])

print()
print('###################################################################################')
#############################################################################

data = {
    'Name':     ['Ruku', 'Sai', 'Kiran', 'Arjun'],
    'Score':    [72, 85, 60, 91],
    'Attempts': [3, 2, 4, 1]
}
df = pd.DataFrame(data)

df['Passed'] = df['Score'].apply(lambda x :True if x >=65 else False)

def validate_grade(grade):
    if grade >=85:
        return 'A'
    elif grade >=70:
        return 'B'
    else:
        return 'C'

df['Grade'] = df['Score'].apply(validate_grade)

df.rename(columns={'Attempts':'Tries'},inplace=True)
df.drop(columns=['Passed'],inplace=True)
print(df)