# -*- coding:utf-8 -*-
"""
@project = 0424-1
@file = 8_2
@author = Liangjisheng
@create_time = 2018/4/24 0024 下午 19:38
"""
import pandas as pd
import numpy as np
# 人们经常想要将DataFrame的一个或多个列当做行索引来用，或者可能希望将行索引变成
# DataFrame的列。以下面这个DataFrame为例
frame = pd.DataFrame({'a': range(7), 'b': range(7, 0, -1),
                      'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two'],
                      'd': [0, 1, 2, 0, 1, 2, 3]})
print(frame)
# DataFrame的set_index函数会将其一个或多个列转换为行索引，并创建一个新的DataFrame
frame2 = frame.set_index(['c', 'd'])
print(frame2)
# 默认情况下，那些列会从DataFrame中移除，但也可以将其保留下来
print(frame.set_index(['c', 'd'], drop=False))
# reset_index的功能跟set_index刚好相反，层次化索引的级别会被转移到列里面
print(frame2.reset_index())
