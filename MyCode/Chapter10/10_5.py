# -*- coding:utf-8 -*-
"""
@project = 0427-1
@file = 10_5
@author = Liangjisheng
@create_time = 2018/4/29 0029 上午 10:16
"""
import pandas as pd
import numpy as np
# 随机采样和排列,假设你想要从一个大数据集中随机抽取（进行替换或不替换）样本以进行
# 蒙特卡罗模拟（Monte Carlo simulation）或其他分析工作。“抽取”的方式有很多，
# 这里使用的方法是对Series使用sample方法
# Hearts, Spades, Clubs, Diamonds
suits = ['H', 'S', 'C', 'D']
card_val = (list(range(1, 11)) + [10] * 3) * 4
print(card_val[:13])
base_names = ['A'] + list(range(2, 11)) + ['J', 'K', 'Q']
cards = []
for suit in suits:
    cards.extend(str(num) + suit for num in base_names)
print(cards[:13])

deck = pd.Series(card_val, index=cards)
print(deck[:13])

# 现在我有了一个长度为52的Series，其索引包括牌名，值则是21点或其他游戏中用于计分的点数
# （为了简单起见，我当A的点数为1）
# 现在，根据我上面所讲的，从整副牌中抽出5张，代码如下
def draw(deck, n=5):
    return deck.sample(n)

print(draw(deck))
# 假设你想要从每种花色中随机抽取两张牌。由于花色是牌名的最后一个字符，
# 所以我们可以据此进行分组，并使用apply
get_suit = lambda card: card[-1]
print(deck.groupby(get_suit).apply(draw, n=2))
# 或者，也可以这样写
print(deck.groupby(get_suit, group_keys=False).apply(draw, n=2))
print()

# 分组加权平均数和相关系数,根据groupby的“拆分－应用－合并”范式，可以进行DataFrame的列与列之间
# 或两个Series之间的运算（比如分组加权平均）。以下面这个数据集为例，它含有分组键、值以及一些权重值
df = pd.DataFrame({'category': ['a'] * 4 + ['b'] * 4,
                   'data': np.random.randn(8),
                   'weights': np.random.rand(8)})
print(df)
# 然后可以利用category计算分组加权平均数
grouped = df.groupby('category')
get_wavg = lambda g: np.average(g['data'], weights=g['weights'])
print(grouped.apply(get_wavg))
print()

# 另一个例子，考虑一个来自Yahoo!Finance的数据集，其中含有几只股票和标准普尔500指数（符号SPX）
# 的收盘价
close_ex = pd.read_csv('stock_px_2.csv', parse_dates=True, index_col=0)
print(close_ex.head())
print(close_ex.info())
print(close_ex[-4:])

# 来做一个比较有趣的任务：计算一个由日收益率（通过百分数变化计算）与SPX之间的年度相关系数
# 组成的DataFrame。下面是一个实现办法，我们先创建一个函数，用它计算每列和SPX列的成对相关系数
spx_corr = lambda x: x.corrwith(x['SPX'])
# 接下来，我们使用pct_change计算close_px的百分比变化
rets = close_ex.pct_change().dropna()
print(rets.head())
# 最后，我们用年对百分比变化进行分组，可以用一个一行的函数，从每行的标签返回每个datetime
# 标签的year属性
get_year = lambda x: x.year
by_year = rets.groupby(get_year)
print(by_year.apply(spx_corr))

# 当然，你还可以计算列与列之间的相关系数。这里，我们计算Apple和Microsoft的年相关系数
print(by_year.apply(lambda g: g['AAPL'].corr(g['MSFT'])))

# 你可以用groupby执行更为复杂的分组统计分析，只要函数返回的是pandas对象或标量值即可。
# 例如，我可以定义下面这个regress函数（利用statsmodels计量经济学库）
# 对各数据块执行普通最小二乘法（Ordinary Least Squares，OLS）回归
import statsmodels.api as sm
def regress(data, yvar, xvars):
    Y = data[yvar]
    X = data[xvars]
    X['intercept'] = 1.
    result = sm.OLS(Y, X).fit()
    return result.params

# 现在，为了按年计算AAPL对SPX收益率的线性回归，执行
print(by_year.apply(regress, 'AAPL', ['SPX']))
