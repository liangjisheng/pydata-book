# -*- coding:utf-8 -*-
"""
@project = 0501-1
@file = 11_6
@author = Liangjisheng
@create_time = 2018/5/1 0001 下午 19:16
"""
from datetime import datetime
import pandas as pd
import numpy as np
# 时期（period）表示的是时间区间，比如数日、数月、数季、数年等。Period类所表示的
# 就是这种数据类型，其构造函数需要用到一个字符串或整数
p = pd.Period(2007, freq='A-DEC')
print(p)
print(type(p))
# 这里，这个Period对象表示的是从2007年1月1日到2007年12月31日之间的整段时间。
# 只需对Period对象加上或减去一个整数即可达到根据其频率进行位移的效果
print(p + 5)
print(p - 2)
# 如果两个Period对象拥有相同的频率，则它们的差就是它们之间的单位数量
print(pd.Period('2014', freq='A-DEC') - p)
# period_range函数可用于创建规则的时期范围
rng = pd.period_range('2000-01-01', '2000-06-30', freq='M')
print(rng)
print(rng[0])
# PeriodIndex类保存了一组Period，它可以在任何pandas数据结构中被用作轴索引
print(pd.Series(np.random.randn(6), index=rng))
# 如果你有一个字符串数组，你也可以使用PeriodIndex类
values = ['2001Q3', '2002Q2', '2003Q1']
index = pd.PeriodIndex(values, freq='Q-DEC')
print(index)

# 时期的频率转换, Period和PeriodIndex对象都可以通过其asfreq方法被转换成别的频率。
# 假设我们有一个年度时期，希望将其转换为当年年初或年末的一个月度时期。该任务非常简单
p = pd.Period('2007', freq='A-DEC')
# 你可以将Period('2007','A-DEC')看做一个被划分为多个月度时期的时间段中的游标
print(p)
print(p.asfreq('M', how='start'))
print(p.asfreq('M', how='end'))

p = pd.Period('2007', freq='A-JUN')
print(p)
print(p.asfreq('M', 'start'))
print(p.asfreq('M', 'end'))

# 在将高频率转换为低频率时，超时期（superperiod）是由子时期（subperiod）所属的位置决定的
# 例如，在A-JUN频率中，月份“2007年8月”实际上是属于周期“2008年”的
p = pd.Period('Aug-2007', 'M')
print(p)
print(p.asfreq('A-JUN'))

# 完整的PeriodIndex或TimeSeries的频率转换方式也是如此
rng = pd.period_range('2006', '2009', freq='A-DEC')
ts = pd.Series(np.random.randn(len(rng)), index=rng)
print(ts)
print(ts.asfreq('M', how='start'))
# 这里，根据年度时期的第一个月，每年的时期被取代为每月的时期。
# 如果我们想要每年的最后一个工作日，我们可以使用“B”频率，并指明想要该时期的末尾
print(ts.asfreq('B', how='end'))
