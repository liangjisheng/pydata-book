# -*- coding:utf-8 -*-
"""
@project = 0501-1
@file = 11-4
@author = Liangjisheng
@create_time = 2018/5/1 0001 上午 11:18
"""
from datetime import datetime
import pandas as pd
import numpy as np
# 移动（shifting）指的是沿着时间轴将数据前移或后移。Series和DataFrame都有一个
# shift方法用于执行单纯的前移或后移操作，保持索引不变
ts = pd.Series(np.random.randn(4),
               index=pd.date_range('1/1/2000', periods=4, freq='M'))
print(ts)
print(ts.shift(2))
print(ts.shift(-2))
# shift通常用于计算一个时间序列或多个时间序列（如DataFrame的列）中的百分比变化。可以这样表达
print(ts / ts.shift(1) - 1)
# 由于单纯的移位操作不会修改索引，所以部分数据会被丢弃。因此，如果频率已知，
# 则可以将其传给shift以便实现对时间戳进行位移而不是对数据进行简单位移
print(ts.shift(2, freq='M'))
# 这里还可以使用其他频率，于是你就能非常灵活地对数据进行超前和滞后处理了
print(ts.shift(3, freq='D'))
print(ts.shift(1, freq='90T'))

# pandas的日期偏移量还可以用在datetime或Timestamp对象上
from pandas.tseries.offsets import Day, MonthEnd
now = datetime(2011, 11, 17)
print(now)
print(now + 3 * Day())
# 如果加的是锚点偏移量（比如MonthEnd），第一次增量会将原日期向前滚动到符合频率规则的下一个日期
print(now + MonthEnd())
print(now + MonthEnd(2))
# 通过锚点偏移量的rollforward和rollback方法，可明确地将日期向前或向后“滚动”
offset = MonthEnd()
print(offset.rollforward(now))
print(offset.rollback(now))
# 日期偏移量还有一个巧妙的用法，即结合groupby使用这两个“滚动”方法
ts = pd.Series(np.random.randn(20),
               index=pd.date_range('1/15/2000', periods=20, freq='4d'))
print(ts)
print(ts.groupby(offset.rollforward).mean())
# 当然，更简单、更快速地实现该功能的办法是使用resample
print(ts.resample('M').mean())
