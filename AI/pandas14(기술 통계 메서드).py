import pandas as pd
import numpy as np

#중복색인

obj = pd.Series(range(5), index = ['a','a','b','b','c'])

print(obj)

df = pd.DataFrame(np.random.randn(4,3), index = ['a','a','b','b'])

print(df)
print(df.loc['a'])


###########################3
df= pd.DataFrame([[1.4,np.nan],[7.1,-4.5],[np.nan, np.nan],[0.75,-1.3]], index = ['a','b','c','d'], columns=['one','two'])

print(df)

# 각 컬럼 or 행 합
print(df.sum())

print(df.sum(axis=1))
print(df.sum(axis=1, skipna=False))

# 간접통계
print(df.idxmin())
print(df.idxmax())

# 누산 메서드
print(df.cumsum())

# 유일한 값, 도수 메서드
s1 = pd.Series(['c','a','d','a','a','b','b','c','c'])
uniq = s1.unique()
print(uniq)

cnt = s1.value_counts()
print(cnt)

print(uniq)
print(s1.sort_index())

# isin 있는지 없는지 불리언으로 반환
mask = s1.isin(['b','c'])
print(mask)


data = pd.DataFrame({'Q1':[1,2,3,4,3], 'Q2':[2,2,1,3,5], 'Q3':[1,7,3,4,4]})
print(data)
res = data.apply(pd.value_counts)
print(res)

#
stringData = pd.Series(['aaa','bbb','ccc',np.nan])
print(stringData)
print(stringData.isnull())

stringData[0] = None
print(stringData)
print(stringData.isnull())