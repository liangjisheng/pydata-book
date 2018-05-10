# -*- coding:utf-8 -*-
"""
@project = 0501-1
@file = 11_8
@author = Liangjisheng
@create_time = 2018/5/2 0002 下午 14:47
"""
from datetime import datetime
import pandas as pd
import numpy as np
# 固定频率的数据集通常会将时间信息分开存放在多个列中。例如，
# 在下面这个宏观经济数据集中，年度和季度就分别存放在不同的列中
data = pd.read_csv('macrodata.csv')
print(data.head(5))
print(data.year)
print(data.quarter)
# 通过将这些数组以及一个频率传入PeriodIndex，就可以将它们合并成DataFrame的一个索引
index = pd.PeriodIndex(year=data.year, quarter=data.quarter, freq='Q-DEC')
print(index)
data.index = index
print(data.infl)
print()

# 重采样（resampling）指的是将时间序列从一个频率转换到另一个频率的处理过程。
# 将高频率数据聚合到低频率称为降采样（downsampling），而将低频率数据转换到
# 高频率则称为升采样（upsampling）。并不是所有的重采样都能被划分到这两个大类中
# 例如，将W-WED（每周三）转换为W-FRI既不是降采样也不是升采样
# pandas对象都带有一个resample方法，它是各种频率转换工作的主力函数。
# resample有一个类似于groupby的API，调用resample可以分组数据，然后会调用一个聚合函数
rng = pd.date_range('2000-01-01', periods=100, freq='D')
print(rng)
ts = pd.Series(np.random.randn(len(rng)), index=rng)
print(ts)
print(ts.resample('M').mean())
print(ts.resample('M', kind='period').mean())
print()

# 将数据聚合到规律的低频率是一件非常普通的时间序列处理任务。待聚合的数据不必拥有固定的频率，
# 期望的频率会自动定义聚合的面元边界，这些面元用于将时间序列拆分为多个片段。例如，要转换到
# 月度频率('M'或'BM'),数据需要被划分到多个单月时间段中.各时间段都是半开放的.一个数据点只能
# 属于一个时间段，所有时间段的并集必须能组成整个时间帧.在用resample对数据进行降采样时,需要
# 考虑两样东西: 1.各区间哪边是闭合的;2.如何标记各个聚合面元，用区间的开头还是末尾
rng = pd.date_range('2000-01-01', periods=12, freq='T')
ts = pd.Series(np.arange(12), index=rng)
print(ts)
# 默认左闭右开,左边标记
print(ts.resample('5min').sum())
# 假设你想要通过求和的方式将这些数据聚合到“5分钟”块中
# 最终的时间序列是以各面元左边界的时间戳进行标记的。传入label='right'
# 即可用面元的邮编界对其进行标记
print(ts.resample('5min', closed='right').sum())
print(ts.resample('5min', closed='right', label='right').sum())
# 最后，你可能希望对结果索引做一些位移，比如从右边界减去一秒以便更容易明白该时间戳到底
# 表示的是哪个区间。只需通过loffset设置一个字符串或日期偏移量即可实现这个目的
print(ts.resample('5min', closed='right', label='right', loffset='-1s').sum())

# 传入的频率将会以“5分钟”的增量定义面元边界。默认情况下，面元的右边界是包含的，
# 因此00:00到00:05的区间中是包含00:05的。传入closed='left'会让区间以左边界闭合
print(ts.resample('5min', closed='left').sum())
print(ts.resample('5min', closed='left', label='right').sum())
print(ts.resample('5min', closed='left', label='right', loffset='-1s').sum())

# 金融领域中有一种无所不在的时间序列聚合方式,即计算各面元的四个值:第一个值(open,开盘)、
# 最后一个值(close,收盘)、最大值(high,最高)以及最小值(low,最低).传入how='ohlc'即可得
# 到一个含有这四种聚合值的DataFrame.整个过程很高效,只需一次扫描即可计算出结果
print(ts.resample('5min').ohlc())
