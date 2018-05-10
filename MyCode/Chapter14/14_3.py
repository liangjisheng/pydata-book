# -*- coding:utf-8 -*-
"""
@project = 0508-1
@file = 14_3
@author = Liangjisheng
@create_time = 2018/5/9 0009 下午 20:33
"""
import pandas as pd
import matplotlib.pyplot as plt
# 这些文件中仅含有当年出现超过5次的名字
names1880 = pd.read_csv('datasets/babynames/yob1880.txt',
                        names=['name', 'sex', 'births'])
# print(names1880)
print(type(names1880))
# 为了简单起见，我们可以用births列的sex分组小计表示该年度的births总计
print(names1880.groupby('sex').births.sum())

# 由于该数据集按年度被分隔成了多个文件，所以第一件事情就是要将所有数据都组装到
# 一个DataFrame里面，并加上一个year字段。使用pandas.concat即可达到这个目的
years = range(1880, 2011)
pieces = []
columns = ['name', 'sex', 'births']

for year in years:
    path = 'datasets/babynames/yob%d.txt' % year
    frame = pd.read_csv(path, names=columns)

    frame['year'] = year
    pieces.append(frame)
    # if year == 1880:
        # print(type(pieces))
        # print(len(pieces))
        # print(pieces[0])

print(type(pieces))
# Concatenate everything into a single DataFrame
names = pd.concat(pieces, ignore_index=True)
# print(names)
# 这里需要注意几件事情。第一，concat默认是按行将多个DataFrame组合到一起的
# 第二，必须指定ignore_index=True，因为我们不希望保留read_csv所返回的原始行号
# 现在我们得到了一个非常大的DataFrame，它含有全部的名字数据

# 有了这些数据之后，我们就可以利用groupby或pivot_table在year和sex级别上对其进行聚合了
total_births = names.pivot_table('births', index='year', columns='sex', aggfunc=sum)
print(total_births.tail())

fig, axes = plt.subplots(1, 1)
total_births.plot(title='Total births by sex and year', ax=axes)
# fig.show()
plt.show()

# 下面我们来插入一个prop列，用于存放指定名字的婴儿数相对于总出生数的比例。
# prop值为0.02表示每100名婴儿中有2名取了当前这个名字。因此，我们先按year和sex分组，
# 然后再将新列加到各个分组上
def add_prop(group):
    group['prop'] = group.births / group.births.sum()
    return group
names = names.groupby(['year', 'sex']).apply(add_prop)
# 现在，完整的数据集就有了下面这些列
print(names)
# 在执行这样的分组处理时，一般都应该做一些有效性检查，比如验证所有分组的prop的总和是否为1
print(names.groupby(['year', 'sex']).prop.sum())

# 工作完成。为了便于实现更进一步的分析，我需要取出该数据的一个子集：
# 每对sex/year组合的前1000个名字。这又是一个分组操作
def get_top1000(group):
    return group.sort_values(by='births', ascending=False)[:1000]
grouped = names.groupby(['year', 'sex'])
top1000 = grouped.apply(get_top1000)
# Drop the group index, not needed
top1000.reset_index(inplace=True, drop=True)
# 现在的结果数据集就小多了
print(top1000)

# 有了完整的数据集和刚才生成的top1000数据集，我们就可以开始分析各种命名趋势了
# 首先将前1000个名字分为男女两个部分
boys = top1000[top1000.sex == 'M']
girls = top1000[top1000.sex == 'F']
