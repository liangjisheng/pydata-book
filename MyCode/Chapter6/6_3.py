# -*- coding:utf-8 -*-
"""
@project = 0419-1
@file = 6_3
@author = Liangjisheng
@create_time = 2018/4/19 0019 下午 20:50
"""
import pandas as pd
import os
import sys
import numpy as np
# 数据也可以被输出为分隔符格式的文本。我们再来看看之前读过的一个CSV文件：
data = pd.read_csv('ex5.csv')
print(data)
# 利用DataFrame的to_csv方法，我们可以将数据写到一个以逗号分隔的文件中
data.to_csv('out.csv')
os.system('type out.csv')
print()

# 当然，还可以使用其他分隔符（由于这里直接写出到sys.stdout，所以仅仅是打印出文本结果而已）
data.to_csv(sys.stdout, sep='|')
# 缺失值在输出结果中会被表示为空字符串。你可能希望将其表示为别的标记值
data.to_csv(sys.stdout, na_rep='NULL')
# 如果没有设置其他选项，则会写出行和列的标签。当然，它们也都可以被禁用
data.to_csv(sys.stdout, index=False, header=False)
# 此外，你还可以只写出一部分的列，并以你指定的顺序排列
data.to_csv(sys.stdout, index=False, columns=['a', 'b', 'c'])
print()

# Series也有一个to_csv方法
dates = pd.date_range('1/1/2000', periods=7)
print(dates)
ts = pd.Series(np.arange(7), index=dates)
print(ts)
ts.to_csv('tseries.csv')
os.system('type tseries.csv')
print()

# 大部分存储在磁盘上的表格型数据都能用pandas.read_table进行加载。然而，
# 有时还是需要做一些手工处理。由于接收到含有畸形行的文件而使read_table
# 出毛病的情况并不少见。为了说明这些基本工具，看看下面这个简单的CSV文件

# 对于任何单字符分隔符文件，可以直接使用Python内置的csv模块。
# 将任意已打开的文件或文件型的对象传给csv.reader：
import csv
f = open('ex7.csv')
reader = csv.reader(f)
# 对这个reader进行迭代将会为每行产生一个元组（并移除了所有的引号）
for line in reader:
    print(line)
f.close()
print()

# 现在，为了使数据格式合乎要求，你需要对其做一些整理工作。我们一步一步来做。
# 首先，读取文件到一个多行的列表中
with open('ex7.csv') as f:
    lines = list(csv.reader(f))
print(lines)
# 然后，我们将这些行分为标题行和数据行
header, values = lines[0], lines[1:]
print(header)
print(values)
# 然后，我们可以用字典构造式和zip(*values)，后者将行转置为列，创建数据列的字典：
data_dict = {h: v for h, v in zip(header, zip(*values))}
print(data_dict)

# CSV文件的形式有很多。只需定义csv.Dialect的一个子类即可定义出新格式
# （如专门的分隔符、字符串引用约定、行结束符等）：
class my_dialect(csv.Dialect):
    lineterminator = '\n'
    delimiter = ';'
    quotechar = '"'
    quoting = csv.QUOTE_MINIMAL

# 要手工输出分隔符文件，你可以使用csv.writer。它接受一个已打开且可写的文件对象以及跟
# csv.reader相同的那些语支和格式化选项
with open('mydata.csv', 'w') as f:
    writer = csv.writer(f, dialect=my_dialect)
    writer.writerow(('one', 'two', 'three'))
    writer.writerow(('1', '2', '3'))
    writer.writerow(('4', '5', '6'))
    writer.writerow(('7', '8', '9'))

os.system('type mydata.csv')
print()
