# -*- coding:utf-8 -*-
"""
@project = 0422-2
@file = 7_6
@author = Liangjisheng
@create_time = 2018/4/22 0022 下午 18:06
"""
import numpy as np
import pandas as pd
val = 'a,b,  guido'
# 以逗号分隔的字符串可以用split拆分成数段
print(val.split(','))
# split常常与strip一起使用，以去除空白符（包括换行符）
pieces = [x.strip() for x in val.split(',')]
print(pieces)
first, second, third = pieces
print(first + '::' + second + '::' + third)
# 但这种方式并不是很实用。一种更快更符合Python风格的方式是，向字符串"::"的join方法传入一个列表或元组
print('::'.join(pieces))
# 检测子串的最佳方式是利用Python的in关键字，还可以使用index和find
print('guido' in val)
# 注意find和index的区别：如果找不到字符串，index将会引发一个异常(而不是返回-1)
print(val.index(','))
print(val.find(':'))
# count可以返回指定子串的出现次数
print(val.count(','))
# replace用于将指定模式替换为另一个模式。通过传入空字符串，它也常常用于删除模式
print(val.replace(',', '::'))
print(val.replace(',', ''))
print()

import re
# 分隔符为数量不定的一组空白符（制表符、空格、换行符等）
text = "foo     bar\t baz  \tqux"
print(re.split('\s+', text))
# 调用re.split('\s+',text)时，正则表达式会先被编译，然后再在text上调用其split方法。
# 你可以用re.compile自己编译regex以得到一个可重用的regex对象
regex = re.compile('\s+')
print(regex)
print(type(regex))
print(regex.split(text))
# 如果只希望得到匹配regex的所有模式，则可以使用findall方法
print(regex.findall(text))

# match和search跟findall功能类似。findall返回的是字符串中所有的匹配项，
# 而search则只返回第一个匹配项。match更加严格，它只匹配字符串的首部。
# 来看一个小例子，假设我们有一段文本以及一条能够识别大部分电子邮件地址的正则表达式
text = """Dave dave@google.com
Steve steve@gmail.com
Rob rob@gmail.com
Ryan ryan@yahoo.com
"""
pattern = r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'
# re.IGNORECASE makes the regex case-insensitive
regex = re.compile(pattern, flags=re.IGNORECASE)
print(regex.findall(text))
# earch返回的是文本中第一个电子邮件地址（以特殊的匹配项对象形式返回）
# 对于上面那个regex，匹配项对象只能告诉我们模式在原字符串中的起始和结束位置
m = regex.search(text)
print(m)
print(text[m.start(): m.end()])
# regex.match则将返回None，因为它只匹配出现在字符串开头的模式
print(regex.match(text))
# 相关的，sub方法可以将匹配到的模式替换为指定字符串，并返回所得到的新字符串
print(regex.sub('REDACTED', text))
# 假设你不仅想要找出电子邮件地址，还想将各个地址分成3个部分：用户名、域名以及域后缀
# 要实现此功能，只需将待分段的模式的各部分用圆括号包起来即可
pattern = r'([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})'
regex = re.compile(pattern, flags=re.IGNORECASE)
# 由这种修改过的正则表达式所产生的匹配项对象，可以通过其groups方法返回一个由模式各段组成的元组
m = regex.match('wesm@bright.net')
print(m.groups())
# 对于带有分组功能的模式，findall会返回一个元组列表
print(regex.findall(text))
# sub还能通过诸如\1、\2之类的特殊符号访问各匹配项中的分组。符号\1对应第一个匹配的组，
# \2对应第二个匹配的组，以此类推
print(regex.sub(r'Username: \1, Domain: \2, Suffix: \3', text))

# pandas的矢量化字符串函数
data = {'Dave': 'dave@google.com', 'Steve': 'steve@gmail.com',
        'Rob': 'rob@gmail.com', 'Wes': np.nan}
data = pd.Series(data)
print(data)
print(data.isnull())
# 通过data.map，所有字符串和正则表达式方法都能被应用于（传入lambda表达式或其他函数）各个值，
# 但是如果存在NA（null）就会报错。为了解决这个问题，Series有一些能够跳过NA值的面向数组方法，
# 进行字符串操作。通过Series的str属性即可访问这些方法。例如，我们可以通过str.contains检查
# 各个电子邮件地址是否含有"gmail"
print(data.str.contains('gmail'))
print(pattern)
print(data.str.findall(pattern, flags=re.IGNORECASE))
# 有两个办法可以实现矢量化的元素获取操作：要么使用str.get，要么在str属性上使用索引
matches = data.str.match(pattern, flags=re.IGNORECASE)
print(matches)
print(matches.str.get(1))
print(matches.str[0])
print(data.str[:5])
