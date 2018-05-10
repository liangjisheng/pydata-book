# -*- coding:utf-8 -*-
"""
@project = 0501-1
@file = 11_2
@author = Liangjisheng
@create_time = 2018/5/1 0001 上午 10:08
"""
from datetime import datetime
import pandas as pd
import numpy as np
dates = [datetime(2011, 1, 2), datetime(2011, 1, 5),
         datetime(2011, 1, 7), datetime(2011, 1, 8),
         datetime(2011, 1, 10), datetime(2011, 1, 12)]
ts = pd.Series(np.random.randn(6), index=dates)
print(ts)
# 这些datetime对象实际上是被放在一个DatetimeIndex中的
print(ts.index)

# 跟其他Series一样，不同索引的时间序列之间的算术运算会自动按日期对齐
print(ts[::2])
print(ts + ts[::2])
# pandas用NumPy的datetime64数据类型以纳秒形式存储时间戳
print(ts.index.dtype)
# DatetimeIndex中的各个标量值是pandas的Timestamp对象
stamp = ts.index[0]
print(stamp)
print(type(stamp))

# 当你根据标签索引选取数据时，时间序列和其它的pandas.Series很像
stamp = ts.index[2]
print(ts[stamp])
# 还有一种更为方便的用法：传入一个可以被解释为日期的字符串
print(ts['1/10/2011'])
print(ts['20110110'])
# 对于较长的时间序列，只需传入“年”或“年月”即可轻松选取数据的切片
longer_ts = pd.Series(np.random.randn(1000),
                      index=pd.date_range('1/1/2000', periods=1000))
print(longer_ts)
print(longer_ts['2001'])
# 这里，字符串“2001”被解释成年，并根据它选取时间区间。指定月也同样奏效
print(longer_ts['2001-05'])

# datetime对象也可以进行切片
print(ts)
print(ts[datetime(2011, 1, 7):])
# 由于大部分时间序列数据都是按照时间先后排序的，因此你也可以用不存在于该时间序列
# 中的时间戳对其进行切片（即范围查询）
print(ts['1/6/2011':'1/11/2011'])
# 跟之前一样，你可以传入字符串日期、datetime或Timestamp。注意，这样切片所产生的是
# 源时间序列的视图，跟NumPy数组的切片运算是一样的
# 这意味着，没有数据被复制，对切片进行修改会反映到原始数据上
# 此外，还有一个等价的实例方法也可以截取两个日期之间TimeSeries
print(ts.truncate(after='1/9/2011'))

# 这些操作对DataFrame也有效。例如，对DataFrame的行进行索引
# freq='W-WED'表示取得时间序列的频率，将每周三的日期取出来
dates = pd.date_range('1/1/2015', periods=100, freq='W-WED')
long_df = pd.DataFrame(np.random.randn(100, 4),
                       index=dates,
                       columns=['Colorado', 'Texas', 'New York', 'Ohio'])
print(long_df.head())
print(long_df['5-2016'])

# 在某些应用场景中，可能会存在多个观测数据落在同一个时间点上的情况。下面就是一个例子
dates = pd.DatetimeIndex(['1/1/2000', '1/2/2000', '1/2/2000', '1/2/2000', '1/3/2000'])
dup_ts = pd.Series(np.arange(5), index=dates)
print(dup_ts)
# 通过检查索引的is_unique属性，我们就可以知道它是不是唯一的
print(dup_ts.index.is_unique)
# 对这个时间序列进行索引，要么产生标量值，要么产生切片，具体要看所选的时间点是否重复
print(dup_ts['1/3/2000'])
print(dup_ts['1/2/2000'])
# 假设你想要对具有非唯一时间戳的数据进行聚合。一个办法是使用groupby，并传入level=0
grouped = dup_ts.groupby(level=0)
print(grouped.mean())
print(grouped.count())
