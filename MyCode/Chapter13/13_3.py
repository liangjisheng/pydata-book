# -*- coding:utf-8 -*-
"""
@project = 0507-2
@file = 13_3
@author = Liangjisheng
@create_time = 2018/5/7 0007 下午 19:50
"""
import numpy as np
import pandas as pd
# 我们用pandas加载测试和训练数据集
train = pd.read_csv('datasets/titanic/train.csv')
test = pd.read_csv('datasets/titanic/test.csv')
# print(train[:4])
# statsmodels和scikit-learn通常不能接收缺失数据，因此我们要查看列是否包含缺失值
print(train.isnull().sum())
print(test.isnull().sum())

# 在统计和机器学习的例子中，根据数据中的特征，一个典型的任务是预测乘客能否生还。模型现在
# 训练数据集中拟合，然后用样本外测试数据集评估, 我想用年龄作为预测值，但是它包含缺失值。
# 缺失数据补全的方法有多种，我用的是一种简单方法，用训练数据集的中位数补全两个表的空值
impute_value = train['Age'].median()
train['Age'] = train['Age'].fillna(impute_value)
test['Age'] = test['Age'].fillna(impute_value)
# 现在我们需要指定模型。我增加了一个列IsFemale，作为“Sex”列的编码
train['IsFemale'] = (train['Sex'] == 'female').astype(int)
test['IsFemale'] = (test['Sex'] == 'female').astype(int)
# 然后，我们确定一些模型变量，并创建NumPy数组
predictors = ['Pclass', 'IsFemale', 'Age']
X_train = train[predictors].values
X_test = test[predictors].values
y_train = train['Survived'].values
print(X_train[:5])
print(y_train[:5])
print(test[:5])

# 我不能保证这是一个好模型，它的特征都符合。我们用scikit-learn的LogisticRegression模型，
# 创建一个模型实例
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
# 与statsmodels类似，我们可以用模型的fit方法，将它拟合到训练数据
print(model.fit(X_train, y_train))
# 现在，我们可以用model.predict，对测试数据进行预测
y_predict = model.predict(X_test)
print(y_predict[:10])
