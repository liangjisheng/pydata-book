# -*- coding:utf-8 -*-
"""
@project = 0501-1
@file = 11_5
@author = Liangjisheng
@create_time = 2018/5/1 0001 上午 11:37
"""
from datetime import datetime
import pandas as pd
import numpy as np
import pytz
print(pytz.common_timezones[-5:])
# 要从pytz中获取时区对象，使用pytz.timezone即可
tz = pytz.timezone('America/New_York')
print(tz)

# 默认情况下，pandas中的时间序列是单纯的（naive）时区。看看下面这个时间序列
rng = pd.date_range('3/9/2012 9:30', periods=6, freq='D')
ts = pd.Series(np.random.randn(len(rng)), index=rng)
print(ts)
# 其索引的tz字段为None
print(ts.index.tz)
# 可以用时区集生成日期范围
print(pd.date_range('3/9/2012 9:30', periods=10, freq='D', tz='UTC'))
# 从单纯到本地化的转换是通过tz_localize方法处理的
ts_utc = ts.tz_localize('UTC')
print(ts)
print(ts_utc)
print(ts_utc.index)
# 一旦时间序列被本地化到某个特定时区，就可以用tz_convert将其转换到别的时区了
print(ts_utc.tz_convert('America/New_York'))
# 对于上面这种时间序列（它跨越了美国东部时区的夏令时转变期），我们可以将其本地化到EST，
# 然后转换为UTC或柏林时间
ts_eastern = ts.tz_localize('America/New_York')
print(ts_eastern.tz_convert('UTC'))
print(ts_eastern.tz_convert('Europe/Berlin'))
# tz_localize和tz_convert也是DatetimeIndex的实例方法
print(ts.index.tz_localize('Asia/Shanghai'))

# 如果两个时间序列的时区不同，在将它们合并到一起时，最终结果就会是UTC。
# 由于时间戳其实是以UTC存储的，所以这是一个很简单的运算，并不需要发生任何转换
rng = pd.date_range('3/7/2012 9:30', periods=10, freq='B')
ts = pd.Series(np.random.randn(len(rng)), index=rng)
print(ts)
print(len(ts[:7]))
ts1 = ts[:7].tz_localize('Europe/London')
print(ts1)
ts2 = ts1[2:].tz_convert('Europe/Moscow')
print(ts2)
result = ts1 + ts2
print(result)
print(result.index)
