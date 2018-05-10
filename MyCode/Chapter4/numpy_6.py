# -*- coding:utf-8 -*-
"""
@project = 0411-2
@file = numpy_6
@author = Liangjisheng
@create_time = 2018/4/14 0014 下午 14:59
"""
# numpy.where函数是三元表达式x if condition else y的矢量化版本
# 假设我们有一个布尔数组和两个值数组
import numpy as np
xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])

# 假设我们想要根据cond中的值选取xarr和yarr的值：当cond中的值为True时，
# 选取xarr的值，否则从yarr中选取。列表推导式的写法应该如下所示
result = [(x if c else y) for x, y, c in zip(xarr, yarr, cond)]
print(result)
# 第一，它对大数组的处理速度不是很快（因为所有工作都是由纯Python完成的）
# 第二，无法用于多维数组。若使用np.where，则可以将该功能写得非常简洁
result = np.where(cond, xarr, yarr)
print(result)

# np.where的第二个和第三个参数不必是数组，它们都可以是标量值。在数据分析工作中，
# where通常用于根据另一个数组而产生一个新的数组。假设有一个由随机数据组成的矩阵，
# 你希望将所有正值替换为2，将所有负值替换为－2。若利用np.where，则会非常简单
arr = np.random.randn(4, 4)
print(arr)
print(arr > 0)
print(np.where(arr > 0, 2, -2))
# 可用常数2替换arr中所有正的值
print(np.where(arr > 0, 2, arr))

# 可以通过数组上的一组数学函数对整个数组或某个轴向的数据进行统计计算。sum、mean以及
# 标准差std等聚合计算(aggregation，通常叫做约简(reduction))
# 既可以当做数组的实例方法调用，也可以当做顶级NumPy函数使用
# 这里，我生成了一些正态分布随机数据，然后做了聚类统计
arr = np.random.randn(5, 4)
print(arr)
print(arr.mean())
print(np.mean(arr))
print(arr.sum())
print()
# mean和sum这类的函数可以接受一个axis选项参数，用于计算该轴向上的统计值，
# 最终结果是一个少一维的数组
print(arr.mean(axis=1))     # 计算行的平均值
print(arr.sum(axis=0))      # 计算每列的和
print()

# 其他如cumsum和cumprod之类的方法则不聚合，而是产生一个由中间结果组成的数组
arr = np.arange(8)
print(arr.cumsum())
# 在多维数组中，累加函数（如cumsum）返回的是同样大小的数组，但是会根据每个
# 低维的切片沿着标记轴计算部分聚类
arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print(arr)
print(arr.cumsum(axis=0))
print(arr.cumprod(axis=1))
print()

# 在上面这些方法中，布尔值会被强制转换为1（True）和0（False）
# 因此，sum经常被用来对布尔型数组中的True值计数
arr = np.random.randn(100)
print((arr > 0).sum())
# 另外还有两个方法any和all，它们对布尔型数组非常有用
# any用于测试数组中是否存在一个或多个True，而all则检查数组中所有值是否都是True
# 这两个方法也能用于非布尔型数组，所有非0元素将会被当做True
bools = np.array([False, False, True, False])
print(bools.any())
print(bools.all())
