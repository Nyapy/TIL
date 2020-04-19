import pandas as pd
import numpy as np

#색인의 계층 색인

data = pd.Series(np.random.randn(10), index = [['a','a','a','b','b','b','c','c','d','d'], [1,2,3,1,2,3,1,2,1,2]])

print(data)
print(data.index)


data = pd.Series(np.random.randn(11), index = [['a','a','a','b','b','b','b','c','c','d','d'], [1,2,3,1,2,3,5,1,2,1,2]])
print(data)
print(data.index)

print(data['a':'b'])

print(data[2])
print(data[:,2])

df = pd.DataFrame(np.arange(12).reshape(4,3), index=[['a','a','b','b'],[1,2,1,2]], columns=[['서울','부산','광주'],['레드','그린','블루']])
print(df)
df.columns.names = ['city','color']
print(df)
print(df['서울'].iloc[0])