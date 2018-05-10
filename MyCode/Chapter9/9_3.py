# -*- coding:utf-8 -*-
"""
@project = 0426-1
@file = 9_3
@author = Liangjisheng
@create_time = 2018/4/26 0026 下午 19:34
"""
import matplotlib.pyplot as plt
import numpy as np
# 图例（legend）是另一种用于标识图表元素的重要工具。添加图例的方式有多种。
# 最简单的是在添加subplot的时候传入label参数
from numpy.random import randn
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
print(ax.plot(randn(1000).cumsum(), 'k', label='one'))
print(ax.plot(randn(1000).cumsum(), 'k--', label='two'))
print(ax.plot(randn(1000).cumsum(), 'k.', label='three'))
# 在此之后，你可以调用ax.legend()或plt.legend()来自动创建图例
ax.legend(loc='best')
fig.show()

# 图形的绘制要麻烦一些。matplotlib有一些表示常见图形的对象。这些对象被称为块（patch）
# 其中有些（如Rectangle和Circle），可以在matplotlib.pyplot中找到，
# 但完整集合位于matplotlib.patches
# 要在图表中添加一个图形，你需要创建一个块对象shp，
# 然后通过ax.add_patch(shp)将其添加到subplot中
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
rect = plt.Rectangle((0.2, 0.75), 0.4, 0.15, color='k', alpha=0.3)
circ = plt.Circle((0.7, 0.2), 0.15, color='b', alpha=0.3)
pgon = plt.Polygon([[0.15, 0.15], [0.35, 0.4], [0.2, 0.6]], color='g', alpha=0.5)
ax.add_patch(rect)
ax.add_patch(circ)
ax.add_patch(pgon)
fig.show()

# 利用plt.savefig可以将当前图表保存到文件。该方法相当于Figure对象的实例方法savefig
# 例如，要将图表保存为SVG文件，你只需输入:plt.savefig('figpath.svg')
plt.savefig('figpath.svg')
# 文件类型是通过文件扩展名推断出来的。因此，如果你使用的是.pdf，就会得到一个PDF文件
# 我在发布图片时最常用到两个重要的选项是dpi（控制“每英寸点数”分辨率）和bbox_inches
# (可以剪除当前图表周围的空白部分).要得到一张带有最小白边且分辨率为400DPI的PNG图片,你可以
plt.savefig('figpath.png', dpi=400, bbox_inches='tight')
# savefig并非一定要写入磁盘，也可以写入任何文件型的对象，比如BytesIO
from io import BytesIO
buffer = BytesIO()
plt.savefig(buffer)
plot_data = buffer.getvalue()
print(plot_data)
