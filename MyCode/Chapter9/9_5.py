# -*- coding:utf-8 -*-
"""
@project = 0426-1
@file = 9_5
@author = Liangjisheng
@create_time = 2018/4/27 0027 下午 19:37
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

party_counts = pd.DataFrame([[1, 16, 1, 1, 0, 0], [2, 53, 18, 13, 1, 0],
                             [0, 39, 15, 18, 3, 1], [1, 48, 4, 5, 1, 3]],
                            index=pd.Index(['Fri', 'Sat', 'Sun', 'Thur'], name='day'),
                            columns=pd.Index(np.arange(6) + 1, name='size'))
print(party_counts)
party_counts = party_counts.loc[:, 2:5]
print(party_counts)
# 然后进行规格化，使得各行的和为1，并生成图表
print(party_counts.sum(1))
party_pcts = party_counts.div(party_counts.sum(1), axis=0)
print(party_pcts)

fig, axes = plt.subplots(1, 1)
party_pcts.plot.bar(ax=axes)
fig.show()

# 直方图（histogram）是一种可以对值频率进行离散化显示的柱状图。数据点被拆分到离散的、
# 间隔均匀的面元中，绘制的是各面元中数据点的数量
data = pd.Series(np.random.randn(1000))
print(data.head())
fig, axes = plt.subplots(1, 1)
# 等分成100份
data.plot.hist(ax=axes, bins=100)
fig.show()

# 与此相关的一种图表类型是密度图，它是通过计算“可能会产生观测数据的连续概率分布的估计”
# 而产生的。一般的过程是将该分布近似为一组核（即诸如正态分布之类的较为简单的分布）
# 因此，密度图也被称作KDE（Kernel Density Estimate，核密度估计）图
# 使用plot.kde和标准混合正态分布估计即可生成一张密度图
fig, axes = plt.subplots(1, 1)
data.plot.density(ax=axes)
fig.show()

# seaborn的distplot方法绘制直方图和密度图更加简单，还可以同时画出直方图和连续密度估计图
# 作为例子，考虑一个双峰分布，由两个不同的标准正态分布组成
comp1 = np.random.normal(0, 1, size=200)
comp2 = np.random.normal(10, 2, size=200)
# print([comp1, comp2])
values = pd.Series(np.concatenate([comp1, comp2]))
# print(values.head())
fig, axes = plt.subplots(1, 1)
sns.distplot(values, bins=100, color='k', ax=axes)
fig.show()
