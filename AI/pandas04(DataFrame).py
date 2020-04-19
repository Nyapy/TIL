import pandas as pd
import numpy as np

data = {
"cities":["서울","부산","광주","대구"],
"year":[2000,2001,2002,2003],
"pop":[4000,2000,1000,1000]
}

df = pd.DataFrame(data)
print(df)

df = pd.DataFrame(data, columns=['year', 'cities', 'pop'])

print(df)

df2=pd.DataFrame(data, columns=['year','cities','pop','dist'], index = ['one','two','three','four'])

print(df2)

print(df2['cities'])
print(df2['year'])

print(df2.columns)
print(df2.index)


print(df2.loc["one"])
print(df2.loc["one":"three", "cities":"dist"])

df2["dist"] = 100

print(df2)

df2["dist"] = np.arange(4.)

print(df2)

val = pd.Series([1000, 2000, 3000, 4000], index = ['one','two','three','four'])

df2["dist"] = val

print(df2)

val1 = pd.Series([1000,3000,5000], index = ['one','three','four'])
df2["dist"] = val1

print(df2)

df2['aaa'] = df2.cities == "서울"

print(df2)

del df2['aaa']

print(df2)

data2 = {"서울": {2000:20, 2001:30},
"부산" : {2000:10, 2001:50, 2002:70}}

df3 = pd.DataFrame(data2)
print(df3)

print(df)


