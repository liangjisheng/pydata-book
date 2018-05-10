# -*- coding:utf-8 -*-
"""
@project = 0501-1
@file = 11_9
@author = Liangjisheng
@create_time = 2018/5/2 0002 下午 15:43
"""
from datetime import datetime
import pandas as pd
import numpy as np
# 升采样和插值,在将数据从低频率转换到高频率时,就不需要聚合了.
# 我们来看一个带有一些周型数据的DataFrame
frame = pd.DataFrame(np.random.randn(2, 4),
                     index=pd.date_range('1/1/2000', periods=2, freq='W-WED'),
                     columns=['Colorado', 'Texas', 'New York', 'Ohio'])
print(frame)
# 当你对这个数据进行聚合，每组只有一个值，这样就会引入缺失值。我们使用asfreq
# 方法转换成高频，不经过聚合
df_daily = frame.resample('D')
print(df_daily)
df_daily = frame.resample('D').asfreq()
print(df_daily)

# 假设你想要用前面的周型值填充"非星期三".resampling的填充和插值方式跟fillna和reindex的一样
print(frame.resample('D').ffill())
# 同样，这里也可以只填充指定的时期数(目的是限制前面的观测值的持续使用距离)
print(frame.resample('D').ffill(limit=2))
# 注意，新的日期索引完全没必要跟旧的重叠
print(frame.resample('W-THU').ffill())
print()

# 通过时期进行重采样,对那些使用时期索引的数据进行重采样与时间戳很像
frame = pd.DataFrame(np.random.randn(24, 4),
                     index=pd.period_range('1-2000', '12-2001', freq='M'),
                     columns=['Colorado', 'Texas', 'New York', 'Ohio'])
print(frame[:5])
annual_frame = frame.resample('A-DEC').mean()
print(annual_frame)

# 升采样要稍微麻烦一些，因为你必须决定在新频率中各区间的哪端用于放置原来的值，
# 就像asfreq方法那样。convention参数默认为'start'，也可设置为'end'
print(annual_frame.resample('Q-DEC').ffill())
print(annual_frame.resample('Q-DEC', convention='end').ffill())
