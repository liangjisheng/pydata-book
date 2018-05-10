# -*- coding:utf-8 -*-
"""
@project = 0416-1
@file = pandas_2
@author = Liangjisheng
@create_time = 2018/4/16 0016 下午 19:52
"""
import pandas as pd
import numpy as np
# 结果DataFrame会自动加上索引（跟Series一样），且全部列会被有序排列
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)
print(frame)
# 对于特别大的DataFrame，head方法会选取前五行
print(frame.head())

# 如果指定了列序列，则DataFrame的列就会按照指定顺序进行排列
print(pd.DataFrame(data, columns=['year', 'state', 'pop']))

# 如果传入的列在数据中找不到，就会在结果中产生缺失值
frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                      index=['one', 'two', 'three', 'four', 'five', 'six'])
print(frame2)

# 通过类似字典标记的方式或属性的方式，可以将DataFrame的列获取为一个Series
# IPython提供了类似属性的访问（即frame2.year）和tab补全。
# frame2[column]适用于任何列的名，但是frame2.column只有在列名是一个合理的
# Python变量名时才适用。
print(frame2['state'])
print(frame2.year)
print(frame2['pop'])
print(frame2['debt'])
print()

# 行也可以通过位置或名称的方式进行获取，比如用loc属性
print(frame2.loc['three'])
# 列可以通过赋值的方式进行修改。例如，我们可以给那个空的"debt"列赋上一个标量值或一组值
frame2['debt'] = 16.5
print(frame2)
# 将列表或数组赋值给某个列时，其长度必须跟DataFrame的长度相匹配
frame2['debt'] = np.arange(6.)
print(frame2)
# 如果赋值的是一个Series，就会精确匹配DataFrame的索引，所有的空位都将被填上缺失值
val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
frame2['debt'] = val
print(frame2)

# 为不存在的列赋值会创建出一个新列。关键字del用于删除列
# 作为del的例子，我先添加一个新的布尔值的列，state是否为'Ohio'
# 注意：不能用frame2.eastern创建新的列
frame2['eastern'] = frame2.state == 'Ohio'
print(frame2)
print(frame2.columns)
del frame2['eastern']
print(frame2.columns)
