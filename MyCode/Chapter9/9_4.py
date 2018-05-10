# -*- coding:utf-8 -*-
"""
@project = 0426-1
@file = 9_4
@author = Liangjisheng
@create_time = 2018/4/26 0026 下午 20:05
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# Series和DataFrame都有一个用于生成各类图表的plot方法。默认情况下，它们所生成的是线型图
s = pd.Series(np.random.randn(10).cumsum(), index=np.arange(0, 100, 10))
fig = plt.figure()
fig.add_subplot(1, 1, 1)
# 该Series对象的索引会被传给matplotlib，并用以绘制X轴。可以通过use_index=False禁用该功能
# X轴的刻度和界限可以通过xticks和xlim选项进行调节，Y轴就用yticks和ylim
fig.add_axes(s.plot())
fig.show()

# pandas的大部分绘图方法都有一个可选的ax参数，它可以是一个matplotlib的subplot对象
# 这使你能够在网格布局中更为灵活地处理subplot的位置
# DataFrame的plot方法会在一个subplot中为各列绘制一条线，并自动创建图例
df = pd.DataFrame(np.random.randn(10, 4).cumsum(0),
                  columns=['A', 'B', 'C', 'D'],
                  index=np.arange(0, 100, 10))
print(df)
ax = plt.plot(df)
print(type(ax))
print(ax)
plt.show()

fig, axes = plt.subplots(1, 1)
df.plot(ax=axes, color='k', alpha=0.7)
fig.show()

# plot.bar()和plot.barh()分别绘制水平和垂直的柱状图。这时，Series和DataFrame
# 的索引将会被用作X（bar）或Y（barh）刻度
fig, axes = plt.subplots(2, 1)
data = pd.Series(np.random.randn(16), index=list('abcdefghijklmnop'))
data.plot.bar(ax=axes[0], color='k', alpha=0.7)
data.plot.barh(ax=axes[1], color='k', alpha=0.7)
fig.show()

# 对于DataFrame，柱状图会将每一行的值分为一组，并排显示
df = pd.DataFrame(np.random.randn(6, 4),
                  index=['one', 'two', 'three', 'four', 'five', 'six'],
                  columns=pd.Index(['A', 'B', 'C', 'D'], name='Genus'))
print(df)

# DataFrame各列的名称"Genus"被用作了图例的标题
fig, axes = plt.subplots(1, 1)
df.plot.bar(ax=axes)
fig.show()

# 设置stacked=True即可为DataFrame生成堆积柱状图，这样每行的值就会被堆积在一起
fig, axes = plt.subplots(1, 1)
df = abs(df)
df.plot.barh(ax=axes, stacked=True, alpha=0.5)
fig.show()
