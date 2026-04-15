import pandas as pd

df = pd.read_csv('Book1.csv')

print(df.head())
print('###################################')
print(df.info())
print('###################################')
print(df.describe())
# df = pd.read_csv('students.csv', usecols=['Name', 'Marks', 'City'])
# df = pd.read_csv('students.csv', nrows=5)
# df = pd.read_csv('students.csv', sep=';')
# Another ways to read