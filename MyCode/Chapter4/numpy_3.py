# -*- coding:utf-8 -*-
"""
@project = 0411-2
@file = numpy_3
@author = Liangjisheng
@create_time = 2018/4/14 0014 上午 11:14
"""
import numpy as np
arr = np.arange(10)
arr[5:8] = 64
print(arr)
print(arr[1:6])

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d)
# 可以看出，它是沿着第0轴（即第一个轴）切片的。也就是说，
# 切片是沿着一个轴向选取元素的。表达式arr2d[:2]可以被认为是“选取arr2d的前两行”
print(arr2d[:2])
# 你可以一次传入多个切片，就像传入多个索引那样
print(arr2d[:2, 1:])
print(arr2d[1, :2])
print(arr2d[:2, 2])
print()
# 注意，“只有冒号”表示选取整个轴，因此你可以像下面这样只对高维轴进行切片
print(arr2d[:, :1])

# 自然，对切片表达式的赋值操作也会被扩散到整个选区
arr2d[:2, 1:] = 0
print(arr2d)
print()

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = np.random.rand(7, 4)     # 生成正态分布随机数
print(names)
print(data)
# 假设每个名字都对应data数组中的一行，而我们想要选出对应于名字"Bob"的所有行。
# 跟算术运算一样，数组的比较运算（如==）也是矢量化的。因此，对names和字符串"Bob"
# 的比较运算将会产生一个布尔型数组
sel = names == 'Bob'
print(sel)
# 这个布尔型数组可用于数组索引：
print(data[sel])
print(data['Bob' == names, 2:])
print(data['Bob' == names, 3])
print()

# 要选择除"Bob"以外的其他值，既可以使用不等于符号（!=），也可以通过~对条件进行否定
sel = names != 'Bob'
print(data[sel])
print()
print(data[~sel])
print()
print(data[names == 'Bob'])
print()
print(data[~(names == 'Bob')])
print()

# 选取这三个名字中的两个需要组合应用多个布尔条件，使用&（和）、|（或）
# 之类的布尔算术运算符即可
mask = (names == 'Bob') | (names == 'Will')
print(mask)
print(data[mask])
print()
# 通过布尔型索引选取数组中的数据，将总是创建数据的副本，即使返回一模一样的数组也是如此
# Python关键字and和or在布尔型数组中无效。要使用&与|

# 通过布尔型数组设置值是一种经常用到的手段。为了将data中的所有负值都设置为0，我们只需
data[data < 0] = 0
print(data)

# 通过一维布尔数组设置整行或列的值也很简单
data[names != 'Joe'] = 7
print(data)
