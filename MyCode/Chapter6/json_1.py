# -*- coding:utf-8 -*-
"""
@project = 0422-1
@file = json_1
@author = Liangjisheng
@create_time = 2018/4/22 0022 上午 10:16
"""
import json
import pandas as pd
import os
obj = """
{"name": "Wes",
"places_lived": ["United States", "Spain", "Germany"],
"pet": null,
"siblings": [{"name": "Scott", "age": 30, "pets": ["Zeus", "Zuko"]},
             {"name": "Katie", "age": 38, "pets": ["Sixes", "Stache", "Cisco"]}]
}
"""
# 除其空值null和一些其他的细微差别（如列表末尾不允许存在多余的逗号）之外，
# JSON非常接近于有效的Python代码。基本类型有对象（字典）、数组（列表）、字符串、
# 数值、布尔值以及null。对象中所有的键都必须是字符串。许多Python库都可以读写JSON数据。
# 我将使用json，因为它是构建于Python标准库中的。
# 通过json.loads即可将JSON字符串转换成Python形式：
result = json.loads(obj)
print(result)
# json.dumps则将Python对象转换成JSON格式：
asjson = json.dumps(result)
print(asjson)
# 最简单方便的方式是：向DataFrame构造器传入一个字典的列表（就是原先的JSON对象），
# 并选取数据字段的子集
siblings = pd.DataFrame(result['siblings'], columns=['name', 'age'])
print(siblings)

# pandas.read_json可以自动将特别格式的JSON数据集转换为Series或DataFrame
# pandas.read_json的默认选项假设JSON数组中的每个对象是表格中的一行
os.system('type ex1.json')
print()
data = pd.read_json('ex1.json')
print(data)
# 如果你需要将数据从pandas输出到JSON，可以使用to_json方法
print(data.to_json())
print(data.to_json(orient='records'))

# Performance_MNR.xml
# 利用lxml.objectify解析该文件，然后通过getroot得到该XML文件的根节点的引用
from lxml import objectify
parsed = objectify.parse(open('Performance_MNR.xml'))
print(parsed)
print(type(parsed))
root = parsed.getroot()
print(root)
print(type(root))

data = []
skip_fields = ['PARENT_SEQ', 'INDICATOR_SEQ', 'DESIRED_CHANGE', 'DECIMAL_PLACES']
# root.INDICATOR返回一个用于产生各个<INDICATOR>XML元素的生成器
# print(root.INDICATOR_SEQ)
for elt in root:
    el_data = {}
    for child in elt.getchildren():
        # print(child.tag)
        # print(child.pyval)
        # print()
        # if child.tag in skip_fields:
            # continue
        el_data[child.tag] = child.pyval
    print(el_data)
    data.append(el_data)

print(data)
# 最后，将这组字典转换为一个DataFrame
perf = pd.DataFrame(data)
print(perf)
print()
print(perf.head())
print()

# XML数据可以比本例复杂得多。每个标记都可以有元数据。看看下面这个HTML的链接标签
# （它也算是一段有效的XML）
from io import StringIO
tag = '<a href="http://www.baidu.com">baidu</a>'
root = objectify.parse(StringIO(tag)).getroot()
# 现在就可以访问标签或链接文本中的任何字段了（如href）：
print(root)
print(root.get('href'))
print(root.text)
