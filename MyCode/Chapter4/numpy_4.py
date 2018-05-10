# -*- coding:utf-8 -*-
"""
@project = 0411-2
@file = numpy_4
@author = Liangjisheng
@create_time = 2018/4/14 0014 上午 11:59
"""
import numpy as np
arr = np.empty((8, 4))
print(arr)
print()

for i in range(8):
    arr[i] = i
print(arr)
print()

# 为了以特定顺序选取行子集，只需传入一个用于指定顺序的整数列表或ndarray即可
print(arr[[4, 3, 0, 6]])
# 这段代码确实达到我们的要求了！使用负数索引将会从末尾开始选取行
print(arr[[-3, -5, -7]])
print()

# 一次传入多个索引数组会有一点特别。它返回的是一个一维数组，其中的元素对应各个索引元组
arr = np.arange(32).reshape((8, 4))
print(arr)
# 最终选出的是元素(1,0)、(5,3)、(7,1)和(2,2)。无论数组是多少维的，花式索引总是一维的
print(arr[[1, 5, 7, 2], [0, 3, 1, 2]])
print()
print(arr[[1, 5, 7, 2]])
print()
print(arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]])
print()
# 记住，花式索引跟切片不一样，它总是将数据复制到新数组中

# 转置是重塑的一种特殊形式，它返回的是源数据的视图（不会进行任何复制操作）。
# 数组不仅有transpose方法，还有一个特殊的T属性
arr = np.arange(15).reshape((3, 5))
print(arr)
print(arr.T)    # 矩阵转置
print()

arr = np.random.randn(6, 3)
print(arr)
print()
# 比如利用np.dot计算矩阵内积,其实就是两个矩阵相乘
print(np.dot(arr.T, arr))
print()

# 对于高维数组，transpose需要得到一个由轴编号组成的元组才能对这些轴进行转置（比较费脑子）
arr = np.arange(16).reshape((2, 2, 4))
print(arr)
# 这里，第一个轴被换成了第二个，第二个轴被换成了第一个，最后一个轴不变
print(arr.transpose((1, 0, 2)))
print()
# ndarray还有一个swapaxes方法，它需要接受一对轴编号,swapaxes也是返回源数据的视图（不会进行任何复制操作）
print(arr.swapaxes(1, 2))
