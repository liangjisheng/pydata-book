# -*- coding:utf-8 -*-
"""
@project = 0411-2
@file = numpy_9
@author = Liangjisheng
@create_time = 2018/4/14 0014 下午 16:23
"""
import matplotlib.pyplot as plt
import random
# 我们通过模拟随机漫步来说明如何运用数组运算。先来看一个简单的随机漫步的例子：
# 从0开始，步长1和－1出现的概率相等，下面是一个通过内置的random模块以纯Python的
# 方式实现1000步的随机漫步
position = 0
walk = [position]
steps = 1000
for i in range(steps):
    step = 1 if random.randint(0, 1) else -1
    position += step
    walk.append(position)

plt.plot(walk[:100])
plt.show()
