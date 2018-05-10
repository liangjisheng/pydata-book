# -*- coding:utf-8 -*-
"""
@project = 0422-2
@file = 7_1
@author = Liangjisheng
@create_time = 2018/4/22 0022 下午 15:35
"""
import pandas as pd
import numpy as np
# pandas使用浮点值NaN（Not a Number）表示缺失数据。我们称其为哨兵值，可以方便的检测出来
string_data = pd.Series(['aardvark', 'artichoke', np.nan, 'avocado'])
print(string_data)
print(string_data.isnull())
# Python内置的None值在对象数组中也可以作为NA：
string_data[0] = None
print(string_data.isnull())

# 过滤掉缺失数据的办法有很多种。你可以通过pandas.isnull或布尔索引的手工方法，
# 但dropna可能会更实用一些。对于一个Series，dropna返回一个仅含非空数据和索引值的Series：
from numpy import nan as NA
data = pd.Series([1, NA, 3.5, NA, 7])
print(data.dropna())
# 等价于
print(data[data.notnull()])

# 而对于DataFrame对象，事情就有点复杂了。你可能希望丢弃全NA或含有NA的行或列。
# dropna默认丢弃任何含有缺失值的行
data = pd.DataFrame([[1., 6.5, 3.], [1., NA, NA], [NA, NA, NA], [NA, 6.5, 3.]])
print(data)
cleaned = data.dropna()
print(cleaned)
# 传入how='all'将只丢弃全为NA的那些行
print(data.dropna(how='all'))

# 用这种方式丢弃列，只需传入axis=1即可：
data[4] = NA
print(data)
print(data.loc[0])
print(data.dropna(axis=1, how='all'))

# 另一个滤除DataFrame行的问题涉及时间序列数据。假设你只想留下一部分观测数据，可以用thresh参数实现此目的
df = pd.DataFrame(np.random.randn(7, 3))
df.iloc[:4, 1] = NA
df.iloc[:2, 2] = NA
print(df)
print(df.dropna())
print(df.dropna(thresh=2))

# 你可能不想滤除缺失数据（有可能会丢弃跟它有关的其他数据），而是希望通过其他方式填补那些“空洞”
# 对于大多数情况而言，fillna方法是最主要的函数。通过一个常数调用fillna就会将缺失值替换为那个常数值
print(df.fillna(0))
# 若是通过一个字典调用fillna，就可以实现对不同的列填充不同的值
print(df.fillna({1: 0.5, 2: 0}))
# fillna默认会返回新对象，但也可以对现有对象进行就地修改,就地修改后函数没有返回值，
# _为None
_ = df.fillna(0, inplace=True)
print(df)
print(_)

# 对reindexing有效的那些插值方法也可用于fillna
df = pd.DataFrame(np.random.randn(6, 3))
df.iloc[2:, 1] = NA
df.iloc[4:, 2] = NA
print(df)
print(df.fillna(method='ffill'))
print(df.fillna(method='ffill', limit=2))

data = pd.Series([1., NA, 3.5, NA, 7])
print(data.fillna(data.mean()))
