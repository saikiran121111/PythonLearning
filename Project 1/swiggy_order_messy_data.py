import pandas as pd

swiggy_data = [
    (101, 'Biryani Blues', 'Hyderabad', '₹450', 4.5),
    (102, 'Pista House', 'Hyderabad', '₹300', None),       # Rating is missing
    (103, 'Truffles', 'Bangalore', '₹600', 4.2),
    (104, 'Haldirams', 'Delhi', '₹250', 4.0),
    (105, 'Biryani Blues', None, '₹550', 4.8),             # City is missing
    (106, 'Dominos', 'Mumbai', '₹800', None),              # Rating is missing
    (107, 'Pista House', 'Hyderabad', '₹400', 4.1)
]

columns = ['order_id', 'restaurant', 'city', 'amount', 'rating']

df = pd.DataFrame(swiggy_data,columns=columns)

df['city'] = df['city'].fillna('Unknown')
df['amount'] = df['amount'].str.replace('₹','').astype(int)
df['rating'] = df['rating'].fillna(0.0)

print(df)
print('################################################')
print(df['restaurant'].value_counts().head(2))
print(df[(df['amount'] == df['amount'].max())])
print('################################################')
print(df.groupby('city')['amount'].sum().reset_index())