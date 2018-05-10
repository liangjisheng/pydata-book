# -*- coding:utf-8 -*-
"""
@project = 0416-1
@file = pandas_8
@author = Liangjisheng
@create_time = 2018/4/18 0018 下午 19:14
"""
import pandas as pd
import numpy as np
# NumPy的ufuncs（元素级数组方法）也可用于操作pandas对象
frame = pd.DataFrame(np.random.rand(4, 3), columns=list('bde'),
                     index=['Utah', 'Ohio', 'Texas', 'Oregon'])
print(frame)
print(np.abs(frame))
# 另一个常见的操作是，将函数应用到由各列或行所形成的一维数组上。
# DataFrame的apply方法即可实现此功能
# 这里的函数f，计算了一个Series的最大值和最小值的差，在frame的每列都执行了一次
# 结果是一个Series，使用frame的列作为索引
f = lambda x: x.max() - x.min()
print(frame.apply(f))
# 如果传递axis='columns'到apply，这个函数会在每行执行
print(frame.apply(f, axis='columns'))
# 许多最为常见的数组统计功能都被实现成DataFrame的方法（如sum和mean），
# 因此无需使用apply方法

# 传递到apply的函数不是必须返回一个标量，还可以返回由多个值组成的Series
def f(x):
    return pd.Series([x.min(), x.max()], index=['min', 'max'])
print(frame.apply(f))

# 元素级的Python函数也是可以用的。假如你想得到frame中各个浮点值的格式化字符串，
# 使用applymap即可
format = lambda x: '%.2f' % x
print(frame.applymap(format))

# 之所以叫做applymap，是因为Series有一个用于应用元素级函数的map方法
print(frame['e'].map(format))
print(frame)

# 根据条件对数据集排序（sorting）也是一种重要的内置运算。要对行或列索引进行排序
# （按字典顺序），可使用sort_index方法，它将返回一个已排序的新对象
obj = pd.Series(range(4), index=['d', 'a', 'b', 'c'])
print(obj.sort_index())
# 对于DataFrame，则可以根据任意一个轴上的索引进行排序
frame = pd.DataFrame(np.arange(8).reshape((2, 4)),
                     index=['three', 'one'],
                     columns=['d', 'a', 'b', 'c'])
print(frame)
print(frame.sort_index())
print(frame.sort_index(axis=1))
print(frame.sort_index().sort_index(axis=1))

# 数据默认是按升序排序的，但也可以降序排序：
print(frame.sort_index(axis=1, ascending=False))

# 若要按值对Series进行排序，可使用其sort_values方法：
obj = pd.Series([4, 7, -3, 2])
print(obj.sort_values())
print(obj.sort_values(ascending=False))

# 在排序时，任何缺失值默认都会被放到Series的末尾
obj = pd.Series([4, np.nan, 7, np.nan, -3, 2])
print(obj)
print(obj.sort_values())
print(obj.sort_values(ascending=False))

# 当排序一个DataFrame时，你可能希望根据一个或多个列中的值进行排序
# 将一个或多个列的名字传递给sort_values的by选项即可达到该目的
frame = pd.DataFrame({'b': [4, 7, -3, 2], 'a': [0, 1, 0, 1]})
print(frame)
print(frame.sort_values(by='b'))
# 要根据多个列进行排序，传入名称的列表即可
print(frame.sort_values(by=['a', 'b']))
