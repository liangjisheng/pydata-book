# -*- coding:utf-8 -*-
"""
@project = 0422-1
@file = 6_6
@author = Liangjisheng
@create_time = 2018/4/22 0022 下午 12:00
"""
# Web APIs交互, 许多网站都有一些通过JSON或其他格式提供数据的公共API。
# 通过Python访问这些API的办法有不少。一个简单易用的办法（推荐）是requests包
# 为了搜索最新的30个GitHub上的pandas主题，我们可以发一个HTTP GET请求
import requests
import pandas as pd
url = 'https://api.github.com/repos/pandas-dev/pandas/issues'
resp = requests.get(url)
print(resp)
# 响应对象的json方法会返回一个包含被解析过的JSON字典，加载到一个Python对象中
data = resp.json()
print(data[0]['title'])
print(type(data))
print(len(data))
print(type(data[0]))
# data中的每个元素都是一个包含所有GitHub主题页数据（不包含评论）的字典。
# 我们可以直接传递数据到DataFrame，并提取感兴趣的字段
issuse = pd.DataFrame(data, columns=['number', 'title', 'labels', 'state'])
print(issuse)
