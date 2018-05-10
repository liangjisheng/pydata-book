# -*- coding:utf-8 -*-
"""
@project = 0501-1
@file = 11_3
@author = Liangjisheng
@create_time = 2018/5/1 0001 上午 10:37
"""
from datetime import datetime
import pandas as pd
import numpy as np
# pandas中的原生时间序列一般被认为是不规则的，也就是说，它们没有固定的频率。
# 对于大部分应用程序而言，这是无所谓的。但是，它常常需要以某种相对固定的频率进行分析，
# 比如每日、每月、每15分钟等（这样自然会在时间序列中引入缺失值）。幸运的是，
# pandas有一整套标准时间序列频率以及用于重采样、频率推断、生成固定频率日期范围的工具。
# 例如，我们可以将之前那个时间序列转换为一个具有固定频率（每日）的时间序列，
# 只需调用resample即可
dates = [datetime(2011, 1, 2), datetime(2011, 1, 5),
         datetime(2011, 1, 7), datetime(2011, 1, 8),
         datetime(2011, 1, 10), datetime(2011, 1, 12)]
ts = pd.Series(np.random.randn(6), index=dates)
print(ts)
resampler = ts.resample('D')
print(resampler)

# 虽然我之前用的时候没有明说，但你可能已经猜到pandas.date_range
# 可用于根据指定的频率生成指定长度的DatetimeIndex
index = pd.date_range('2012-04-01', '2012-06-01')
print(index)
# 默认情况下，date_range会产生按天计算的时间点。如果只传入起始或结束日期，
# 那就还得传入一个表示一段时间的数字
print(pd.date_range(start='2012-04-01', periods=20))
print(pd.date_range(end='2012-06-01', periods=20))
# 起始和结束日期定义了日期索引的严格边界。例如，如果你想要生成一个由每月
# 最后一个工作日组成的日期索引，可以传入"BM"频率（表示business end of month）
# 这样就只会包含时间间隔内（或刚好在边界上的）符合频率要求的日期
print(pd.date_range('2017-01-01', '2017-12-01', freq='BM'))

# date_range默认会保留起始和结束时间戳的时间信息（如果有的话）
print(pd.date_range('2012-05-02 12:56:31', periods=5))
# 有时，虽然起始和结束日期带有时间信息，但你希望产生一组被规范化（normalize）
# 到午夜的时间戳。normalize选项即可实现该功能
print(pd.date_range('2012-05-02 12:56:31', periods=5, normalize=True))

# pandas中的频率是由一个基础频率（base frequency）和一个乘数组成的。基础频率通常以
# 一个字符串别名表示，比如"M"表示每月，"H"表示每小时。对于每个基础频率，
# 都有一个被称为日期偏移量（date offset）的对象与之对应。例如，按小时计算的频率
# 可以用Hour类表示
from pandas.tseries.offsets import Hour, Minute
hour = Hour()
print(hour)
# 传入一个整数即可定义偏移量的倍数
four_hours = Hour(4)
print(four_hours)
# 一般来说，无需明确创建这样的对象，只需使用诸如"H"或"4H"这样的字符串别名即可。
# 在基础频率前面放上一个整数即可创建倍数
print(pd.date_range('2001-01-01', '2001-01-03 23:59', freq='4h'))
# 大部分偏移量对象都可通过加法进行连接
print(Hour(2) + Minute(30))
# 同理，你也可以传入频率字符串（如"2h30min"），这种字符串可以被高效地解析为等效的表达式
print(pd.date_range('2000-01-01', periods=10, freq='1h30min'))
# WOM（Week Of Month）是一种非常实用的频率类，它以WOM开头
# 它使你能获得诸如“每月第3个星期五”之类的日期
rng = pd.date_range('2012-01-01', '2012-09-01', freq='WOM-3FRI')
print(type(rng))
print(rng)
print(list(rng))
print(type(list(rng)[0]))
