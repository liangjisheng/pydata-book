# -*- coding:utf-8 -*-
"""
@project = 0411-2
@file = numpy_7
@author = Liangjisheng
@create_time = 2018/4/14 0014 下午 15:25
"""
import numpy as np
arr = np.random.randn(6)
print(arr)
# NumPy数组也可以通过sort方法就地排序
arr.sort()
print(arr)

# 多维数组可以在任何一个轴向上进行排序，只需将轴编号传给sort即可
arr = np.random.randn(5, 3)
print(arr)
arr.sort(axis=1)
print(arr)
print()

# 顶级方法np.sort返回的是数组的已排序副本，而就地排序则会修改数组本身
# 计算数组分位数最简单的办法是对其进行排序，然后选取特定位置的值
large_arr = np.random.randn(1000)
large_arr.sort()
print(large_arr[int(0.05 * len(large_arr))])    # 5% quantile

# umPy提供了一些针对一维ndarray的基本集合运算。最常用的可能要数np.unique了，
# 它用于找出数组中的唯一值并返回已排序的结果
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
print(np.unique(names))
print(sorted(set(names)))
ints = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])
print(np.unique(ints))
# 另一个函数np.in1d用于测试一个数组中的值在另一个数组中的成员资格，返回一个布尔型数组
values = np.array([6, 0, 0, 3, 2, 5, 6])
print(np.in1d(values, [2, 3, 6]))
