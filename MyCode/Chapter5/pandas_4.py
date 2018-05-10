# -*- coding:utf-8 -*-
"""
@project = 0416-1
@file = pandas_4
@author = Liangjisheng
@create_time = 2018/4/16 0016 下午 20:36
"""
import pandas as pd
import numpy as np
obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
print(obj)
# 用该Series的reindex将会根据新索引进行重排。如果某个索引值当前不存在，就引入缺失值
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
print(obj2)

# 对于时间序列这样的有序数据，重新索引时可能需要做一些插值处理
# method选项即可达到此目的，例如，使用ffill可以实现前向值填充
obj3 = pd.Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
print(obj3)
print(obj3.reindex(range(6), method='ffill'))

# 借助DataFrame，reindex可以修改（行）索引和列。只传递一个序列时，会重新索引结果的行
frame = pd.DataFrame(np.arange(9).reshape((3, 3)), index=['a', 'c', 'd'],
                     columns=['Ohio', 'Texas', 'California'])
print(frame)
frame2 = frame.reindex(['a', 'b', 'c', 'd'])
print(frame2)
# 列可以用columns关键字重新索引
states = ['Texas', 'Utah', 'California']
print(frame.reindex(columns=states))

# 丢弃指定轴上的一个或多个项很简单，只要有一个索引数组或列表即可
# 由于需要执行一些数据整理和集合逻辑，所以drop方法返回的是一个在指定轴上
# 删除了指定值的新对象
obj = pd.Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
print(obj)
new_obj = obj.drop('c')
print(new_obj)
print(obj.drop(['d', 'c']))
print()

# 对于DataFrame，可以删除任意轴上的索引值
data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
print(data)
# 用标签序列调用drop会从行标签（axis 0）删除值
print(data.drop(['Colorado', 'Ohio']))
# 通过传递axis=1或axis='columns'可以删除列的值
print(data.drop('two', axis=1))
print(data.drop(['two', 'four'], axis=1))

# 许多函数，如drop，会修改Series或DataFrame的大小或形状
# 可以就地修改对象，不会返回新的对象
# 小心使用inplace，它会销毁所有被删除的数据
obj.drop('c', inplace=True)
print(obj)
