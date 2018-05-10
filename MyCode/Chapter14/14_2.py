# -*- coding:utf-8 -*-
"""
@project = 0508-1
@file = test
@author = Liangjisheng
@create_time = 2018/5/9 0009 下午 18:50
"""
import pandas as pd
# make display smaller
pd.options.display.max_rows = 10
unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table('datasets/movielens/users.dat', sep='::',
                      header=None, names=unames)
rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('datasets/movielens/ratings.dat', sep='::',
                        header=None, names=rnames)
mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('datasets/movielens/movies.dat', sep='::',
                       header=None, names=mnames)

print(users[:5])
print(ratings[:5])
print(movies[:5])
data = pd.merge(pd.merge(ratings, users), movies)
print(data[:5])
print(data.iloc[0])
print(type(data.iloc[0]))

# 为了按性别计算每部电影的平均得分，我们可以使用pivot_table方法
mean_ratings = data.pivot_table('rating', index='title',
                                columns='gender', aggfunc='mean')
print(mean_ratings[:5])

# 现在，我打算过滤掉评分数据不够250条的电影（随便选的一个数字）。为了达到这个目的，
# 我先对title进行分组，然后利用size()得到一个含有各电影分组大小的Series对象
print(data['title'][:5])
ratings_by_title = data.groupby('title').size()
print(ratings_by_title[:10])
active_titles = ratings_by_title.index[ratings_by_title >= 250]
print(active_titles)

# 标题索引中含有评分数据大于250条的电影名称，然后我们就可以据此从前面的
# mean_ratings中选取所需的行了
mean_ratings = mean_ratings.loc[active_titles]
# 为了了解女性观众最喜欢的电影，我们可以对F列降序排列
top_female_ratings = mean_ratings.sort_values(by='F', ascending=False)
print(top_female_ratings[:10])

# 假设我们想要找出男性和女性观众分歧最大的电影。一个办法是给mean_ratings加上一
# 个用于存放平均得分之差的列，并对其进行排序
mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']
# 按"diff"排序即可得到分歧最大且女性观众更喜欢的电影
sorted_by_diff = mean_ratings.sort_values(by='diff')
print(sorted_by_diff[:10])
# 对排序结果反序并取出前10行，得到的则是男性观众更喜欢的电影
print(sorted_by_diff[::-1][:10])

# 如果只是想要找出分歧最大的电影（不考虑性别因素），则可以计算得分数据的方差或标准差
rating_std_by_title = data.groupby('title')['rating'].std()
rating_std_by_title = rating_std_by_title.loc[active_titles]
print(rating_std_by_title.sort_values(ascending=False)[:10])
