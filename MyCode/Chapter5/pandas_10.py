# -*- coding:utf-8 -*-
"""
@project = 0416-1
@file = pandas_10
@author = Liangjisheng
@create_time = 2018/4/18 0018 下午 20:12
"""
import pandas as pd
import numpy as np
# pandas对象拥有一组常用的数学和统计方法。它们大部分都属于约简和汇总统计，
# 用于从Series中提取单个值（如sum或mean）或从DataFrame的行或列中提取一个Series。
# 跟对应的NumPy数组方法相比，它们都是基于没有缺失数据的假设而构建的。
# 看一个简单的DataFrame
df = pd.DataFrame([[1.4, np.nan], [7.1, -4.5], [np.nan, np.nan], [0.75, -1.3]],
                  index=['a', 'b', 'c', 'd'], columns=['one', 'two'])
print(df)
# 调用DataFrame的sum方法将会返回一个含有列的和的Series
print(df.sum())
# 传入axis='columns'或axis=1将会按行进行求和运算
print(df.sum(axis=1))
# NA值会自动被排除，除非整个切片（这里指的是行或列）都是NA。通过skipna选项可以禁用该功能
print(df.mean(axis='columns', skipna=False))

# 有些方法（如idxmin和idxmax）返回的是间接统计（比如达到最小值或最大值的索引）
print(df.idxmax())
print(df.idxmin())
# 另一些方法则是累计型的
print(df.cumsum())

# 还有一种方法，它既不是约简型也不是累计型。describe就是一个例子，
# 它用于一次性产生多个汇总统计
print(df.describe())

# 对于非数值型数据，describe会产生另外一种汇总统计：
obj = pd.Series(['a', 'a', 'b', 'c'] * 4)
print(obj.describe())

# import pandas_datareader.data as web
# all_data = {ticker: web.get_data_google(ticker)
#            for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG']}
# price = pd.DataFrame({ticker: data['Adj Close']
#                      for ticker, data, in all_data.items()})
# volume = pd.DataFrame({ticker: data['Volume']
#                       for ticker, data, in all_data.items()})

# 现在计算价格的百分数变化
# returns = price.pct_change()
# print(returns.tail())

# 唯一值、值计数以及成员资格
obj = pd.Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])
# 第一个函数是unique，它可以得到Series中的唯一值数组,
#  返回的唯一值是未排序的，如果需要的话，可以对结果再次进行排序
uniques = obj.unique()
print(uniques)
uniques.sort()
print(uniques)
# value_counts用于计算一个Series中各值出现的频率
print(obj.value_counts())
# 为了便于查看，结果Series是按值频率降序排列的。value_counts还是一个顶级pandas方法，
# 可用于任何数组或序列
print(pd.value_counts(obj.values, sort=False))
print(pd.value_counts(obj.values))

# isin用于判断矢量化集合的成员资格，可用于过滤Series中或DataFrame列中数据的子集
print(obj)
mask = obj.isin(['b', 'c'])
print(mask)
print(obj[mask])

# 与isin类似的是Index.get_indexer方法，它可以给你一个索引数组，
# 从可能包含重复值的数组到另一个不同值的数组
to_match = pd.Series(['c', 'a', 'b', 'b', 'c', 'a'])
unique_vals = pd.Series(['c', 'b', 'a'])
print(pd.Index(unique_vals).get_indexer(to_match))

# 有时，你可能希望得到DataFrame中多个相关列的一张柱状图。例如：
data = pd.DataFrame({'Qu1': [1, 3, 4, 3, 4], 'Qu2': [2, 3, 1, 2, 3],
                     'Qu3': [1, 5, 2, 4, 4]})
print(data)
# 将pandas.value_counts传给该DataFrame的apply函数
# 这里，结果中的行标签是所有列的唯一值。后面的频率值是每个列中这些值的相应计数
result = data.apply(pd.value_counts)
print(result)
result = data.apply(pd.value_counts).fillna(0)
print(result)
