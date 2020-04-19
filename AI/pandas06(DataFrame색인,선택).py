import pandas as pd
import numpy as np


df = pd.DataFrame(np.arange(9).reshape(3,3), index = ['a','b','c'], columns=['x','y','z'])
print(df)
df2 = df.reindex(['a','b','c','d'])
print(df2)
col = ['w','x','y','z']
print(df.reindex(columns=col))

df3 = df.reindex(index = ['a','b','c','d'], columns = col)

print(df3)

df3 = df.reindex(index = ['a','b','c','d'], columns = col, method='ffill')
print(df3)

