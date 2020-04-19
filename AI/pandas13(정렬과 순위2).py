import pandas as pd
import numpy as np

frame= pd.DataFrame({'b':[4,7,-5,2], 'a':[0,0,3,2]})

print(frame)

print(frame.sort_values(by='b'))
print(frame.sort_values(by='a'))
print(frame.sort_values(by=['a','b']))
print(frame.sort_values(by=['b','a']))

obj3 = pd.Series([7,-2,7,4,2,0,4,4,4])


print("--------------------------------------------------------------")
print(obj3)
print(obj3.rank())
print(obj3.rank(method="first"))

print("------------그룹------------------")
print(obj3)
print(obj3.rank(ascending=False, method='max'))
print(obj3.rank(ascending=False, method='min'))