# -*- coding:utf-8 -*-
"""
@project = 0507-2
@file = 13_2
@author = Liangjisheng
@create_time = 2018/5/7 0007 下午 19:13
"""
import numpy as np
import pandas as pd
# statsmodels的线性模型有两种不同的接口：基于数组，和基于公式
import statsmodels.api as sm
import statsmodels.formula.api as smf
# 为了展示它们的使用方法，我们从一些随机数据生成一个线性模型
def dnorm(mean, variance, size=1):
    if isinstance(size, int):
        size = size
    return mean + np.sqrt(variance) * np.random.randn(size)

np.random.seed(12345)
N = 100
X = np.c_[dnorm(0, 0.4, size=N),
            dnorm(0, 0.6, size=N),
            dnorm(0, 0.2, size=N)]
eps = dnorm(0, 0.1, size=N)
beta = [0.1, 0.3, 0.5]
y = np.dot(X, beta) + eps

print(X[:5])
print(len(X))
print(y[:5])
print(len(y))

# 像之前Patsy看到的，线性模型通常要拟合一个截距。sm.add_constant函数
# 可以添加一个截距的列到现存的矩阵
X_model = sm.add_constant(X)
print(X_model[:5])

# sm.OLS类可以拟合一个普通最小二乘回归
model = sm.OLS(y, X)
# 这个模型的fit方法返回了一个回归结果对象，它包含估计的模型参数和其它内容
results = model.fit()
print(results.params)
# 对结果使用summary方法可以打印模型的详细诊断结果
print(results.summary())

# 这里的参数名为通用名x1, x2等等。假设所有的模型参数都在一个DataFrame中
# 现在，我们使用statsmodels的公式API和Patsy的公式字符串
data = pd.DataFrame(X, columns=['col0', 'col1', 'col2'])
data['y'] = y
print(data[:5])
results = smf.ols('y ~ col0 + col1 + col2', data=data).fit()
print(results.params)
print(results.tvalues)

# 给出一个样本外数据，你可以根据估计的模型参数计算预测值
print(results.predict(data[:5]))
