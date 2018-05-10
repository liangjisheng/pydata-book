# -*- coding:utf-8 -*-
"""
@project = 0507-1
@file = 12_1
@author = Liangjisheng
@create_time = 2018/5/7 0007 下午 15:59
"""
import numpy as np
import pandas as pd
values = pd.Series(['apple', 'orange', 'apple', 'apple'] * 2)
print(values)
print(pd.unique(values))
print(pd.value_counts(values))

# 许多数据系统（数据仓库、统计计算或其它应用）都发展出了特定的表征重复值的方法，
# 以进行高效的存储和计算。在数据仓库中，最好的方法是使用所谓的包含不同值得
# 维表(Dimension Table)，将主要的参数存储为引用维表整数键
values = pd.Series([0, 1, 0, 0] * 2)
dim = pd.Series(['apple', 'orange'])
print(values)
print(dim)
# 可以使用take方法存储原始的字符串Series
print(dim.take(values))

# pandas有一个特殊的分类类型，用于保存使用整数分类表示法的数据
fruits = ['apple', 'orange', 'apple', 'apple'] * 2
N = len(fruits)
df = pd.DataFrame({'fruit': fruits,
                   'basket_id': np.arange(N),
                   'count': np.random.randint(3, 15, size=N),
                   'weight': np.random.uniform(0, 4, size=N)},
                  columns=['basket_id', 'fruit', 'count', 'weight'])
print(df)
print(df['fruit'])
# 这里，df['fruit']是一个Python字符串对象的数组。我们可以通过调用它，将它转变为分类
fruit_cat = df['fruit'].astype('category')
print(fruit_cat)
# ruit_cat的值不是NumPy数组，而是一个pandas.Categorical实例
c = fruit_cat.values
print(type(c))
print(c.categories)
print(c.codes)

# 你还可以从其它Python序列直接创建pandas.Categorical
my_categories = pd.Categorical(['foo', 'bar', 'baz', 'foo', 'bar'])
print(my_categories)

# 如果你已经从其它源获得了分类编码，你还可以使用from_codes构造器
categories = ['foo', 'bar', 'baz']
codes = [0, 1, 2, 0, 0, 1]
my_cats_2 = pd.Categorical.from_codes(codes, categories)
print(my_cats_2)
