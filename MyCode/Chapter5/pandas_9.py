# -*- coding:utf-8 -*-
"""
@project = 0416-1
@file = pandas_9
@author = Liangjisheng
@create_time = 2018/4/18 0018 下午 19:38
"""
import pandas as pd
import numpy as np
# 接下来介绍Series和DataFrame的rank方法。默认情况下，
# rank是通过“为各组分配一个平均排名”的方式破坏平级关系的
obj = pd.Series([7, -5, 7, 4, 2, 0, 4])
print(obj)
print(obj.rank())
# 也可以根据值在原数据中出现的顺序给出排名：
# 这里，条目0和2没有使用平均排名6.5，它们被设成了6和7，因为数据中标签0位于标签2的前面
print(obj.rank(method='first'))
# 你也可以按降序进行排名
print(obj.rank(method='max', ascending=False))
print(obj.rank(method='min'))

# DataFrame可以在行或列上计算排名：
frame = pd.DataFrame({'b': [4.3, 7, -3, 2], 'a': [0, 1, 0, 1], 'c': [-2, 5, 8, -2.5]})
print(frame)
print(frame.rank(axis='columns'))

# 直到目前为止，我所介绍的所有范例都有着唯一的轴标签（索引值）。虽然许多pandas函数
# （如reindex）都要求标签唯一，但这并不是强制性的。我们来看看下面这个简单的带有
# 重复索引值的Series
obj = pd.Series(range(5), index=['a', 'a', 'b', 'b', 'c'])
print(obj)
# 索引的is_unique属性可以告诉你它的值是否是唯一的：
print(obj.index)
print(obj.index.is_unique)
# 对于带有重复值的索引，数据选取的行为将会有些不同。如果某个索引对应多个值，
# 则返回一个Series；而对应单个值的，则返回一个标量值
print(obj['a'])
print(obj['c'])
# 对DataFrame的行进行索引时也是如此：
df = pd.DataFrame(np.random.randn(4, 3), index=['a', 'a', 'b', 'b'])
print(df)
print(df.loc['b'])
