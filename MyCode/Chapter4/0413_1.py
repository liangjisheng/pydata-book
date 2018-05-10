# -*- coding:utf-8 -*-
"""
@project = 0411-2
@file = 0413_1
@author = Liangjisheng
@create_time = 2018/4/13 0013 下午 19:56
"""


def squares(n=10):
    print('Generating squares form 1 to {0}'.format(n ** 2))
    for i in range(1, n + 1):
        yield i ** 2


gen = squares()
print(gen)
for x in gen:
    print(x, end=' ')
print()

# 生成器表达式
gen1 = (x ** 2 for x in range(10))
print(gen1)
print(list(gen1))

print(sum(x ** 2 for x in range(100)))
print(dict((i, i ** 2) for i in range(5)))

import itertools
first_leter = lambda x: x[0]
names = ['Alan', 'Adam', 'Wes', 'Will', 'Albert', 'Steven']

# groupby可以接受任何序列和一个函数，它根据函数的返回值对序列中的连续元素进行分组
for letter, names in itertools.groupby(names, first_leter):
    print(letter, list(names))  # names is a generator
