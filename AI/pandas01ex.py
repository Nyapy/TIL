import pandas as pd

obj = pd.Series([1, 2, 3, 4])

print(obj)

print(obj.values)

print(obj.index)

obj2 = pd.Series([4,5,6,2], index=['a','b','c','d'])

print(obj2)


obj3 = pd.Series([4,5,6,2], index=['a','b',"2",3])

print(obj3)

print(obj2['a'])

print(obj2[['a','c','b']])

print(obj2*2)

print('a' in obj2)

print(5 in obj2.values)

data = {"kim":100, "lee":1000, "park":80, "kang":50, "hong":30}

obj4 = pd.Series(data)

print(obj4)

name = ["p","lee","kim","h"]

obj5 = pd.Series(data, index = name)

print(obj5)

print(pd.isnull(obj5))
print(pd.notnull(obj5))