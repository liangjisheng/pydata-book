# -*- coding:utf-8 -*-
"""
@project = 0424-1
@file = 8_5
@author = Liangjisheng
@create_time = 2018/4/25 0025 下午 19:40
"""
import pandas as pd
import numpy as np
# 轴向连接,另一种数据合并运算也被称作连接(concatenation)、绑定(binding)或堆叠(stacking)
# NumPy的concatenation函数可以用NumPy数组来做
arr = np.arange(12).reshape((3, 4))
print(arr)
print(np.concatenate([arr, arr], axis=0))
print(np.concatenate([arr, arr], axis=1))

# pandas的concat函数提供了一种能够解决这些问题的可靠方式。
# 我将给出一些例子来讲解其使用方式。假设有三个没有重叠索引的Series
s1 = pd.Series([0, 1], index=['a', 'b'])
s2 = pd.Series([2, 3, 4], index=['c', 'd', 'e'])
s3 = pd.Series([5, 6], index=['f', 'g'])
# 对这些对象调用concat可以将值和索引粘合在一起
print(pd.concat([s1, s2, s3]))
# 默认情况下，concat是在axis=0上工作的，最终产生一个新的Series。如果传入axis=1，
# 则结果就会变成一个DataFrame（axis=1是列）
print(pd.concat([s1, s2, s3], axis=1))
# 传入join='inner'即可得到它们的交集
s4 = pd.concat([s1, s3])
print(s4)
print(pd.concat([s1, s4], axis=1))
print(pd.concat([s1, s4], axis=1, join='inner'))
# 你可以通过join_axes指定要在其它轴上使用的索引
print(pd.concat([s1, s4], axis=1, join_axes=[['a', 'c', 'b', 'e']]))

# 不过有个问题，参与连接的片段在结果中区分不开。假设你想要在连接轴上创建一个层次化索引。
# 使用keys参数即可达到这个目的
result = pd.concat([s1, s1, s3], keys=['one', 'two', 'three'])
print(result)
print(result.unstack())
# 如果沿着axis=1对Series进行合并，则keys就会成为DataFrame的列头
print(pd.concat([s1, s2, s3], axis=1, keys=['one', 'two', 'three']))

# 同样的逻辑也适用于DataFrame对象
df1 = pd.DataFrame(np.arange(6).reshape(3, 2), index=['a', 'b', 'c'],
                   columns=['one', 'two'])
df2 = pd.DataFrame(5 + np.arange(4).reshape(2, 2), index=['a', 'c'],
                   columns=['three', 'four'])
print(df1)
print(df2)
print(pd.concat([df1, df2], axis=1, keys=['level1', 'level2']))
# 如果传入的不是列表而是一个字典，则字典的键就会被当做keys选项的值
print(pd.concat({'level1': df1, 'level2': df2}, axis=1))
# 举个例子，我们可以用names参数命名创建的轴级别
print(pd.concat([df1, df2], axis=1, keys=['level1', 'level2'],
                names=['upper', 'lower']))

df1 = pd.DataFrame(np.random.randn(3, 4), columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.random.randn(2, 3), columns=['b', 'd', 'a'])
print(df1)
print(df2)
print(pd.concat([df1, df2], ignore_index=True))
