# -*- coding:utf-8 -*-
"""
@project = 0427-1
@file = 10_2
@author = Liangjisheng
@create_time = 2018/4/28 0028 下午 15:03
"""
import pandas as pd
import numpy as np
# 除数组以外，分组信息还可以其他形式存在
people = pd.DataFrame(np.random.randn(5, 5),
                      columns=['a', 'b', 'c', 'd', 'e'],
                      index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis'])
print(people)
people.iloc[2:3, [1, 2]] = np.nan
print(people)
# 现在，假设已知列的分组关系，并希望根据分组计算列的和
mapping = {'a': 'red', 'b': 'red', 'c': 'blue', 'd': 'blue', 'e': 'red', 'f': 'orange'}
# 现在，你可以将这个字典传给groupby，来构造数组，但我们可以直接传递字典
# （我包含了键“f”来强调，存在未使用的分组键是可以的）
by_column = people.groupby(mapping, axis=1)
print(by_column)
print(list(by_column))
for name, group in list(by_column):
    print(type(name))
    print(name)
    print(type(group))
    print(group)
    print(type(group.sum(axis=1)))
    print(group.sum(axis=1))
print()

print(type(by_column.sum()))
print(by_column.sum())

# Series也有同样的功能，它可以被看做一个固定大小的映射
map_series = pd.Series(mapping)
print(map_series)
print(people.groupby(map_series, axis=1).count())

# 比起使用字典或Series，使用Python函数是一种更原生的方法定义分组映射。任何被当做分组键的函数
# 都会在各个索引值上被调用一次，其返回值就会被用作分组名称。具体点说，以上一小节的示例
# DataFrame为例，其索引值为人的名字。你可以计算一个字符串长度的数组，更简单的方法是传入len函数
print(people)
print(people.groupby(len).sum())

# 将函数跟数组、列表、字典、Series混合使用也不是问题，因为任何东西在内部都会被转换为数组
key_list = ['one', 'one', 'one', 'two', 'two']
print(key_list)
print(list(people.index))
key_len = list(map(len, list(people.index)))
print(key_len)
df_key = pd.DataFrame([key_len, key_list])
print(df_key)
print(df_key.T)

# 层次化索引数据集最方便的地方就在于它能够根据轴索引的一个级别进行聚合
columns = pd.MultiIndex.from_arrays([['US', 'US', 'US', 'JP', 'JP'],
                                     [1, 3, 5, 1, 3]],
                                    names=['cty', 'tenor'])
print(columns)
hier_df = pd.DataFrame(np.random.randn(4, 5), columns=columns)
print(hier_df)
# 要根据级别分组，使用level关键字传递级别序号或名字
print(hier_df.groupby(level='cty', axis=1).count())
