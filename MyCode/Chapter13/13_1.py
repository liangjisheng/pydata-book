# -*- coding:utf-8 -*-
"""
@project = 0507-2
@file = 13_1
@author = Liangjisheng
@create_time = 2018/5/7 0007 下午 16:40
"""
# pandas与其它分析库通常是靠NumPy的数组联系起来的。将DataFrame转换为NumPy数组，
# 可以使用.values属性
import numpy as np
import pandas as pd
data = pd.DataFrame({'x0': [1, 2, 3, 4, 5],
                     'x1': [0.01, -0.01, 0.25, -4.1, 0.],
                     'y': [-1.5, 0., 3.6, 1.3, -2.]})
print(data)
print(data.columns)
print(data.values)
# 要转换回DataFrame，可以传递一个二维ndarray，可带有列名
df2 = pd.DataFrame(data.values, columns=['one', 'two', 'three'])
print(df2)

# 最好当数据是均匀的时候使用.values属性。例如，全是数值类型。如果数据是不均匀的，
# 结果会是Python对象的ndarray
df3 = data.copy()
df3['strings'] = ['a', 'b', 'c', 'd', 'e']
print(df3)
print(df3.values)

# 对于一些模型，你可能只想使用列的子集。我建议你使用loc，用values作索引
model_cols = ['x0', 'x1']
print(data.loc[:, model_cols].values)
print()

# 用Patsy创建模型描述, a+b不是将a与b相加的意思，而是为模型创建的设计矩阵。patsy.dmatrices
# 函数接收一个公式字符串和一个数据集(可以是DataFrame或数组的字典),为线性模型创建设计矩阵
import patsy
y, X = patsy.dmatrices('y ~ x0 + x1', data)
print(y)
print(X)
print(np.asarray(y))
print(np.asarray(X))

print(patsy.dmatrices('y ~ x0 + x1 + 0', data)[1])
# Patsy对象可以直接传递到算法（比如numpy.linalg.lstsq）中，它执行普通最小二乘回归
coef, resid, _, _ = np.linalg.lstsq(X, y)
print(coef)
coef = pd.Series(coef.squeeze(), index=X.design_info.column_names)
print(coef)

# 你可以将Python代码与patsy公式结合。在评估公式时，库将尝试查找在封闭作用域内使用的函数
y, X = patsy.dmatrices('y ~ x0 + np.log(np.abs(x1) + 1)', data)
print(X)

# 常见的变量转换包括标准化(平均值为0，方差为1)和中心化(减去平均值)
# Patsy有内置的函数进行这样的工作
y, X = patsy.dmatrices('y ~ standardize(x0) + center(x1)', data)
print(X)

# 作为建模的一步，你可能拟合模型到一个数据集，然后用另一个数据集评估模型。另一个数据集可能
# 是剩余的部分或是新数据。当执行中心化和标准化转变，用新数据进行预测要格外小心。因为你必须
# 使用平均值或标准差转换新数据集，这也称作状态转换
# patsy.build_design_matrices函数可以使用原始样本数据集的保存信息，来转换新数据
new_data = pd.DataFrame({'x0': [6, 7, 8, 9],
                         'x1': [3.1, -0.5, 0, 2.3],
                         'y': [1, 2, 3, 4]})
new_X = patsy.build_design_matrices([X.design_info], new_data)
print(new_X)

# 因为Patsy中的加号不是加法的意义，当你按照名称将数据集的列相加时，
# 你必须用特殊I函数将它们封装起来
y, X = patsy.dmatrices('y ~ I(x0 + x1)', data)
print(X)
