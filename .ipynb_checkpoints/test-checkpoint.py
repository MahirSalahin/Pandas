import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [21, 25, 23],
        'A': [20, 215, 223],
        'City': ['New York', 'London', 'Los Angeles']}
df = pd. DataFrame(data,index=['a','b','c'])
df = df.iloc[1:3]
print(df)