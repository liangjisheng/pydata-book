# -*- coding:utf-8 -*-
"""
@project = 0422-2
@file = 7_2
@author = Liangjisheng
@create_time = 2018/4/22 0022 下午 16:06
"""
import pandas as pd
import numpy as np
data = pd.DataFrame({'k1': ['one', 'two'] * 3 + ['two'],
                     'k2': [1, 1, 2, 3, 3, 4, 4]})
print(data)
# DataFrame的duplicated方法返回一个布尔型Series，表示各行是否是重复行（前面出现过的行）
print(data.duplicated())
# 还有一个与此相关的drop_duplicates方法，它会返回一个DataFrame
print(data.drop_duplicates())

# 上面两个方法默认会判断全部列，你也可以指定部分列进行重复项判断。
# 假设我们还有一列值，且只希望根据k1列过滤重复项
print(data.shape)
data['v1'] = range(data.shape[0])
print(data)
print(data.duplicated(['k1']))
print(data.drop_duplicates(['k1']))

# duplicated和drop_duplicates默认保留的是第一个出现的值组合。传入keep='last'则保留最后一个
print(data.drop_duplicates(['k1', 'k2'], keep='last'))
print()

# 利用函数或映射进行数据转换
# 对于许多数据集，你可能希望根据数组、Series或DataFrame列中的值来实现转换工作
data = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon', 'Pastrami', 'corned beef', 'Bacon',
                              'pastrami', 'honey ham', 'nova lox'],
                     'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
print(data)
# 假设你想要添加一列表示该肉类食物来源的动物类型。我们先编写一个不同肉类到动物的映射
meat_to_animal = {'bacon': 'pig', 'pulled pork': 'pig', 'pastrami': 'cow',
                  'corned beef': 'cow', 'honey ham': 'pig', 'nova lox': 'salmon'}
lowercased = data['food'].str.lower()
print(lowercased)
data['animal'] = lowercased.map(meat_to_animal)
print(data)
# 我们也可以传入一个能够完成全部这些工作的函数
# 使用map是一种实现元素级转换以及其他数据清理工作的便捷方式
data['food'].map(lambda x: meat_to_animal[x.lower()])
print(data)
print()

# 利用fillna方法填充缺失数据可以看做值替换的一种特殊情况。前面已经看到，
# map可用于修改对象的数据子集，而replace则提供了一种实现该功能的更简单、更灵活的方式
data = pd.Series([1., -999., 2., -999., -1000., 3.])
print(data)
# -999这个值可能是一个表示缺失数据的标记值。要将其替换为pandas能够理解的NA值，
# 我们可以利用replace来产生一个新的Series（除非传入inplace=True）
print(data.replace(-999, np.nan))
# 如果你希望一次性替换多个值，可以传入一个由待替换值组成的列表以及一个替换值
print(data.replace([-999, -1000], np.nan))
# 要让每个值有不同的替换值，可以传递一个替换列表
print(data.replace([-999, -1000], [np.nan, 0]))
# 传入的参数也可以是字典
print(data.replace({-999: np.nan, -1000: 0}))
