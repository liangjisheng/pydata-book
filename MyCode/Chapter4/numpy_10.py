# -*- coding:utf-8 -*-
"""
@project = 0411-2
@file = numpy_10
@author = Liangjisheng
@create_time = 2018/4/14 0014 下午 16:30
"""
# 使用np.random实现随机漫步
import numpy as np
nsteps = 1000
# 从给定的上下限范围内随机选择整数，不包括上限
draws = np.random.randint(0, 2, size=nsteps)
steps = np.where(draws > 0, 1, -1)
walk = steps.cumsum()

# 求最大值和最小值
print(walk.min())
print(walk.max())

# 现在来看一个复杂点的统计任务——首次穿越时间，即随机漫步过程中第一次到达某个特定值的时间
# 假设我们想要知道本次随机漫步需要多久才能距离初始0点至少10步远（任一方向均可）
# np.abs(walk)>=10可以得到一个布尔型数组，它表示的是距离是否达到或超过10，
# 而我们想要知道的是第一个10或－10的索引。可以用argmax来解决这个问题，
# 它返回的是该布尔型数组第一个最大值的索引（True就是最大值）
print((np.abs(walk) >= 10).argmax())
print()
# 注意，这里使用argmax并不是很高效，因为它无论如何都会对数组进行完全扫描
# 在本例中，只要发现了一个True，那我们就知道它是个最大值了

# 如果你希望模拟多个随机漫步过程（比如5000个），只需对上面的代码做一点点修改即
# 可生成所有的随机漫步过程。只要给numpy.random的函数传入一个二元元组就可以产生
# 一个二维数组，然后我们就可以一次性计算5000个随机漫步过程（一行一个）的累计和了
nwalks = 5000
nsteps = 1000
draws = np.random.randint(0, 2, size=(nwalks, nsteps))  # 0 or 1
steps = np.where(draws > 0, 1, -1)
walks = steps.cumsum(axis=1)
print(walks)

# 现在，我们来计算所有随机漫步过程的最大值和最小值：
print(walks.min())
print(walks.max())

# 得到这些数据之后，我们来计算30或－30的最小穿越时间。这里稍微复杂些，
# 因为不是5000个过程都到达了30。我们可以用any方法来对此进行检查
hits30 = (np.abs(walks) >= 30).any(1)
print(hits30)
print(hits30.sum())

# 然后我们利用这个布尔型数组选出那些穿越了30（绝对值）的随机漫步（行）
# 并调用argmax在轴1上获取穿越时间
corssing_time = (np.abs(walks[hits30]) >= 30).argmax(1)
print(corssing_time)
print(corssing_time.mean())
