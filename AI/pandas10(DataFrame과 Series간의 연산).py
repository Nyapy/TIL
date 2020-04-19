import pandas as pd
import numpy as np

arr = np.arange(12.).reshape(3,4)

print(arr)

print(arr-arr[0])

df = pd.DataFrame(np.arange(12).reshape(4,3), columns=list('bde'), index =["서울","대전","대구","부산"])

s1 = df.iloc[0]
print(df)
print(s1)

print(df-s1)

s2 = pd.Series(range(3), index=list("bef"))
print(s2)

print(df-s2)

########################
s3 = df['d']
print(s3)

print(df+s3)

print(df.add(s3, axis=0))