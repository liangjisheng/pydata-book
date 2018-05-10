# -*- coding:utf-8 -*-
"""
@project = 0426-1
@file = 9_1
@author = Liangjisheng
@create_time = 2018/4/26 0026 下午 16:52
"""
import matplotlib.pyplot as plt
import numpy as np
data = np.arange(10)
print(data)
plt.plot(data)
plt.show()

# matplotlib的图像都位于Figure对象中。你可以用plt.figure创建一个新的Figure
fig = plt.figure()
# 不能通过空Figure绘图。必须用add_subplot创建一个或多个subplot才行
# 这条代码的意思是：图像应该是2×2的（即最多4张图），且当前选中的是4个subplot中的第一个（编号从1开始）
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
# 如果这时执行一条绘图命令, matplotlib就会在最后一个用过的subplot（如果没有则创建一个）
# 上进行绘制，隐藏创建figure和subplot的过程
# "k--"是一个线型选项，用于告诉matplotlib绘制黑色虚线图
plt.plot(np.random.randn(50).cumsum(), 'k--')
# 上面那些由fig.add_subplot所返回的对象是AxesSubplot对象，直接调用它们的实例方法
# 就可以在其它空着的格子里面画图了
_ = ax1.hist(np.random.randn(100), bins=20, color='k', alpha=0.3)
ax2.scatter(np.arange(30), np.arange(30) + 3 * np.random.randn(30))
fig.show()

# 创建包含subplot网格的figure是一个非常常见的任务，matplotlib有一个更为方便的方法
# plt.subplots，它可以创建一个新的Figure，并返回一个含有已创建的subplot对象的NumPy数组
fig, axes = plt.subplots(2, 3)
print(axes)

# 默认情况下，matplotlib会在subplot外围留下一定的边距，并在subplot之间留下一定的间距。
# 间距跟图像的高度和宽度有关，因此，如果你调整了图像大小（不管是编程还是手工），
# 间距也会自动调整。利用Figure的subplots_adjust方法可以轻而易举地修改间距，
# 此外，它也是个顶级函数
# subplots_adjust(left=None, bottom=None, right=None, top=None,
#                 wspace=None, hspace=None)
# wspace和hspace用于控制宽度和高度的百分比，可以用作subplot之间的间距。
# 下面是一个简单的例子，其中我将间距收缩到了0
fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)
for i in range(2):
    for j in range(2):
        axes[i, j].hist(np.random.randn(500), bins=50, color='k', alpha=0.5)
plt.subplots_adjust(wspace=0, hspace=0)
fig.show()
# 不难看出，其中的轴标签重叠了。matplotlib不会检查标签是否重叠，所以对于这种情况，
# 你只能自己设定刻度位置和刻度标签。后面几节将会详细介绍该内容
