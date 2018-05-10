# -*- coding:utf-8 -*-
"""
@project = 0422-2
@file = 7_5
@author = Liangjisheng
@create_time = 2018/4/22 0022 下午 17:35
"""
import pandas as pd
import numpy as np
# 计算指标/哑变量
# 另一种常用于统计建模或机器学习的转换方式是：将分类变量（categorical variable）
# 转换为“哑变量”或“指标矩阵”
# 如果DataFrame的某一列中含有k个不同的值，则可以派生出一个k列矩阵或DataFrame
# （其值全为1和0）。pandas有一个get_dummies函数可以实现该功能
df = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
                   'data1': range(6)})
print(df)
print(pd.get_dummies(df['key']))
print(pd.get_dummies(df['data1']))
# 有时候，你可能想给指标DataFrame的列加上一个前缀，以便能够跟其他数据进行合并
# get_dummies的prefix参数可以实现该功能
dummies = pd.get_dummies(df['key'], prefix='key')
print(dummies)
print(df[['data1']])
df_with_dummy = df[['data1']].join(dummies)
print(df_with_dummy)
print()

# 一个对统计应用有用的秘诀是：结合get_dummies和诸如cut之类的离散化函数
np.random.seed(12345)
values = np.random.rand(10)
print(values)
bins = [0, 0.2, 0.4, 0.6, 0.8, 1]
cats = pd.cut(values, bins)
print(cats)
print(pd.get_dummies(cats))
