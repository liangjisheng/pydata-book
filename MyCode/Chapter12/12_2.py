# -*- coding:utf-8 -*-
"""
@project = 0507-1
@file = 12_2
@author = Liangjisheng
@create_time = 2018/5/7 0007 下午 16:21
"""
import numpy as np
import pandas as pd
np.random.seed(12345)
draws = np.random.randn(1000)
print(draws[:5])
# 计算这个数据的分位面元，提取一些统计信息
bins = pd.qcut(draws, 4)
print(bins)
# 虽然有用，确切的样本分位数与分位的名称相比，不利于生成汇总。
# 我们可以使用labels参数qcut，实现目的
bins = pd.qcut(draws, 4, labels=['Q1', 'Q2', 'Q3', 'Q4'])
print(bins)
print(bins.codes[:10])
