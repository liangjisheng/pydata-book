# -*- coding:utf-8 -*-
"""
@project = 0424-1
@file = 8_6
@author = Liangjisheng
@create_time = 2018/4/25 0025 下午 20:03
"""
# 使用NumPy的where函数，它表示一种等价于面向数组的if-else
import pandas as pd
import numpy as np
a = pd.Series([np.nan, 2.5, np.nan, 3.5, 4.5, np.nan],
              index=['f', 'e', 'd', 'c', 'b', 'a'])
b = pd.Series(np.arange(len(a), dtype=np.float64),
              index=['f', 'e', 'd', 'c', 'b', 'a'])
b[-1] = np.nan
print(a)
print(b)
print(b[:-2])
# Series有一个combine_first方法，实现的也是一样的功能，还带有pandas的数据对齐
print(b[:-2].combine_first(a[2:]))
# 对于DataFrame，combine_first自然也会在列上做同样的事情，因此你可以将其看做：
# 用传递对象中的数据为调用对象的缺失数据“打补丁”
df1 = pd.DataFrame({'a': [1., np.nan, 5., np.nan],
                    'b': [np.nan, 2., np.nan, 6.],
                    'c': range(2, 18, 4)})
df2 = pd.DataFrame({'a': [5., 4., np.nan, 3., 7.],
                    'b': [np.nan, 3., 4., 6., 8.]})
print(df1)
print(df2)
print(df1.combine_first(df2))
print()

# 有许多用于重新排列表格型数据的基础运算。这些函数也称作重塑（reshape）或轴向旋转（pivot）运算
# 重塑层次化索引, 层次化索引为DataFrame数据的重排任务提供了一种具有良好一致性的方式
# 主要功能有二
# stack：将数据的列“旋转”为行。
# unstack：将数据的行“旋转”为列
data = pd.DataFrame(np.arange(6).reshape((2, 3)),
                    index=pd.Index(['Ohio', 'Colorado'], name='state'),
                    columns=pd.Index(['one', 'two', 'three'], name='number'))
print(data)
# 对该数据使用stack方法即可将列转换为行，得到一个Series
result = data.stack()
print(result)
# 对于一个层次化索引的Series，你可以用unstack将其重排为一个DataFrame
print(result.unstack())
# 默认情况下，unstack操作的是最内层（stack也是如此）。传入分层级别的编号或名称
# 即可对其它级别进行unstack操作
print(result.unstack(0))
print(result.unstack('state'))

# 如果不是所有的级别值都能在各分组中找到的话，则unstack操作可能会引入缺失数据
s1 = pd.Series([0, 1, 2, 3], index=['a', 'b', 'c', 'd'])
s2 = pd.Series([4, 5, 6], index=['c', 'd', 'e'])
data2 = pd.concat([s1, s2])
print(data2)
data2 = pd.concat([s1, s2], keys=['one', 'two'])
print(data2)
print(data2.unstack())
# stack默认会滤除缺失数据，因此该运算是可逆的
print(data2.unstack().stack())
print(data2.unstack().stack(dropna=False))

# 在对DataFrame进行unstack操作时，作为旋转轴的级别将会成为结果中的最低级别
print(result)
df = pd.DataFrame({'left': result, 'right': result + 5},
                  columns=pd.Index(['left', 'right'], name='side'))
print(df)
print(df.unstack('state'))
# 当调用stack，我们可以指明轴的名字
print(df.unstack('state').stack('side'))
