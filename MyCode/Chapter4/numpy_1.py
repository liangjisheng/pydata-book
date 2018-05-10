# -*- coding:utf-8 -*-
"""
@project = 0411-2
@file = numpy_1
@author = Liangjisheng
@create_time = 2018/4/14 0014 上午 10:11
"""
import numpy as np
data = np.random.randn(2, 3)
print(data)
print(data * 10)
print(data + data)

# ndarray是一个通用的同构数据多维容器，也就是说，所有元素必须是相同类型
# 每个数组都有一个shape(一个表示各维度大小的元组)和一个dtype(一个用于说明
# 数组数据类型的对象)
print(data.shape)
print(data.data)
print(data.dtype)
print()

data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)
print(arr1)
print(arr1.nbytes)

# 等长列表组成的列表将会被转换为一个多维数组
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
print(arr2)
print(arr2.ndim)
print(arr2.nbytes)
print(arr2.shape)
print(arr2.dtype)
print()

print(np.zeros(10))
print(np.zeros(10).dtype)
print(np.zeros((3, 6)))
print(np.empty((2, 3, 2)))
print(np.arange(15))
print()

# 可以通过ndarray的astype方法明确地将一个数组从一个dtype转换成另一个dtype
# int32 to float64
arr = np.array([1, 2, 3, 4, 5])
print(arr.dtype)
float_arr = arr.astype(np.float64)
print(float_arr.dtype)
# float64 to int32,小数部分将会被截取删除
arr = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
print(arr)
print(arr.astype(np.int32))

# 如果某字符串数组表示的全是数字，也可以用astype将其转换为数值类型
numeric_strings = np.array(['1.25', '-9.6', '42'], dtype=np.string_)
print(numeric_strings.astype(float))
print()

int_array = np.arange(10)
calibers = np.array([.22, .270, .357, .380, .44, .50], dtype=np.float64)
print(int_array.astype(calibers.dtype))
empty_uint32 = np.empty(8, dtype='u4')
print(empty_uint32)
