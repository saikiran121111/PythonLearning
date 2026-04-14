import pandas as pd


#1 Series
scores = pd.Series([45, 72, 38, 90, 55], index=[1,2,3,4,5]) # Can set custom indexing etccc

print(scores)

#2 DataFrame

data = {
    'Name':   ['Ruku', 'Sai', 'Kiran', 'Arjun'],
    'Age':    [22, 25, 23, 24],
    'Score':  [85, 92, 78, 95]
}

finall = pd.DataFrame(data)

print(finall)