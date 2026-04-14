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