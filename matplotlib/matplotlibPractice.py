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

# Q1 — Bar chart of Salary per Department
#       (group by dept, use sns.barplot)
# Expected: 3 bars — Finance(70k), HR(70k avg), IT(50k avg)
sns.barplot( x='Dept',y='Salary',data=df )
plt.title('This is title')
plt.show()

# Q2 — Scatter plot of Age vs Salary
#       color each dot by Department (hue='Dept')
# Expected: 6 dots, each dept a different color
sns.scatterplot(x='Age',y='Salary',data=df,hue='Dept')
plt.title('THis is scatter Title')
plt.show()