# -*- coding:utf-8 -*-
"""
@project = 0426-1
@file = 9_2
@author = Liangjisheng
@create_time = 2018/4/26 0026 下午 17:32
"""
import matplotlib.pyplot as plt
import numpy as np
# matplotlib的plot函数接受一组X和Y坐标，还可以接受一个表示颜色和线型的字符串缩写。
# 例如，要根据x和y绘制绿色虚线，你可以执行如下代码
# ax.plot(x, y, 'g--')
# 这种在一个字符串中指定颜色和线型的方式非常方便。在实际中，如果你是用代码绘图，
# 你可能不想通过处理字符串来获得想要的格式。通过下面这种更为明确的方式也能得到同样的效果
# ax.plot(x, y, linestyle='--', color='g')
# 线图可以使用标记强调数据点。因为matplotlib可以创建连续线图，在点之间进行插值，
# 因此有时可能不太容易看出真实数据点的位置。标记也可以放到格式字符串中，
# 但标记类型和线型必须放在颜色后面
from numpy.random import randn
data = randn(30)
print(data)
plt.plot(data.cumsum(), 'ko--')
plt.show()

# 还可以将其写成更为明确的形式
plt.plot(randn(30).cumsum(), color='k', linestyle='dashed', marker='o')
plt.show()

# 在线型图中，非实际数据点默认是按线性方式插值的。可以通过drawstyle选项修改
data = np.random.randn(30).cumsum()
print(plt.plot(data, 'k--', label='Default'))
print(plt.plot(data, 'k-', drawstyle='steps-post', label='steps-post'))
plt.legend(loc='best')
plt.show()

# 为了说明自定义轴，我将创建一个简单的图像并绘制一段随机漫步
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(np.random.randn(1000).cumsum())
fig.show()

# 要改变x轴刻度，最简单的办法是使用set_xticks和set_xticklabels。
# 前者告诉matplotlib要将刻度放在数据范围中的哪些位置，默认情况下，
# 这些位置也就是刻度标签。但我们可以通过set_xticklabels将任何其他的值用作标签
ticks = ax.set_xticks([0, 250, 500, 750, 1000])
labels = ax.set_xticklabels(['one', 'two', 'three', 'four', 'five'],
                            rotation=30, fontsize='small')
# rotation选项设定x刻度标签倾斜30度。最后，再用set_xlabel为X轴设置一个名称，
# 并用set_title设置一个标题
ax.set_title('My first matplotlib plot')
ax.set_xlabel('Stages')
fig.show()
# Y轴的修改方式与此类似，只需将上述代码中的x替换为y即可。轴的类有集合方法，
# 可以批量设定绘图选项。前面的例子，也可以写为
# props = {'title': 'My first matplotlib plot', 'xlable': 'Stages'}
# ax.set(**props)
