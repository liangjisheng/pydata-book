# -*- coding:utf-8 -*-
"""
@project = 0411-2
@file = numpy_8
@author = Liangjisheng
@create_time = 2018/4/14 0014 下午 15:36
"""
# NumPy能够读写磁盘上的文本数据或二进制数据。这一小节只讨论NumPy的内置二进制格式，
# 因为更多的用户会使用pandas或其它工具加载文本或表格数据
# np.save和np.load是读写磁盘数组数据的两个主要函数。默认情况下，
# 数组是以未压缩的原始二进制格式保存在扩展名为.npy的文件中的
import numpy as np
arr = np.arange(10)
np.save('some_array', arr)
# 如果文件路径末尾没有扩展名.npy，则该扩展名会被自动加上
# 然后就可以通过np.load读取磁盘上的数组：
print(np.load('some_array.npy'))
# 通过np.savez可以将多个数组保存到一个未压缩文件中，将数组以关键字参数的形式传入即可
np.savez('array_archive.npz', a=arr, b=arr)
# 加载.npz文件时，你会得到一个类似字典的对象，该对象会对各个数组进行延迟加载
arch = np.load('array_archive.npz')
print(arch['a'])
print(arch['b'])

# NumPy提供了一个用于矩阵乘法的dot函数（既是一个数组方法也是numpy命名空间中的一个函数
x = np.array([[1., 2., 3.], [4., 5., 6.]])
y = np.array([[6., 23.], [-1, 7], [8, 9]])
print(x)
print(y)
print(x.dot(y))
# x.dot(y)等价于np.dot(x, y)：
print(np.dot(x, y))

# 一个二维数组跟一个大小合适的一维数组的矩阵点积运算之后将会得到一个一维数组
print(np.dot(x, np.ones(3)))
# @符（类似Python 3.5）也可以用作中缀运算符，进行矩阵乘法
print(x @ np.ones(3))

# numpy.linalg中有一组标准的矩阵分解运算以及诸如求逆和行列式之类的东西。
# 它们跟MATLAB和R等语言所使用的是相同的行业标准线性代数库，如BLAS、LAPACK、
# Intel MKL（Math Kernel Library，可能有，取决于你的NumPy版本）
from numpy.linalg import inv, qr
X = np.random.randn(5, 5)
mat = X.T.dot(X)
print(mat)
print()
print(inv(mat))
print()
print(mat.dot(inv(mat)))
q, r = qr(mat)
print(q)
print()
print(r)
print()

# numpy.random模块对Python内置的random进行了补充，增加了一些用于高效生成多种
# 概率分布的样本值的函数。例如，你可以用normal来得到一个标准正态分布的4×4样本数组
samples = np.random.normal(size=(4, 4))
print(samples)

# 可以用NumPy的np.random.seed更改随机数生成种子
# np.random.seed(1234)
# 改变种子后，每次生成的随机数都是一样的
print(np.random.normal(size=(2, 2)))

# numpy.random的数据生成函数使用了全局的随机种子。要避免全局状态，
# 你可以使用numpy.random.RandomState，创建一个与其它隔离的随机数生成器
rng = np.random.RandomState(1234)
print(rng.randn(10))
