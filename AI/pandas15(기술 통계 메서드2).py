import pandas as pd
import numpy as np

#누락된 데이터 골라내기
#dropna 함수를 이용 등 여러 방법이 있음
data = pd.Series([1,np.nan, 3.4, np.nan, 8])
print(data.dropna())

print(data.notnull())

#DataFrame에서 누락된 데이터 고르기
data = pd.DataFrame([[1,5.5,3],[1,np.nan,np.nan],[np.nan,np.nan,np.nan],[np.nan,3.3,3]])

print(data)
print(data.dropna())
data[4]= np.nan
print(data)
print(data.dropna(how='all'))
print(data.dropna(how='all',axis=1))

data2 =  pd.DataFrame([[1,2,3,np.nan],[1,33,np.nan,np.nan],[np.nan,2,np.nan,np.nan],[np.nan,np.nan,np.nan,np.nan]])

print(data2.dropna(thresh=2))
print(data2.fillna(0))
print(data2.fillna({1:50,3:30}))
print(data2.fillna(method='ffill', limit=1))

data3 = pd.Series([1,np.nan, 4, np.nan, 7])
print(data3)
print(data3.fillna(data3.mean()))