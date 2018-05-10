# -*- coding:utf-8 -*-
"""
@project = 0416-1
@file = pandas_5
@author = Liangjisheng
@create_time = 2018/4/17 0017 下午 19:10
"""
import pandas as pd
import numpy as np
# Series索引（obj[...]）的工作方式类似于NumPy数组的索引，只不过Series的索引值不只是整数
obj = pd.Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
print(obj)
print(obj['b'])
print(obj[1])
print(obj[2:4])
print(obj[['b', 'a', 'd']])
print(obj[[1, 3]])
print(obj[obj < 2])

# 利用标签的切片运算与普通的Python切片运算不同，其末端是包含的
print(obj['b':'c'])
obj['b':'c'] = 5
print(obj)
print()

# 用一个值或序列对DataFrame进行索引其实就是获取一个或多个列
data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
print(data)
print(data['two'])
print(data[['three', 'one']])
# 这种索引方式有几个特殊的情况。首先通过切片或布尔型数组选取数据
print(data[:2])
print(data[data['three'] > 5])
# 另一种用法是通过布尔型DataFrame（比如下面这个由标量比较运算得出的）进行索引
print(data < 5)
data[data < 5] = 0
print(data)
print()

# 对于DataFrame的行的标签索引，我引入了特殊的标签运算符loc和iloc
# 它们可以让你用类似NumPy的标记，使用轴标签（loc）或整数索引（iloc）
# 从DataFrame选择行和列的子集
# 通过标签选择一行和多列
print(data.loc['Colorado', ['two', 'three']])
# 然后用iloc和整数进行选取
print(data.iloc[2, [3, 0, 1]])
print(data.iloc[2])
print(data.iloc[[1, 2], [3, 0, 1]])
# 这两个索引函数也适用于一个标签或多个标签的切片
print(data.loc[:'Utah', 'two'])
print(data.iloc[:, :3])
print(data.iloc[:, :3][data.three > 5])
