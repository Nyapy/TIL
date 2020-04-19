import pandas as pd
import numpy as np

s1 = pd.Series([5,6,-1,2], index = ['a','b','d','c'])

s2 = pd.Series([7,5,6,-1,2], index = ['a','b','e','d','f'])

print(s1+s2)

df1 = pd.DataFrame(np.arange(9).reshape(3,3), columns=list('bcd'), index = ["서울","대전","부산"])
df2 = pd.DataFrame(np.arange(12).reshape(4,3), columns=list('bde'), index = ["서울","대전","수원","부산"])

print(df1+df2)

df3 = pd.DataFrame(np.arange(12).reshape(3,4), columns=list('abcd'),)
df4 = pd.DataFrame(np.arange(20).reshape(4,5), columns=list('abcde'))

print(df3)
print(df4)

print(df3+df4)

print(df3.add(df4,fill_value=0))