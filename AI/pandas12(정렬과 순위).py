import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(4,3), columns=list('bde'), index = ['서울', '대전', '대구','인천'])

format = lambda x: '%.2f' %x
print(df['e'].map(format))

s1 = df['e'].map(format)

print(s1.sort_index())

df2 = pd.DataFrame(np.arange(8).reshape(2,4), index = ["three", "one"], columns=['d','a','b','c'])

print(df2)
print(df2.sort_index())
print(df2.sort_index(axis=1))

obj = pd.Series([4,7,-3,1])
print(obj)
print(obj.sort_values())

obj2 = pd.Series([4,np.nan, 8, np.nan, -10, 2])
print(obj2)
print(obj2.sort_values())
print(obj2.sort_values(ascending=False))