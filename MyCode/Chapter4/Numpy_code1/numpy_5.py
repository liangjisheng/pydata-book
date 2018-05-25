# -*- coding:utf-8 -*-
"""
@project = 0411-2
@file = numpy_5
@author = Liangjisheng
@create_time = 2018/4/14 0014 下午 14:23
"""
# 通用函数（即ufunc）是一种对ndarray中的数据执行元素级运算的函数。
# 你可以将其看做简单函数（接受一个或多个标量值，并产生一个或多个标量值）的矢量化包装器
import numpy as np
arr = np.arange(10)
print(arr)
print(np.sqrt(arr))
print(np.exp(arr))

x = np.random.randn(8)
y = np.random.randn(8)
print(x)
print(y)
print(np.maximum(x, y))
print()

# 虽然并不常见，但有些ufunc的确可以返回多个数组。modf就是一个例子，
# 它是Python内置函数divmod的矢量化版本，它会返回浮点数数组的小数和整数部分
arr = np.random.randn(7) * 5
print(arr)
remainder, whole_part = np.modf(arr)
print(remainder)
print(whole_part)

# Ufuncs可以接受一个out可选参数，这样就能在数组原地进行操作
arr[arr < 0] = 0
print(np.sqrt(arr))

# NumPy数组使你可以将许多种数据处理任务表述为简洁的数组表达式（否则需要编写循环）
# 用数组表达式代替循环的做法，通常被称为矢量化。一般来说，矢量化数组运算要比等价
# 的纯Python方式快上一两个数量级（甚至更多），尤其是各种数值计算

# 假设我们想要在一组值（网格型）上计算函数sqrt(x^2+y^2)
# np.meshgrid函数接受两个一维数组，并产生两个二维矩阵（对应于两个数组中所有的(x,y)对）
points = np.arange(-5, 5, 0.01)
xs, ys = np.meshgrid(points, points)
print(xs)
print(xs.dtype)
print(xs.nbytes)
print(ys)
# 现在，对该函数的求值运算就好办了，把这两个数组当做两个浮点数那样编写表达式即可
z = np.sqrt(xs ** 2 + ys ** 2)
print(z)
print(len(z))
print(len(z[0]))

import matplotlib.pyplot as plt
plt.imshow(z, cmap=plt.cm.gray)
plt.colorbar()
plt.title('Image plot of $\sqrt{x^2 + y^2}$ for a grid of values')
plt.show()

