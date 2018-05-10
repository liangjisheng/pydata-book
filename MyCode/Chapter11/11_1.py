# -*- coding:utf-8 -*-
"""
@project = 0501-1
@file = 11_1
@author = Liangjisheng
@create_time = 2018/5/1 0001 上午 9:27
"""
from datetime import datetime
from datetime import timedelta
import pandas as pd
now = datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.date())
print(now.microsecond)
print(now.fold)
print(now.time())
print(now.ctime())
print(now.dst())
print(now.timestamp())
print(now.timetuple())
print(now.timetz())
print(now.toordinal())
print(now.tzname())
print(now.utcoffset())
print(now.utctimetuple())
print(now.weekday())

# datetime以毫秒形式存储日期和时间。timedelta表示两个datetime对象之间的时间差
delta = datetime(2011, 1, 7) - datetime(2008, 6, 24, 8, 15)
print(delta)
print(delta.days)
print(delta.microseconds)
print(delta.seconds)
print(delta.total_seconds())
print(delta.max)
print(delta.min)
print(delta.resolution)

# 可以给datetime对象加上（或减去）一个或多个timedelta，这样会产生一个新对象
start = datetime(2011, 1, 7)
print(start)
print(start + timedelta(12))
print(start - 2 * timedelta(12))

# 利用str或strftime方法（传入一个格式化字符串），datetime对象和
# pandas的Timestamp对象（稍后就会介绍）可以被格式化为字符串
stamp = datetime(2011, 1, 3)
print(str(stamp))
print(stamp.strftime('%Y-%m-%d'))
print(stamp.strftime('%H-%M-%S'))

# datetime.strptime可以用这些格式化编码将字符串转换为日期
value = '2011-01-03'
print(datetime.strptime(value, '%Y-%m-%d'))
datestrs = ['7/6/2011', '8/6/2011']
print([datetime.strptime(x, '%m/%d/%Y') for x in datestrs])

# datetime.strptime是通过已知格式进行日期解析的最佳方式。但是每次都要编写格式定义
# 是很麻烦的事情，尤其是对于一些常见的日期格式。这种情况下，
# 你可以用dateutil这个第三方包中的parser.parse方法（pandas中已经自动安装好了）
from dateutil.parser import parse
print(parse('2011-01-03'))
# dateutil可以解析几乎所有人类能够理解的日期表示形式
print(parse('Jan 31, 1997 10:45 PM'))
# 在国际通用的格式中，日出现在月的前面很普遍，传入dayfirst=True即可解决这个问题
print(parse('6/12/2011', dayfirst=True))

# pandas通常是用于处理成组日期的，不管这些日期是DataFrame的轴索引还是列。
# to_datetime方法可以解析多种不同的日期表示形式。对标准日期格式（如ISO8601）的解析非常快
datestrs = ['2011-07-06 12:00:00', '2011-08-06 00:00:00']
print(pd.to_datetime(datestrs))
# 它还可以处理缺失值（None、空字符串等）
idx = pd.to_datetime(datestrs + [None])
print(idx)
print(idx[2])
print(pd.isnull(idx))
