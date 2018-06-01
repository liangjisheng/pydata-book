# -*- coding:utf-8 -*-
"""
@project = 0411-2
@file = data_1
@author = Liangjisheng
@create_time = 2018/4/12 0012 下午 20:58
"""
import re
states = ['   Alabama ', 'Georgia!', 'Georgia', 'georgia', 'FlOrIda', 'south   carolina##', 'West virginia?']
# 去除空白符、删除各种标点符号、正确的大写格式等。做法之一是使用内建的字符串方法和正则表达式re模块


def clean_strings(strings):
    result = []
    for value in strings:
        value = value.strip()
        value = re.sub('[!#?]', '', value)
        value = value.title()
        result.append(value)

    return result


print(clean_strings(states))

# 另一种方法:将需要在一组给定字符串上执行的所有运算做成一个列表


def remove_punctuation(value):
    return re.sub('[!#?]', '', value)


clean_ops = [str.strip, remove_punctuation, str.title]


def clean_strings_1(strings, ops):
    result = []
    for value in strings:
        for function in ops:
            value = function(value)
        result.append(value)
    return result


print(clean_strings_1(states, clean_ops))

for x in map(remove_punctuation, states):
    print(x, end=' ')
print()

# 假设有一组字符串，你想要根据各字符串不同字母的数量对其进行排序
strings = ['foo', 'card', 'bar', 'aaaa', 'abab']
print(strings)
strings.sort(key=lambda x: len(set(list(x))))
print(strings)
