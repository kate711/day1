# import matplotlib.pyplot as plt
# plt.bar([1,3,5,7,9],[5,2,7,8,2])
# plt.xlabel('bar number')
# plt.ylabel('bar height')
# plt.show()
# import pandas as pd
# d1 = pd.DataFrame([[1,2,3],[4,5,6]],columns=['a','b','c'])
# print(d1.head())
# print(d1.describe())

from pandas import Series, DataFrame

s = Series([1, 2, 3.0, 'abc', 'def'])
print(s)

s1 = Series(data=[1, 2, 3.0, 'abc', 'def'], index=[10, 20, 30, 40, 50])
print(s1)

data = {'id': [100, 101, 102, 103, 104], 'name': ['aa', 'bb', 'cc', 'dd', 'ee'], 'age': [18, 19, 20, 19, 18]}
data1 = DataFrame(data)
print(data1)

data2 = DataFrame(data, index=['one', 'two', 'three', 'four', 'five'])
print(data2)

from numpy import nan as NA

data3 = Series([12, None, 34, NA, 68])
print(data3)
print(data3.isnull())
print(data3.dropna())

from pandas import Series, DataFrame, np

data4 = DataFrame(np.random.randn(5, 4))
data4.ix[:2, 1] = NA
data4.ix[:3, 2] = NA

print(data4)
print('------')
print(data4.dropna(thresh=2))
print(data4.dropna(thresh=3))
