# -*- coding:utf-8 -*-
"""
@project = 0411-2
@file = numpy_2
@author = Liangjisheng
@create_time = 2018/4/14 0014 上午 10:54
"""
import numpy as np

# 大小相等的数组之间的任何算术运算都会将运算应用到元素级
arr = np.array([[1., 2., 3.], [4., 5., 6.]])
print(arr.dtype)
print(arr)
print(arr * arr)
print(arr - arr)

# 数组与标量的算术运算会将标量值传播到各个元素
print(1 / arr)
print(arr ** 0.5)

# 大小相同的数组之间的比较会生成布尔值数组
arr2 = np.array([[0., 4., 1.], [7., 2., 12.]])
print(arr2)
print(arr2 > arr)
print()
# 不同大小的数组之间的运算叫做广播（broadcasting）

# numpy基本的索引和切片
arr = np.arange(10)
print(arr)
print(arr[5])
print(arr[5:8])
# 当你将一个标量值赋值给一个切片时（如arr[5:8]=12），该值会自动传播
# （也就说后面将会讲到的“广播”）到整个选区
arr[5:8] = 12
print(arr)

# 跟列表最重要的区别在于，数组切片是原始数组的视图。这意味着数据不会被复制，
# 视图上的任何修改都会直接反映到源数组上
# 先创建一个arr的切片,修改arr_slice中的值，变动也会体现在原始数组arr中
arr_slice = arr[5:8]
print(arr_slice)
arr_slice[1] = 12345
print(arr)

arr_slice[:] = 64
print(arr)
print()
# 如果你想要得到的是ndarray切片的一份副本而非视图，就需要明确地进行复制操作，例如arr[5:8].copy()

# 对于高维度数组，能做的事情更多。在一个二维数组中，各索引位置上的元素不再是标量而是一维数组
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d)
print(arr2d[2])
# 可以对各个元素进行递归访问，但这样需要做的事情有点多。你可以传入一个以逗号隔开的
# 索引列表来选取单个元素。也就是说，下面两种方式是等价的
print(arr2d[0][2])
print(arr2d[0, 2])
print()

# 在多维数组中，如果省略了后面的索引，则返回对象会是一个维度低一点的ndarray（它含有高一级维度上的所有数据）
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3d)
print(arr3d[0])
# 标量值和数组都可以被赋值给arr3d[0]
old_values = arr3d[0].copy()
arr3d[0] = 42
print(arr3d)
arr3d[0] = old_values
print(arr3d)
print()

# 相似的，arr3d[1,0]可以访问索引以(1,0)开头的那些值（以一维数组的形式返回）
print(arr3d[1, 0])
x = arr3d[1]
print(x)
print(x[0])
# 注意，在上面所有这些选取数组子集的例子中，返回的数组都是视图
