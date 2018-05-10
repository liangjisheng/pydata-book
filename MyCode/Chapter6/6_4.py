# -*- coding:utf-8 -*-
"""
@project = 0422-1
@file = 6_4
@author = Liangjisheng
@create_time = 2018/4/22 0022 上午 11:23
"""
# 实现数据的高效二进制格式存储最简单的办法之一是使用Python内置的pickle序列化
# pandas对象都有一个用于将数据以pickle格式保存到磁盘上的to_pickle方法
import pandas as pd
import numpy as np
frame = pd.read_csv('ex1.csv')
print(frame)
frame.to_pickle('frame_pickle')
# 你可以通过pickle直接读取被pickle化的数据，或是使用更为方便的pandas.read_pickle
print(pd.read_pickle('frame_pickle'))
# 注意：pickle仅建议用于短期存储格式。其原因是很难保证该格式永远是稳定的；
# 今天pickle的对象可能无法被后续版本的库unpickle出来。虽然我尽力保证这种事情不会发生
# 在pandas中，但是今后的某个时候说不定还是得“打破”该pickle格式

# HDF5是一种存储大规模科学数组数据的非常好的文件格式
# HDF5中的HDF指的是层次型数据格式（hierarchical data format）。每个HDF5文件都含有一个
# 文件系统式的节点结构，它使你能够存储多个数据集并支持元数据。与其他简单格式相比，
# HDF5支持多种压缩器的即时压缩，还能更高效地存储重复模式数据。对于那些非常大的无法
# 直接放入内存的数据集，HDF5就是不错的选择，因为它可以高效地分块读写
frame = pd.DataFrame({'a': np.random.randn(100)})
print(frame.head())
store = pd.HDFStore('mydata.h5')
store['obj1'] = frame
store['obj1_col'] = frame['a']
print(store)
print(type(store))
# HDF5文件中的对象可以通过与字典一样的API进行获取：
print(store['obj1'])
print(store['obj1_col'])

# HDFStore支持两种存储模式，'fixed'和'table'。后者通常会更慢，但是支持使用特殊语法进行查询操作
# put是store['obj2'] = frame方法的显示版本，允许我们设置其它的选项，比如格式
store.put('obj2', frame, format='table')
print(store.select('obj2', where=['index >= 10 and index <= 15']))

# 使用期间不能关闭文件
store.close()

# pandas.read_hdf函数可以快捷使用这些工具
frame.to_hdf('mydata.h5', 'obj3', format='table')
print(pd.read_hdf('mydata.h5', 'obj3', where=['index < 5']))
