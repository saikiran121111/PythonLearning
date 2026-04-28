import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


data = {
    'Name':   ['Alice','Bob','Charlie','Diana','Eve','Frank'],
    'Dept':   ['IT','HR','IT','Finance','IT','HR'],
    'Salary': [50000,60000,55000,70000,45000,80000],
    'Age':    [25,32,28,35,22,40]
}
df = pd.DataFrame(data)

#Chart 1 — Bar Chart (most common)
# Matplotlib way — more lines
plt.bar(df['Name'],df['Salary'],color = 'steelblue')
plt.title("Salary per employee")

plt.xlabel('Name')
plt.ylabel('Salary')

plt.show()

# Seaborn way — one line, looks better
sns.barplot(x='Name', y='Salary', data=df)
plt.title('Salary per Employee')
plt.show()

#Chart 2 — Line Chart (for trends)

# Seaborn line chart
sns.lineplot(x='Name', y='Salary', data=df, marker='o')
plt.title('Salary Trend')
plt.show()

#Chart 3 — Scatter Plot (compare two numbers)

# Does age relate to salary?
sns.scatterplot(x='Age', y='Salary', data=df, hue='Dept', s=100)
# hue='Dept' → different color per department
# s=100     → dot size
plt.title('Age vs Salary')
plt.show()

#Chart 4 — Histogram (distribution of values)
# How are salaries spread out?
plt.hist(df['Salary'], bins=5, color='coral', edgecolor='black')
plt.title('Salary Distribution')
plt.xlabel('Salary')
plt.ylabel('Count')
plt.show()

#Chart 5 — Heatmap (correlation — Seaborn's superpower)
# Which columns are related to each other?
sns.heatmap(df[['Salary','Age']].corr(), annot=True, cmap='Blues')
plt.title('Correlation Heatmap')
plt.show()

#The 3 Lines You Need Every Time
# Line 1 → create the chart
sns.barplot(x='Name', y='Salary', data=df)

# Line 2 → add title (optional but good habit)
plt.title('My Chart')

# Line 3 → display it
plt.show()