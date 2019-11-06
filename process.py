import pandas as pd
import numpy as np

# datafile = 'D:/新建 Microsoft Office Excel 工作表.xlsx'
# data = pd.read_excel(datafile,header=None)
# min = (data-data.min())/(data.max()-data.min())
# zero = (data - data.mean())/data.std()
# float = data/10**np.ceil(np.log10(data.abs().max())) #小数定标规范化
# print("原始数据为：\n",data)
# print('--------------------')
# print('最小-最大规范化后的数据：\n',min)

from pandas import Series, DataFrame

df = DataFrame(np.random.randn(4, 3), index=list('abcd'), columns=['frist', 'second', 'third'])
print(df)
print(df.describe())
print(df.sum())
print(df.sum(axis=1))
print('-----------')
print(df.idxmax(), df.idxmin(), df.idxmin(axis=1))
print(df.cumsum())
print(df.var())
print(df.std())
print(df.pct_change())
print(df.cov())
print(df.corr())
