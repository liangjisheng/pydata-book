# -*- coding:utf-8 -*-
"""
@project = 0416-1
@file = pandas_6
@author = Liangjisheng
@create_time = 2018/4/17 0017 下午 19:33
"""
import pandas as pd
import numpy as np
# 处理整数索引的pandas对象常常难住新手，因为它与Python内置的列表和元组的索引语法不同
ser = pd.Series(np.arange(3.))
print(ser)
print(ser[0])
print(ser[1])
print(ser[2])
# print(ser[-1])    # error
# 对于非整数索引，上述问题不会出现
ser2 = pd.Series(np.arange(3.), index=['a', 'b', 'c'])
print(ser2)
print(ser2['a'])
print(ser2['b'])
print(ser2['c'])
print(ser2[0])
print(ser2[1])
print(ser2[2])
print(ser2[-1])
print(ser2[-2])
print(ser2[-3])

# 为了进行统一，如果轴索引含有整数，数据选取总会使用标签。为了更准确，
# 请使用loc（标签）或iloc（整数）
print(ser[:1])
print(ser.loc[:1])      # 使用标签索引，在最后会包含最后一个元素，跟python中正常索引不一样
print(ser.iloc[:1])
print()

# pandas最重要的一个功能是，它可以对不同索引的对象进行算术运算。在将对象相加时，
# 如果存在不同的索引对，则结果的索引就是该索引对的并集。对于有数据库经验的用户，
# 这就像在索引标签上进行自动外连接。看一个简单的例子
s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])
print(s1)
print(s2)
# 自动的数据对齐操作在不重叠的索引处引入了NaN值。缺失值会在算术运算过程中传播
print(s1 + s2)

# 对于DataFrame，对齐操作会同时发生在行和列上
df1 = pd.DataFrame(np.arange(9).reshape((3, 3)), columns=list('bcd'),
                   index=['Ohio', 'Texas', 'Colorado'])
df2 = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'),
                   index=['Utah', 'Ohio', 'Texas', 'Oregon'])
print(df1)
print(df2)
# 把它们相加后将会返回一个新的DataFrame，其索引和列为原来那两个DataFrame的并集
# 因为'c'和'e'列均不在两个DataFrame对象中，在结果中以缺省值呈现。行也是同样
print(df1 + df2)

# 如果DataFrame对象相加，没有共用的列或行标签，结果都会是空
df1 = pd.DataFrame({'A': [1, 2]})
df2 = pd.DataFrame({'B': [3, 4]})
print(df1)
print(df2)
print(df1 + df2)
