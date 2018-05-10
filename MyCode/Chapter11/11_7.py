# -*- coding:utf-8 -*-
"""
@project = 0501-1
@file = 11_7
@author = Liangjisheng
@create_time = 2018/5/2 0002 下午 14:17
"""
from datetime import datetime
import pandas as pd
import numpy as np
# 季度型数据在会计、金融等领域中很常见。许多季度型数据都会涉及“财年末”的概念，
# 通常是一年12个月中某月的最后一个日历日或工作日。就这一点来说，时期"2012Q4"根据
# 财年末的不同会有不同的含义。pandas支持12种可能的季度型频率，即Q-JAN到Q-DEC
p = pd.Period('2012Q4', freq='Q-JAN')
print(p)
# 在以1月结束的财年中，2012Q4是从去年11月到1月(将其转换为日型频率就明白了)
print(p.asfreq('D', 'start'))
print(p.asfreq('D', 'end'))
# Period之间的算术运算会非常简单。例如，要获取该季度倒数第二个工作日下午4点的时间戳，
# 你可以这样
p4pm = (p.asfreq('B', 'end') - 1).asfreq('T', 'start') + 16 * 60
print(type(p4pm))
print(p4pm)
print(type(p4pm.to_timestamp()))
print(p4pm.to_timestamp())

# period_range可用于生成季度型范围
rng = pd.period_range('2011Q3', '2012Q4', freq='Q-JAN')
print(rng)
ts = pd.Series(np.arange(len(rng)), index=rng)
print(ts)
new_rng = (rng.asfreq('B', 'end') - 1).asfreq('T', 'start') + 16 * 60
print(new_rng)
ts.index = new_rng.to_timestamp()
print(ts)
print()

# 通过使用to_period方法，可以将由时间戳索引的Series和DataFrame对象转换为以时期索引
rng = pd.date_range('2000-01-01', periods=3, freq='M')
print(rng)
ts = pd.Series(np.random.randn(3), index=rng)
print(ts)
pts = ts.to_period()
print(pts)
print()

# 由于时期指的是非重叠时间区间，因此对于给定的频率，一个时间戳只能属于一个时期
# 新PeriodIndex的频率默认是从时间戳推断而来的，你也可以指定任何别的频率。
# 结果中允许存在重复时期
rng = pd.date_range('1/29/2000', periods=6, freq='D')
print(rng)
ts2 = pd.Series(np.random.randn(6), index=rng)
print(ts2)
print(ts2.to_period('M'))
pts = ts2.to_period()
print(pts)
print(pts.to_timestamp(how='end'))
