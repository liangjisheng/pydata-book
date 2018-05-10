# -*- coding:utf-8 -*-
"""
@project = 0419-1
@file = 6_2
@author = Liangjisheng
@create_time = 2018/4/19 0019 下午 20:33
"""
import pandas as pd
import os
# os.system('ex6.csv')  # 会打开Notepad++默认文本编辑器
os.system('type ex6.csv')
print()

# 在看大文件之前，我们先设置pandas显示地更紧些
pd.options.display.max_rows = 10
file = 'ex6.csv'
result = pd.read_csv(file)
print(result)

# 如果只想读取几行（避免读取整个文件），通过nrows进行指定即可
print(pd.read_csv(file, nrows=5))
# 要逐块读取文件，可以指定chunksize（行数）
chunker = pd.read_csv(file, chunksize=8)
print(chunker)
print()

# read_csv所返回的这个TextFileReader对象使你可以根据chunksize对文件进行逐块迭代
# 比如说，我们可以迭代处理ex6.csv，将值计数聚合到"key"列中
tot = pd.Series([])
for piece in chunker:
    # print(piece)
    # print(piece['key'].value_counts())
    tot = tot.add(piece['key'].value_counts(), fill_value=0)
tot = tot.sort_values(ascending=False)
print(tot)
