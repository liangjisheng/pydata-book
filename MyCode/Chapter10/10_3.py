# -*- coding:utf-8 -*-
"""
@project = 0427-1
@file = 10_3
@author = Liangjisheng
@create_time = 2018/4/28 0028 下午 15:56
"""
import pandas as pd
import numpy as np
# 聚合指的是任何能够从数组产生标量值的数据转换过程。之前的例子已经用过一些，
# 比如mean、count、min以及sum等. 你可以使用自己发明的聚合运算，还可以调用分组对象上已经定义好
# 的任何方法。例如，quantile可以计算Series或DataFrame列的样本分位数
# 虽然quantile并没有明确地实现于GroupBy，但它是一个Series方法，所以这里是能用的。实际上，
# GroupBy会高效地对Series进行切片，然后对各片调用piece.quantile(0.9)，
# 最后将这些结果组装成最终结果

df = pd.DataFrame({'key1': ['a', 'a', 'b', 'b', 'a'],
                   'key2': ['one', 'two', 'one', 'two', 'one'],
                   'data1': np.random.randn(5),
                   'data2': np.random.randn(5)})
print(df)
grouped = df.groupby('key1')
for name, group in grouped:
    print(name)
    print(type(group))
    print(group)
print()

for name, group in grouped['data1']:
    print(name)
    print(type(group))
    print(group)
    print(group.quantile(0.9))
print()

print(grouped['data1'].quantile(0.9))

# 如果要使用你自己的聚合函数，只需将其传入aggregate或agg方法即可
# 自定义聚合函数要比表10-1中那些经过优化的函数慢得多。这是因为在构造中间分组数据块时
# 存在非常大的开销（函数调用、数据重排等）
def peak_to_peak(arr):
    return arr.max() - arr.min()
print(grouped.agg(peak_to_peak))

# 你可能注意到注意，有些方法（如describe）也是可以用在这里的，即使严格来讲，它们并非聚合运算
print(grouped.describe())
print(grouped['data1'].describe())
print()

# 回到前面小费的例子。使用read_csv导入数据之后，我们添加了一个小费百分比的列tip_pct
tips = pd.read_csv('tips.csv')
# Add tip percentage of total bill
tips['tip_pct'] = tips['tip'] / tips['total_bill']
print(tips.head())

# 你已经看到，对Series或DataFrame列的聚合运算其实就是使用aggregate（使用自定义函数）
# 或调用诸如mean、std之类的方法。然而，你可能希望对不同的列使用不同的聚合函数，
# 或一次应用多个函数。其实这也好办，我将通过一些示例来进行讲解。首先，
# 我根据天和smoker对tips进行分组
grouped = tips.groupby(['day', 'smoker'])
grouped_pct = grouped['tip_pct']
print(grouped_pct.head())
# 可以将函数名以字符串的形式传入
print(grouped_pct.agg('mean'))

# 如果传入一组函数或函数名，得到的DataFrame的列就会以相应的函数命名
# 这里，我们传递了一组聚合函数进行聚合，独立对数据分组进行评估
print(grouped_pct.agg(['mean', 'std', peak_to_peak]))

# 你并非一定要接受GroupBy自动给出的那些列名，特别是lambda函数，它们的名称是'<lambda>'，
# 这样的辨识度就很低了（通过函数的name属性看看就知道了）。因此，如果传入的是一个由
# (name,function)元组组成的列表，则各元组的第一个元素就会被用作DataFrame的列名
# （可以将这种二元元组列表看做一个有序映射）
print(grouped_pct.agg([('foo', 'mean'), ('bar', np.std)]))
print()

# 对于DataFrame，你还有更多选择，你可以定义一组应用于全部列的一组函数，或不同的列应用不同的函数
# 假设我们想要对tip_pct和total_bill列计算三个统计信息
functions = ['count', 'mean', 'max']
result = grouped['tip_pct', 'total_bill'].agg(functions)
# 如你所见，结果DataFrame拥有层次化的列，这相当于分别对各列进行聚合，然后用concat将结果
# 组装到一起，使用列名用作keys参数
print(result)
print(result['tip_pct'])

# 跟前面一样，这里也可以传入带有自定义名称的一组元组
ftuples = [('Durchschnitt', 'mean'), ('Abweichung', np.var)]
print(grouped['tip_pct', 'total_bill'].agg(ftuples))

# 现在，假设你想要对一个列或不同的列应用不同的函数。具体的办法是向agg
# 传入一个从列名映射到函数的字典
# 只有将多个函数应用到至少一列时，DataFrame才会拥有层次化的列
print(grouped.agg({'tip': np.max, 'size': 'sum'}))
print(grouped.agg({'tip': ['min', 'max', 'mean', 'std'], 'size': 'sum'}))

# 到目前为止，所有示例中的聚合数据都有由唯一的分组键组成的索引（可能还是层次化的）
# 由于并不总是需要如此，所以你可以向groupby传入as_index=False以禁用该功能
print(tips.groupby(['day', 'smoker'], as_index=False).mean())

# 回到之前那个小费数据集，假设你想要根据分组选出最高的5个tip_pct值
# 首先，编写一个选取指定列具有最大值的行的函数
def top(df, n=5, column='tip_pct'):
    return df.sort_values(by=column)[-n:]

print(top(tips, n=6))
print(tips.head())
# 现在，如果对smoker分组并用该函数调用apply，就会得到
# 这里发生了什么？top函数在DataFrame的各个片段上调用，然后结果由pandas.concat组装到一起
# 并以分组名称进行了标记。于是，最终结果就有了一个层次化索引，其内层索引值来自原DataFrame
print(tips.groupby('smoker').apply(top))

# 如果传给apply的函数能够接受其他参数或关键字，则可以将这些内容放在函数名后面一并传入
print(tips.groupby(['smoker', 'day']).apply(top, n=1, column='total_bill'))
print()

result = tips.groupby('smoker')['tip_pct'].describe()
print(result)
print(result.unstack('smoker'))

# 从上面的例子中可以看出，分组键会跟原始对象的索引共同构成结果对象中的层次化索引
# 将group_keys=False传入groupby即可禁止该效果
print(tips.groupby('smoker', group_keys=False).apply(top))
