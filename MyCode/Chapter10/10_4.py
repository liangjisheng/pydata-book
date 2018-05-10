# -*- coding:utf-8 -*-
"""
@project = 0427-1
@file = 10_4
@author = Liangjisheng
@create_time = 2018/4/28 0028 下午 20:42
"""
import pandas as pd
import numpy as np
# pandas有一些能根据指定面元或样本分位数将数据拆分成多块的工具（比如cut和qcut）
# 将这些函数跟groupby结合起来，就能非常轻松地实现对数据集的桶(bucket)或分位数(quantile)分析了
# 以下面这个简单的随机数据集为例，我们利用cut将其装入长度相等的桶中
frame = pd.DataFrame({'data1': np.random.randn(1000),
                      'data2': np.random.randn(1000)})
print(frame.head())
quartiles = pd.cut(frame.data1, 4)
print(quartiles[:10])

# 由cut返回的Categorical对象可直接传递到groupby。因此，我们可以像下面这样对data2列做一些统计计算
def get_stats(group):
    return {'min': group.min(), 'max': group.max(),
            'count': group.count(), 'mean': group.mean()}

grouped = frame.data2.groupby(quartiles)
print(grouped.apply(get_stats).unstack())

# 这些都是长度相等的桶。要根据样本分位数得到大小相等的桶，使用qcut即可
# 传入labels=False即可只获取分位数的编号
grouping = pd.qcut(frame.data1, 10, labels=False)
grouped = frame.data2.groupby(grouping)
print(grouped.apply(get_stats).unstack())

grouping = pd.qcut(frame.data1, 10)
grouped = frame.data2.groupby(grouping)
print(grouped.apply(get_stats).unstack())
print()

# 对于缺失数据的清理工作，有时你会用dropna将其替换掉，而有时则可能会希望用一个固定值
# 或由数据集本身所衍生出来的值去填充NA值。这时就得使用fillna这个工具了
# 在下面这个例子中，我用平均值去填充NA值
s = pd.Series(np.random.randn(6))
s[::2] = np.nan
print(s)
print(s.sum())
print(s.mean())
print(s.fillna(s.mean()))

# 假设你需要对不同的分组填充不同的值。一种方法是将数据分组，并使用apply和一个能够对各数据块调用
# fillna的函数即可.下面是一些有关美国几个州的示例数据，这些州又被分为东部和西部
states = ['Ohio', 'New York', 'Vermont', 'Florida', 'Oregon', 'Nevada', 'California', 'Idaho']
group_key = ['East'] * 4 + ['West'] * 4
print(group_key)
data = pd.Series(np.random.randn(8), index=states)
print(data)
# 将一些值设为缺失
data[['Vermont', 'Nevada', 'Idaho']] = np.nan
print(data)
print(data.groupby(group_key).mean())
# 我们可以用分组平均值去填充NA值:
fill_mean = lambda g: g.fillna(g.mean())
print(data.groupby(group_key).apply(fill_mean))

# 也可以在代码中预定义各组的填充值。由于分组具有一个name属性，所以我们可以拿来用一下
fill_values = {'East': 0.5, 'West': -1}
fill_func = lambda g: g.fillna(fill_values[g.name])
print(data.groupby(group_key).apply(fill_func))
