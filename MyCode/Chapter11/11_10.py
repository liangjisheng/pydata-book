# -*- coding:utf-8 -*-
"""
@project = 0501-1
@file = 11_10
@author = Liangjisheng
@create_time = 2018/5/2 0002 下午 16:11
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
close_px_all = pd.read_csv('stock_px_2.csv',
                           parse_dates=True, index_col=0)
print(close_px_all[:5])
close_px = close_px_all[['AAPL', 'MSFT', 'XOM']]
print(close_px[:5])
close_px = close_px.resample('B').ffill()
print(close_px[:5])

print(close_px.AAPL.plot())
fig, axes = plt.subplots(1, 1)
close_px.AAPL.plot(ax=axes)
fig.show()

# 现在引入rolling运算符，它与resample和groupby很像。可以在TimeSeries或
# DataFrame以及一个window(表示期数)上调用它
fig, axes = plt.subplots(1, 1)
close_px.AAPL.plot(ax=axes)
# 表达式rolling(250)与groupby很像，但不是对其进行分组，而是创建一个按照250天分组
# 的滑动窗口对象。然后，我们就得到了苹果公司股价的250天的移动窗口
close_px.AAPL.rolling(250).mean().plot(ax=axes)
fig.show()

# 默认情况下，rolling函数需要窗口中所有的值为非NA值。可以修改该行为以解决缺失
# 数据的问题。其实，在时间序列开始处尚不足窗口期的那些数据就是个特例
appl_std250 = close_px.AAPL.rolling(250, min_periods=10).std()
print(appl_std250[:12])

# 对DataFrame调用rolling_mean（以及与之类似的函数）会将转换应用到所有的列上
fig, axes = plt.subplots(1, 1)
close_px.rolling(60).mean().plot(ax=axes, logy=True)
fig.show()

# rolling函数也可以接受一个指定固定大小时间补偿字符串，而不是一组时期。这样
# 可以方便处理不规律的时间序列。这些字符串也可以传递给resample。例如，我们
# 可以计算20天的滚动均值，如下所示
print(close_px.rolling('20D').mean())
