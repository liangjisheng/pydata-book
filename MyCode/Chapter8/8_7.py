# -*- coding:utf-8 -*-
"""
@project = 0424-1
@file = 8_7
@author = Liangjisheng
@create_time = 2018/4/25 0025 下午 20:35
"""
import pandas as pd
import numpy as np
df = pd.DataFrame({'key': ['foo', 'bar', 'baz'],
                   'A': [1, 2, 3],
                   'B': [4, 5, 6],
                   'C': [7, 8, 9]})
print(df)
# key列可能是分组指标，其它的列是数据值。当使用pandas.melt，
# 我们必须指明哪些列是分组指标。下面使用key作为唯一的分组指标
melted = pd.melt(df, 'key')
print(melted)
# 使用pivot，可以重塑回原来的样子
reshaped = melted.pivot('key', 'variable', 'value')
print(reshaped)
# 因为pivot的结果从列创建了一个索引，用作行标签，我们可以使用reset_index将数据移回列
print(reshaped.reset_index())

# 你还可以指定列的子集，作为值的列
print(pd.melt(df, id_vars=['key'], value_vars=['A', 'B']))
# pandas.melt也可以不用分组指标
print(pd.melt(df, value_vars=['A', 'B', 'C']))
print(pd.melt(df, value_vars=['key', 'A', 'B']))
