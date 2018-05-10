# -*- coding:utf-8 -*-
"""
@project = 0416-1
@file = pandas_1
@author = Liangjisheng
@create_time = 2018/4/16 0016 下午 19:07
"""
import pandas as pd
import numpy as np
# Series是一种类似于一维数组的对象，它由一组数据（各种NumPy数据类型）
# 以及一组与之相关的数据标签（即索引）组成。仅由一组数据即可产生最简单的Series
obj = pd.Series([4, 7, -5, 3])
print(obj)
print(obj.values)
print(obj.index)
print()

obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
print(obj2)
print(obj2.index)
# 与普通NumPy数组相比，你可以通过索引的方式选取Series中的单个或一组值：
print(obj2['a'])
obj2['d'] = 6
print(obj2)
print()

# ['c', 'a', 'd']是索引列表，即使它包含的是字符串而不是整数
print(obj2[['c', 'a', 'd']])

# 使用NumPy函数或类似NumPy的运算（如根据布尔型数组进行过滤、标量乘法、应用数学函数等）
# 都会保留索引值的链接：
print(obj2[obj2 > 0])
print(obj2 * 2)
print(np.exp(obj2))

# 还可以将Series看成是一个定长的有序字典，因为它是索引值到数据值的一个映射
# 它可以用在许多原本需要字典参数的函数中
print('b' in obj2)
print('e' in obj2)

# 如果数据被存放在一个Python字典中，也可以直接通过这个字典来创建Series
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
#
obj3 = pd.Series(sdata)
print(obj3)

# 如果只传入一个字典，则结果Series中的索引就是原字典的键（有序排列）
# 你可以传入排好序的字典的键以改变顺序
states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = pd.Series(sdata, index=states)
print(obj4)
# pandas的isnull和notnull函数可用于检测缺失数据：
print(pd.isnull(obj4))
print(pd.notnull(obj4))
# Series也有类似的实例方法
print(obj4.isnull())
print(obj4.notnull())
print()

# 对于许多应用而言，Series最重要的一个功能是，它会根据运算的索引标签自动对齐数据：
# 如果你使用过数据库，你可以认为是类似join的操作
print(obj3)
print(obj4)
print(obj3 + obj4)

# Series对象本身及其索引都有一个name属性，该属性跟pandas其他的关键功能关系非常密切
obj4.name = 'population'
obj4.index.name = 'state'
print(obj4)

# Series的索引可以通过赋值的方式就地修改
print(obj)
obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
print(obj)
