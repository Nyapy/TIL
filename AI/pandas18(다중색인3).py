import pandas as pd
import numpy as np

df= pd.DataFrame({'a':range(7), 'b':range(7,0,-1), 'c':['one','one','one', 'two','two','two','two'], 'd':[0,1,2,0,1,2,3]})
print(df)

print(df.set_index(['c','d']))
print(df.set_index(['c','d'],drop=False))
df2 = df.set_index(['c','d'],)
print(df2)
print(df2.reset_index())