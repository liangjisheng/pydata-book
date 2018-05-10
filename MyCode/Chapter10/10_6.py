# -*- coding:utf-8 -*-
"""
@project = 0427-1
@file = 10_6
@author = Liangjisheng
@create_time = 2018/4/29 0029 上午 11:07
"""
import pandas as pd
import numpy as np
# 回到前面小费的例子。使用read_csv导入数据之后，我们添加了一个小费百分比的列tip_pct
tips = pd.read_csv('tips.csv')
# Add tip percentage of total bill
tips['tip_pct'] = tips['tip'] / tips['total_bill']
print(tips.head())

# 假设我想要根据day和smoker计算分组平均数（pivot_table的默认聚合类型），并将day和smoker放到行上
print(tips.pivot_table(index=['day', 'smoker']))
print(tips.pivot_table(['tip_pct', 'size'], index=['time', 'day'], columns='smoker'))
# 还可以对这个表作进一步的处理，传入margins=True添加分项小计。这将会添加标签为All的行和列，
# 其值对应于单个等级中所有数据的分组统计
print(tips.pivot_table(['tip_pct', 'size'], index=['time', 'day'],
                       columns='smoker', margins=True))

# 要使用其他的聚合函数，将其传给aggfunc即可。例如
# 使用count或len可以得到有关分组大小的交叉表（计数或频率）
print(tips.pivot_table('tip_pct', index=['time', 'smoker'], columns='day',
                       aggfunc=len, margins=True))
print()

# 如果存在空的组合（也就是NA），你可能会希望设置一个fill_value
print(tips.pivot_table('tip_pct', index=['time', 'size', 'smoker'],
                       columns='day', aggfunc='mean', fill_value=0))
