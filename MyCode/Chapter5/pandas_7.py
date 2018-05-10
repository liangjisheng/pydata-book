# -*- coding:utf-8 -*-
"""
@project = 0416-1
@file = pandas_7
@author = Liangjisheng
@create_time = 2018/4/17 0017 下午 20:11
"""
import pandas as pd
import numpy as np
# 在对不同索引的对象进行算术运算时，你可能希望当一个对象中某个轴标签
# 在另一个对象中找不到时填充一个特殊值（比如0）
df1 = pd.DataFrame(np.arange(12.).reshape((3, 4)), columns=list('abcd'))
df2 = pd.DataFrame(np.arange(20.).reshape((4, 5)), columns=list('abcde'))
df2.loc[1, 'b'] = np.nan
print(df1)
print(df2)
print(df1 + df2)

# 使用df1的add方法，传入df2以及一个fill_value参数
print(df1.add(df2, fill_value=0))

# Series和DataFrame的算术方法。它们每个都有一个副本，以字母r开头，它会翻转参数
# 下面这两个语句是等价的
print(1 / df1)
print(df1.rdiv(1))
print(df1.div(1))

# 与此类似，在对Series或DataFrame重新索引时，也可以指定一个填充值
print(df1.reindex(columns=df2.columns, fill_value=0))
print()

arr = np.arange(12.).reshape((3, 4))
print(arr)
print(arr[0])
print(arr - arr[0])
# 当我们从arr减去arr[0]，每一行都会执行这个操作。这就叫做广播（broadcasting）
# DataFrame和Series之间的运算差不多也是如此
frame = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'),
                     index=['Utah', 'Ohio', 'Texas', 'Oregon'])
series = frame.iloc[0]
print(frame)
print(series)
# 默认情况下，DataFrame和Series之间的算术运算会将Series的索引匹配到DataFrame的列，
# 然后沿着行一直向下广播
print(frame - series)

# 如果某个索引值在DataFrame的列或Series的索引中找不到，
# 则参与运算的两个对象就会被重新索引以形成并集
series2 = pd.Series(range(3), index=['b', 'e', 'f'])
print(frame + series2)

# 如果你希望匹配行且在列上广播，则必须使用算术运算方法
# 传入的轴号就是希望匹配的轴。在本例中，我们的目的是匹配DataFrame的行索引
# （axis='index' or axis=0）并进行广播
series3 = frame['d']
print(series3)
print(frame.sub(series3, axis='index'))
