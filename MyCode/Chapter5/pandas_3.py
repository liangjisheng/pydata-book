# -*- coding:utf-8 -*-
"""
@project = 0416-1
@file = pandas_3
@author = Liangjisheng
@create_time = 2018/4/16 0016 下午 20:12
"""
import pandas as pd
import numpy as np
# 另一种常见的数据形式是嵌套字典, 如果嵌套字典传给DataFrame，
# pandas就会被解释为：外层字典的键作为列，内层键则作为行索引
pop = {'Nevada': {2001: 2.4, 2002: 2.9}, 'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame3 = pd.DataFrame(pop)
print(frame3)
# 你也可以使用类似NumPy数组的方法，对DataFrame进行转置（交换行和列）
print(frame3.T)

# 内层字典的键会被合并、排序以形成最终的索引。如果明确指定了索引，则不会这样
print(pd.DataFrame(pop, index=[2001, 2002, 2003]))

# 由Series组成的字典差不多也是一样的用法：
pdata = {'Ohio': frame3['Ohio'][:-1],
         'Nevada': frame3['Nevada'][:2]}
print(pd.DataFrame(pdata))

# 如果设置了DataFrame的index和columns的name属性，则这些信息也会被显示出来
frame3.index.name = 'year'
frame3.columns.name = 'state'
print(frame3)
# values属性会以二维ndarray的形式返回DataFrame中的数据
print(frame3.values)
print(frame3.values.dtype)
print()

# pandas的索引对象负责管理轴标签和其他元数据（比如轴名称等）
# 构建Series或DataFrame时，所用到的任何数组或其他序列的标签都会被转换成一个Index对象
obj = pd.Series(range(3), index=['a', 'b', 'c'])
index = obj.index
print(index)
print(index[1:])

# Index对象是不可变的，因此用户不能对其进行修改
# 不可变可以使Index对象在多个数据结构之间安全共享
labels = pd.Index(np.arange(3))
print(labels)
obj2 = pd.Series([1.5, -2.5, 0], index=labels)
print(obj2)
print(obj2.index is labels)

print(frame3.columns)
print('Ohio' in frame3.columns)
print(2003 in frame3.index)

# 与python的集合不同，pandas的Index可以包含重复的标签
dup_labels = pd.Index(['foo', 'foo', 'bar', 'bar'])
print(dup_labels)
