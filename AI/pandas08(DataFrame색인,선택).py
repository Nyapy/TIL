import pandas as pd
import numpy as np


obj = pd.Series(np.arange(4), index = ['a','b','c','d'])

print(obj)

data = pd.DataFrame(np.arange(16).reshape(4,4), index = ["서울","대전","대구","부산"], columns = ["one","two","three","four"])
print(data)


print(data[data["three"]>5])
print(data <5)