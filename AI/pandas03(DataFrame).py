import pandas as pd

a = pd.DataFrame([
[1,2,3],
[4,5,6],
[7,8,9]
])

print(a)

data = {
"cities":["서울","부산","광주","대구"],
"year":[2000,2001,2002,2003],
"pop":[4000,2000,1000,1000]
}

df = pd.DataFrame(data)
print(df)

df = pd.DataFrame(data, columns=['year', 'cities', 'pop'])

print(df)