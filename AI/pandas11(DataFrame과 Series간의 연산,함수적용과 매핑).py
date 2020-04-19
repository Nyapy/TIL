import pandas as pd
import numpy as np

df=pd.DataFrame(np.random.randn(4,3), columns =list('bde'), index = ["서울","대전","대구","부산"])
print(df)

print(np.abs(df))

f=lambda x : x.max()-x.min()
print(df.apply(f))

print(df.apply(f, axis=1))


def f(x):
 return pd.Series([x.min(), x.max()], index=['min', 'max'])

print(df.apply(f))

# 배열의 

format = lambda x : '%.2f' % x

print(df.applymap(format))
print(df['e'].map(format))