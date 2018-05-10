# -*- coding:utf-8 -*-
"""
@project = 0424-1
@file = 8_3
@author = Liangjisheng
@create_time = 2018/4/24 0024 下午 20:07
"""
# pandas.merge可根据一个或多个键将不同DataFrame中的行连接起来。SQL或其他关系型数据库
# 的用户对此应该会比较熟悉，因为它实现的就是数据库的join操作
# pandas.concat可以沿着一条轴将多个对象堆叠到一起
# 实例方法combine_first可以将重复数据编接在一起，用一个对象中的值填充另一个对象中的缺失值
# 数据库风格的DataFrame合并
# 数据集的合并（merge）或连接（join）运算是通过一个或多个键将行链接起来的。
# 这些运算是关系型数据库（基于SQL）的核心。pandas的merge函数是对数据应用这些算法的主要切入点
import pandas as pd
import numpy as np
df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                    'data1': range(7)})
df2 = pd.DataFrame({'key': ['a', 'b', 'd'],
                    'data2': range(3)})
print(df1)
print(df2)
# 这是一种多对一的合并。df1中的数据有多个被标记为a和b的行，而df2中key列的每个值则仅对应一行。
# 对这些对象调用merge即可得到
print(pd.merge(df1, df2))
print(pd.merge(df2, df1))
# 注意，我并没有指明要用哪个列进行连接。如果没有指定，merge就会将重叠列的列名当做键。
# 不过，最好明确指定一下
print(pd.merge(df1, df2, on='key'))

# 如果两个对象的列名不同，也可以分别进行指定
df3 = pd.DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                    'data1': range(7)})
df4 = pd.DataFrame({'rkey': ['a', 'b', 'd'],
                    'data2': range(3)})
print(pd.merge(df3, df4, left_on='lkey', right_on='rkey'))

# 可能你已经注意到了，结果里面c和d以及与之相关的数据消失了。默认情况下，merge做的是“内连接”
# 结果中的键是交集。其他方式还有"left"、"right"以及"outer"。外连接求取的是键的并集，
# 组合了左连接和右连接的效果
print(pd.merge(df1, df2, how='outer'))
print()

# 多对多的合并有些不直观。看下面的例子
df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
                    'data1': range(6)})
df2 = pd.DataFrame({'key': ['a', 'b', 'a', 'b', 'd'],
                    'data2': range(5)})
print(df1)
print(df2)
# 多对多连接产生的是行的笛卡尔积。由于左边的DataFrame有3个"b"行，右边的有2个，
# 所以最终结果中就有6个"b"行。连接方式只影响出现在结果中的不同的键的值
print(pd.merge(df1, df2, on='key', how='left'))
print(pd.merge(df1, df2, how='inner'))
print()

# 要根据多个键进行合并，传入一个由列名组成的列表即可
left = pd.DataFrame({'key1': ['foo', 'foo', 'bar'],
                     'key2': ['one', 'two', 'one'],
                     'lval1': [1, 2, 3]})
right = pd.DataFrame({'key1': ['foo', 'foo', 'bar', 'bar'],
                      'key2': ['one', 'one', 'one', 'two'],
                      'rval': [4, 5, 6, 7]})
print(left)
print(right)
# 结果中会出现哪些键组合取决于所选的合并方式，你可以这样来理解：
# 多个键形成一系列元组，并将其当做单个连接键（当然，实际上并不是这么回事）
print(pd.merge(left, right, on=['key1', 'key2'], how='outer'))
# 对于合并运算需要考虑的最后一个问题是对重复列名的处理。虽然你可以手工处理列名重叠的问题
# （查看前面介绍的重命名轴标签），但merge有一个更实用的suffixes选项，用于指定附加到左右
# 两个DataFrame对象的重叠列名上的字符串
print(pd.merge(left, right, on='key1'))
print(pd.merge(left, right, on='key1', suffixes=('_left', '_right')))
