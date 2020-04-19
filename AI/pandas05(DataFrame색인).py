import pandas as pd
import numpy as np

data = {
"cities":["서울","부산","광주","대구"],
"year":[2000,2001,2002,2003],
"pop":[4000,2000,1000,1000]
}

data2 = {"서울": {2000:20, 2001:30},
"부산" : {2000:10, 2001:50, 2002:70}}

df3 = pd.DataFrame(data2)
print(df3)

print(df3.T)

obj = pd.Series(range(3), index =['a','b','c'])
print(obj)

idx = obj.index
print(idx)
print(idx[1])

index2 = pd.Index(np.arange(3))
print(index2)

obj = pd.Series([2.3,4.3,-4.1,3.5], index = ['d','b','a','c'])

print(obj)
obj2 = obj.reindex(['a','b','c','d','e'])
print(obj2)
obj3 = obj.reindex(['a','b','c','d','e','f'], fill_value=0.0)
print(obj3)

df = pd.DataFrame(np.arange(9))
print(df)
df = pd.DataFrame(np.arange(9).reshape(3,3), index = ['a','b','c'])
print(df)
df = pd.DataFrame(np.arange(9).reshape(3,3), index = ['a','b','c'], columns=['x','y','z'])
print(df)
df2 = df.reindex(['a','b','c','d'])
print(df2)
col = ['w','x','y','z']
print(df.reindex(columns=col))

obj4 = pd.Series(['blue','red','yellow'], index=[0,2,4])
print(obj4)
obj5 = obj4.reindex(range(6), method='ffill')
print(obj5)
obj6 = obj4.reindex(range(6), fill_value="green")
print(obj6)