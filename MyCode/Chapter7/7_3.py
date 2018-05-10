# -*- coding:utf-8 -*-
"""
@project = 0422-2
@file = 7_3
@author = Liangjisheng
@create_time = 2018/4/22 0022 下午 16:47
"""
# 跟Series中的值一样，轴标签也可以通过函数或映射进行转换，从而得到一个新的
# 不同标签的对象。轴还可以被就地修改，而无需新建一个数据结构
import pandas as pd
import numpy as np
data = pd.DataFrame(np.arange(12).reshape((3, 4)),
                    index=['Ohio', 'Colorado', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
print(data)
# 跟Series一样，轴索引也有一个map方法
transform = lambda x: x[:4].upper()
print(data.index.map(transform))
# 你可以将其赋值给index，这样就可以对DataFrame进行就地修改
data.index = data.index.map(transform)
print(data)
# 如果想要创建数据集的转换版（而不是修改原始数据），比较实用的方法是rename
print(data.rename(index=str.title, columns=str.upper))
# 特别说明一下，rename可以结合字典型对象实现对部分轴标签的更新
print(data.rename(index={"OHIO": 'INDIANA'}, columns={'three': 'peekboo'}))
print()

# 为了便于分析，连续数据常常被离散化或拆分为“面元”（bin）
# 假设有一组人员数据，而你希望将它们划分为不同的年龄组
ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
# 接下来将这些数据划分为“18到25”、“26到35”、“35到60”以及“60以上”几个面元。
# 要实现该功能，你需要使用pandas的cut函数
bins = [18, 25, 35, 60, 100]
cats = pd.cut(ages, bins)
print(cats)

# pandas返回的是一个特殊的Categorical对象。结果展示了pandas.cut划分的面元。
# 你可以将其看做一组表示面元名称的字符串。它的底层含有一个表示不同分类名称的类型数组，
# 以及一个codes属性中的年龄数据的标签
print(cats.codes)
print(cats.categories)
# pd.value_counts(cats)是pandas.cut结果的面元计数
print(pd.value_counts(cats))
# 跟“区间”的数学符号一样，圆括号表示开端，而方括号则表示闭端（包括）
# 哪边是闭端可以通过right=False进行修改
print(pd.cut(ages, [18, 26, 36, 61, 100], right=False))
# 你可以通过传递一个列表或数组到labels，设置自己的面元名称
group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']
print(pd.cut(ages, bins, labels=group_names))
# 如果向cut传入的是面元的数量而不是确切的面元边界，则它会根据数据的最小值和最大值计算等长面元
# 下面这个例子中，我们将一些均匀分布的数据分成四组
data = np.random.randn(20)
print(pd.cut(data, 4, precision=2))

# qcut是一个非常类似于cut的函数，它可以根据样本分位数对数据进行面元划分。根据数据的分布情况，
# cut可能无法使各个面元中含有相同数量的数据点。而qcut由于使用的是样本分位数，
# 因此可以得到大小基本相等的面元
data = np.random.randn(1000)
cats = pd.qcut(data, 4, precision=2)
print(cats)
print(pd.value_counts(cats))
# 与cut类似，你也可以传递自定义的分位数（0到1之间的数值，包含端点）
print(pd.qcut(data, [0, 0.1, 0.5, 0.9, 1.]))
