# -*- coding:utf-8 -*-
"""
@project = 0427-1
@file = 10_1
@author = Liangjisheng
@create_time = 2018/4/27 0027 下午 20:23
"""
# Hadley Wickham（许多热门R语言包的作者）创造了一个用于表示分组运算的术语
# "split-apply-combine"（拆分－应用－合并）。第一个阶段，pandas对象
# (无论是Series、DataFrame还是其他的)中的数据会根据你所提供的一个或多个键被拆分(split)为多组
# 拆分操作是在对象的特定轴上执行的.例如DataFrame可以在其行(axis=0)或列(axis=1)上进行分组
# 然后，将一个函数应用（apply）到各个分组并产生一个新值。最后，所有这些函数的执行结果会
# 被合并（combine）到最终的结果对象中。结果对象的形式一般取决于数据上所执行的操作
import pandas as pd
import numpy as np

df = pd.DataFrame({'key1': ['a', 'a', 'b', 'b', 'a'],
                   'key2': ['one', 'two', 'one', 'two', 'one'],
                   'data1': np.random.randn(5),
                   'data2': np.random.randn(5)})
print(df)
# 假设你想要按key1进行分组，并计算data1列的平均值。实现该功能的方式有很多，
# 而我们这里要用的是：访问data1，并根据key1调用groupby
grouped = df['data1'].groupby(df['key1'])
print(grouped)
# 变量grouped是一个GroupBy对象。它实际上还没有进行任何计算，只是含有一些有关分组键df['key1']
# 的中间数据而已。换句话说，该对象已经有了接下来对各分组执行运算所需的一切信息。
# 例如，我们可以调用GroupBy的mean方法来计算分组平均值
print(grouped.mean())
# 稍后我将详细讲解.mean()的调用过程。这里最重要的是，数据（Series）根据分组键进行了聚合，
# 产生了一个新的Series，其索引为key1列中的唯一值。之所以结果中索引的名称为key1，
# 是因为原始DataFrame的列df['key1']就叫这个名字

# 如果我们一次传入多个数组的列表，就会得到不同的结果
mean = df['data1'].groupby([df['key1'], df['key2']]).mean()
print(mean)
# 这里，我通过两个键对数据进行了分组，得到的Series具有一个层次化索引（由唯一的键对组成）

# 转换最内层的列为行
print(mean.unstack())

# 在这个例子中，分组键均为Series。实际上，分组键可以是任何长度适当的数组
states = np.array(['Ohio', 'California', 'California', 'Ohio', 'Ohio'])
years = np.array([2005, 2005, 2006, 2005, 2006])
print(df['data1'].groupby([states, years]).mean())

# 通常，分组信息就位于相同的要处理DataFrame中。这里，你还可以将列名
# （可以是字符串、数字或其他Python对象）用作分组键

# 你可能已经注意到了，第一个例子在执行df.groupby('key1').mean()时，结果中没有key2列。
# 这是因为df['key2']不是数值数据（俗称“麻烦列”），所以被从结果中排除了。默认情况下，
# 所有数值列都会被聚合，虽然有时可能会被过滤为一个子集，稍后就会碰到
print(df.groupby('key1').mean())
print(df.groupby(['key1', 'key2']).mean())

# 无论你准备拿groupby做什么，都有可能会用到GroupBy的size方法，它可以返回一个含有分组大小的Series
print(df.groupby(['key1', 'key2']).size())

# GroupBy对象支持迭代，可以产生一组二元元组（由分组名和数据块组成）
print(df)
print(df.groupby('key1'))
for name, group in df.groupby('key1'):
    print(name)
    print(group)

# 对于多重键的情况，元组的第一个元素将会是由键值组成的元组
for (k1, k2), group in df.groupby(['key1', 'key2']):
    print((k1, k2))
    print(group)
print()

# 当然，你可以对这些数据片段做任何操作。有一个你可能会觉得有用的运算：将这些数据片段做成一个字典
print(list(df.groupby('key1')))
print(list(df.groupby('key1'))[0])
print(list(df.groupby('key1'))[1])
print()

for item in list(df.groupby('key1'))[0]:
    print(type(item))
    print(item)

pieces = dict(list(df.groupby('key1')))
print(pieces)
print(pieces['a'])
print(pieces['b'])

# groupby默认是在axis=0上进行分组的，通过设置也可以在其他任何轴上进行分组
# 拿上面例子中的df来说，我们可以根据dtype对列进行分组
print(df.dtypes)
grouped = df.groupby(df.dtypes, axis=1)
for dtype, group in grouped:
    print(dtype)
    print(group)

print(df.groupby('key1')['data1'])
print(list(df.groupby('key1')['data1']))
for name, group in list(df.groupby('key1')['data1']):
    print(type(name))
    print(name)
    print(type(group))
    print(group)
print()

print(df.groupby('key1')[['data1']])
print(list(df.groupby('key1')[['data1']]))
for name, group in list(df.groupby('key1')[['data1']]):
    print(type(name))
    print(name)
    print(type(group))
    print(group)
print()

print(df['data1'].groupby(df['key1']))
print(list(df['data1'].groupby(df['key1'])))
for name, group in list(df['data1'].groupby(df['key1'])):
    print(type(name))
    print(name)
    print(type(group))
    print(group)
print()

print(df[['data2']].groupby(df['key1']))
print(list(df[['data2']].groupby(df['key1'])))
for name, group in list(df[['data2']].groupby(df['key1'])):
    print(type(name))
    print(name)
    print(type(group))
    print(group)
print()

print(df)
print(type(df['data1']))
print(df['data1'])
print(type(df[['data1']]))
print(df[['data1']])

# 尤其对于大数据集，很可能只需要对部分列进行聚合。例如，在前面那个数据集中，
# 如果只需计算data2列的平均值并以DataFrame形式得到结果，可以这样写
print(df.groupby(['key1', 'key2'])[['data2']].mean())

# 这种索引操作所返回的对象是一个已分组的DataFrame（如果传入的是列表或数组）
# 或已分组的Series（如果传入的是标量形式的单个列名）
s_grouped = df.groupby(['key1', 'key2'])[['data2']]
print(s_grouped)
print(type(s_grouped.mean()))
print(s_grouped.mean())

s_grouped = df.groupby(['key1', 'key2'])['data2']
print(s_grouped)
print(type(s_grouped.mean()))
print(s_grouped.mean())
