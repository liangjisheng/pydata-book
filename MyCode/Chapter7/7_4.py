# -*- coding:utf-8 -*-
"""
@project = 0422-2
@file = 7_4
@author = Liangjisheng
@create_time = 2018/4/22 0022 下午 17:22
"""
# 过滤或变换异常值（outlier）在很大程度上就是运用数组运算
import pandas as pd
import numpy as np
data = pd.DataFrame(np.random.randn(1000, 4))
print(data.describe())
# 假设你想要找出某列中绝对值大小超过3的值
col = data[2]
print(col[np.abs(col) > 3])
# 要选出全部含有“超过3或－3的值”的行，你可以在布尔型DataFrame中使用any方法
print(np.abs(data) > 3)
print((np.abs(data) > 3).any(1))
print(data[(np.abs(data) > 3).any(1)])
# 根据这些条件，就可以对值进行设置。下面的代码可以将值限制在区间－3到3以内
# 根据数据的值是正还是负，np.sign(data)可以生成1和-1
data[np.abs(data) > 3] = np.sign(data) * 3
print(data.describe())
print(np.sign(data).head())
print()

# 排列和随机采样
# 利用numpy.random.permutation函数可以轻松实现对Series或DataFrame的列的排列工作
# （permuting，随机重排序）。通过需要排列的轴的长度调用permutation，可产生一个表示新顺序的整数数组
df = pd.DataFrame(np.arange(5 * 4).reshape(5, 4))
sampler = np.random.permutation(5)
print(sampler)
# 然后就可以在基于iloc的索引操作或take函数中使用该数组了
print(df)
print(df.take(sampler))
# 如果不想用替换的方式选取随机子集，可以在Series和DataFrame上使用sample方法
print(df.sample(n=3))
# 要通过替换的方式产生样本（允许重复选择），可以传递replace=True到sample
choices = pd.Series([5, 7, -1, 6, 4])
draws = choices.sample(n=10, replace=True)
print(draws)
