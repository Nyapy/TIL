import pandas as pd
import numpy as np



data = pd.Series(np.random.randn(11), index = [['a','a','a','b','b','b','b','c','c','d','d'], [1,2,3,1,2,3,5,1,2,1,2]])
print(data)
print(data.index)

print(data['a':'b'])

print(data[2])
print(data[:,2])

df = pd.DataFrame(np.arange(12).reshape(4,3), index=[['a','a','b','b'],[1,2,1,2]], columns=[['서울','부산','광주'],['레드','그린','블루']])
print(df)
df.columns.names = ['city','color']
df.index.names = ['key1','key2']
print(df)

print(df.swaplevel('key1','key2'))

#사전식으로 계층을 바꾸어 정렬
#sortlevel()메소드를 이용해 정렬
#안되네 없어졌나??

print(df.sum(level='key2'))


df = pd.DataFrame(np.arange(12).reshape(4,3), index=[['a','a','b','b'],[1,2,1,2]], columns=[['서울','부산','광주'],['레드','그린','레드']])
df.columns.names = ['city','color']
df.index.names = ['key1','key2']
print(df)
print(df.sum(level='color', axis=1))