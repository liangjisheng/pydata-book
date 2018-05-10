# -*- coding:utf-8 -*-
"""
@project = 0419-1
@file = 6_1
@author = Liangjisheng
@create_time = 2018/4/19 0019 下午 19:35
"""
import pandas as pd
import os

# 由于该文件以逗号分隔，所以我们可以使用read_csv将其读入一个DataFrame：
df = pd.read_csv('ex1.csv')
print(df)
# 我们还可以使用read_table，并指定分隔符
print(pd.read_table('ex1.csv', sep=','))

# windows系统
os.system('type ex2.csv')
# Linux系统
# os.system('cat ex2.csv')
print()
# 读入ex2.csv的办法有两个。你可以让pandas为其分配默认的列名，也可以自己定义列名
file2 = 'ex2.csv'
names = ['a', 'b', 'c', 'd', 'message']
print(pd.read_csv(file2, header=None))
print(pd.read_csv(file2, names=names))

# 假设你希望将message列做成DataFrame的索引。你可以明确表示要将该列放到索引4的位置上
# 也可以通过index_col参数指定"message"
print(pd.read_csv(file2, names=names, index_col=names[4]))

# 如果希望将多个列做成一个层次化索引，只需传入由列编号或列名组成的列表即可
os.system('type csv_mindex.csv')
parsed = pd.read_csv('csv_mindex.csv', index_col=['key1', 'key2'])
print(parsed)

# 有些情况下，有些表格可能不是用固定的分隔符去分隔字段的(比如空白符或其它模式)
os.system('type ex3.csv')
print()
# 虽然可以手动对数据进行规整，这里的字段是被数量不同的空白字符间隔开的。
# 这种情况下，你可以传递一个正则表达式作为read_table的分隔符。可以用正则表达式表达为\s+
result = pd.read_table('ex3.csv', sep='\s+')
# 这里，由于列名比数据行的数量少，所以read_table推断第一列应该是DataFrame的索引
print(result)

# 这些解析器函数还有许多参数可以帮助你处理各种各样的异形文件格式
# 你可以用skiprows跳过文件的第一行、第三行和第四行
print(pd.read_csv('ex4.csv', skiprows=[0, 2, 3]))

# 缺失值处理是文件解析任务中的一个重要组成部分。缺失数据经常是要么没有（空字符串），
# 要么用某个标记值表示。默认情况下，pandas会用一组经常出现的标记值进行识别，比如NA及NULL
result = pd.read_csv('ex5.csv')
print(result)
print(pd.isnull(result))

# na_values可以用一个列表或集合的字符串表示缺失值
result = pd.read_csv('ex5.csv', na_values=['NULL'])
print(result)
# 字典的各列可以使用不同的NA标记值
sentinels = {'message': ['foo', 'NA'], 'something': ['two']}
print(pd.read_csv('ex5.csv', na_values=sentinels))
