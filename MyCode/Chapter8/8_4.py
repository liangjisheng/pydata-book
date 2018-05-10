# -*- coding:utf-8 -*-
"""
@project = 0424-1
@file = 8_4
@author = Liangjisheng
@create_time = 2018/4/24 0024 下午 20:37
"""
import pandas as pd
import numpy as np
# 有时候，DataFrame中的连接键位于其索引中。在这种情况下，你可以传入left_index=True或
# right_index=True（或两个都传）以说明索引应该被用作连接键
left1 = pd.DataFrame({'key': ['a', 'b', 'a', 'a', 'b', 'c'],
                      'value': range(6)})
right1 = pd.DataFrame({'group_val': [3.5, 7]}, index=['a', 'b'])
print(left1)
print(right1)
print(pd.merge(left1, right1, left_on='key', right_index=True))
# 由于默认的merge方法是求取连接键的交集，因此你可以通过外连接的方式得到它们的并集
print(pd.merge(left1, right1, left_on='key', right_index=True, how='outer'))
print()

# 对于层次化索引的数据，事情就有点复杂了，因为索引的合并默认是多键合并
lefth = pd.DataFrame({'key1': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
                      'key2': [2000, 2001, 2002, 2001, 2002],
                      'data': np.arange(5.)})
righth = pd.DataFrame(np.arange(12).reshape((6, 2)),
                      index=[['Nevada', 'Nevada', 'Ohio', 'Ohio', 'Ohio', 'Ohio'],
                             [2001, 2000, 2000, 2000, 2001, 2002]],
                      columns=['event1', 'event2'])
print(lefth)
print(righth)
# 这种情况下，你必须以列表的形式指明用作合并键的多个列（注意用how='outer'对重复索引值的处理）
print(pd.merge(lefth, righth, left_on=['key1', 'key2'], right_index=True))
print(pd.merge(lefth, righth, left_on=['key1', 'key2'], right_index=True, how='outer'))

# 同时使用合并双方的索引也没问题
left2 = pd.DataFrame([[1., 2.], [3., 4.], [5., 6.]],
                     index=['a', 'c', 'e'],
                     columns=['Ohio', 'Nevada'])
right2 = pd.DataFrame([[7., 8.], [9., 10.], [11., 12.], [13, 14]],
                      index=['b', 'c', 'd', 'e'],
                      columns=['Missouri', 'Alabama'])
print(left2)
print(right2)
print(pd.merge(left2, right2, how='outer', left_index=True, right_index=True))

# DataFrame还有一个便捷的join实例方法，它能更为方便地实现按索引合并。
# 它还可用于合并多个带有相同或相似索引的DataFrame对象，但要求没有重叠的列
print(left2.join(right2, how='outer'))
print()

# 因为一些历史版本的遗留原因，DataFrame的join方法默认使用的是左连接，保留左边表的行索引
# 它还支持在调用的DataFrame的列上，连接传递的DataFrame索引
print(left1)
print(right1)
print(left1.join(right1, on='key'))

# 最后，对于简单的索引合并，你还可以向join传入一组DataFrame，
# 下一节会介绍更为通用的concat函数，也能实现此功能
another = pd.DataFrame([[7., 8.], [9., 10.], [11., 12.], [16., 17.]],
                       index=['a', 'c', 'e', 'f'],
                       columns=['New York', 'Oregon'])
print(another)
print(left2.join([right2, another]))
print(left2.join([right2, another], how='outer'))
