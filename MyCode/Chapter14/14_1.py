# -*- coding:utf-8 -*-
"""
@project = 0508-1
@file = 14_1
@author = Liangjisheng
@create_time = 2018/5/8 0008 下午 17:48
"""
# 以每小时快照为例，文件中各行的格式为JSON（即JavaScript Object Notation，这是一种常用的
# Web数据格式）。例如，如果我们只读取某个文件中的第一行，那么所看到的结果应该是下面这样
path = 'datasets/bitly_usagov/example.txt'
# print(open(path).readline())
# Python有内置或第三方模块可以将JSON字符串转换成Python字典对象。这里，
# 我将使用json模块及其loads函数逐行加载已经下载好的数据文件
import json
records = [json.loads(line) for line in open(path)]
# # 现在，records对象就成为一组Python字典了
print(type(records[0]))
for key, value in records[0].items():
    print(key, ":", value)
# 假设我们想要知道该数据集中最常出现的是哪个时区（即tz字段），得到答案的办法有很多。
# 首先，我们用列表推导式取出一组时区
time_zones = [rec['tz'] for rec in records if 'tz' in rec]
print(time_zones[:10])

# 只看前10个时区，我们发现有些是未知的（即空的）。虽然可以将它们过滤掉，但现在暂时先留着
# 接下来，为了对时区进行计数，这里介绍两个办法：一个较难（只使用标准Python库），另一个较
# 简单（使用pandas）。计数的办法之一是在遍历时区的过程中将计数值保存在字典中
def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts

# 如果使用Python标准库的更高级工具，那么你可能会将代码写得更简洁一些
from collections import defaultdict

def get_counts2(sequence):
    counts = defaultdict(int)   # values will initialize to 0
    for x in sequence:
        counts[x] += 1
    return counts

# 我将逻辑写到函数中是为了获得更高的复用性。要用它对时区进行处理，只需将time_zones传入即可
counts = get_counts(time_zones)
print(counts['America/New_York'])
print(len(time_zones))

# 如果想要得到前10位的时区及其计数值，我们需要用到一些有关字典的处理技巧
def top_counts(count_dict, n=10):
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]

print(top_counts(counts))

# 如果你搜索Python的标准库，你能找到collections.Counter类，它可以使这项工作更简单
from collections import Counter
counts = Counter(time_zones)
print(counts.most_common(10))

# 用pandas对时区进行计数
import pandas as pd
frame = pd.DataFrame(records)
print(frame[:5])
print(frame.info())
print(frame['tz'][:10])

# 然后可以对Series使用value_counts方法
tz_counts = frame['tz'].value_counts()
print(tz_counts[:10])

# 我们可以用matplotlib可视化这个数据.为此,我们先给记录中未知或缺失的时区填上一个替代值
# fillna函数可以替换缺失值(NA),而未知值(空字符串)则可以通过布尔型数组索引加以替换
clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'
tz_counts = clean_tz.value_counts()
print(tz_counts[:10])

# 此时，我们可以用seaborn包创建水平柱状图
import seaborn as sns
import matplotlib.pyplot as plt
subset = tz_counts[:10]
flg, axes = plt.subplots(1, 1)
sns.barplot(y=subset.index, x=subset.values, ax=axes)
flg.show()

# a字段含有执行URL短缩操作的浏览器、设备、应用程序的相关信息
print(frame['a'][1])
print(frame['a'][50])
print(frame['a'][51][:50])

# 将这些"agent"字符串中的所有信息都解析出来是一件挺郁闷的工作。一种策略是
# 将这种字符串的第一节（与浏览器大致对应）分离出来并得到另外一份用户行为摘要
results = pd.Series([x.split()[0] for x in frame.a.dropna()])
print(results[:5])
print(results.value_counts()[:8])
print()

# 现在，假设你想按Windows和非Windows用户对时区统计信息进行分解。为了简单
# 起见，我们假定只要agent字符串中含有"Windows"就认为该用户为Windows用户
# 由于有的agent缺失，所以首先将它们从数据中移除
cframe = frame[frame.a.notnull()]
# 然后计算出各行是否含有Windows的值
import numpy as np
cframe['os'] = np.where(cframe['a'].str.contains('Windows'), 'Windows', 'Not Windows')
print(cframe['os'][:5])
# 接下来就可以根据时区和新得到的操作系统列表对数据进行分组了
by_tz_os = cframe.groupby(['tz', 'os'])
print(by_tz_os.size())
agg_counts = by_tz_os.size().unstack().fillna(0)
print(agg_counts[:10])
print(len(agg_counts))
print(agg_counts.sum(1))
# 最后，我们来选取最常出现的时区。为了达到这个目的，我根据agg_counts中的行数构造了一个间接索引数组
indexer = agg_counts.sum(1).argsort()
print(indexer[:10])
print(indexer[-10:])
# 然后我通过take按照这个顺序截取了最后10行最大值
count_subset = agg_counts.take(indexer[-10:])
print(count_subset)
# pandas有一个简便方法nlargest，可以做同样的工作
print(agg_counts.sum(1).nlargest(10))

# 然后，如这段代码所示，可以用柱状图表示。我传递一个额外参数到seaborn的barpolt函数，来画一个堆积条形图
# Rearrange the data for plotting
count_subset = count_subset.stack()
print(count_subset)
count_subset.name = 'total'
print(count_subset)
count_subset = count_subset.reset_index()
print(count_subset[:10])

flg, axes = plt.subplots(1, 1)
sns.barplot(y='tz', x='total', ax=axes, hue='os', data=count_subset)
flg.show()

# 这张图不容易看出Windows用户在小分组中的相对比例，因此标准化分组百分比之和为1
def norm_total(group):
    group['normed_total'] = group.total / group.total.sum()
    return group


results = count_subset.groupby('tz').apply(norm_total)
flg, axes = plt.subplots(1, 1)
sns.barplot(y='tz', x='normed_total', ax=axes, hue='os', data=results)
flg.show()
