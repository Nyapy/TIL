import pandas as pd

data = {"Seoul":100, "Busan":200, "Gumi":300, "Changwon":500}

obj = pd.Series(data)

print(obj)

cities = ["Seoul", "Busan", "Changwon", "Daegu"]

obj2 = pd.Series(data, index=cities)

print(obj2)

print(obj+obj2)

obj2.name = "인구수"

print(obj2)

obj2.index.name ="도시"

print(obj2)

obj2.index = ["Daejeon", "Busan", "Jaeju", "Jeonju"]

print(obj2)