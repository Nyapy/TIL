import pandas as pd
import numpy as np

obj = pd.Series(np.arange(5), index = ['a','b','c','d','e'])

print(obj)

obj2 = obj.drop('c')

print(obj2)

obj3 = obj.drop(['b','d','c'])


print(obj3)

df = pd.DataFrame(np.arange(16).reshape(4,4), index = ["서울","부산","대전","대구"], columns=["one","two","three","four"])

print(df)

newdf = df.drop(["서울","대전"])

print(newdf)

ndf = df.drop("one", axis = 1)
print(ndf)