# -*- coding:utf-8 -*-
"""
@project = 0422-1
@file = 6_5
@author = Liangjisheng
@create_time = 2018/4/22 0022 上午 11:49
"""
import pandas as pd
# pandas的ExcelFile类或pandas.read_excel函数支持读取存储在Excel 2003（或更高版本）中的表格型数据
# 要使用ExcelFile，通过传递xls或xlsx路径创建一个实例
xlsx = pd.ExcelFile('ex1.xlsx')
# 存储在表单中的数据可以read_excel读取到DataFrame
frame = pd.read_excel(xlsx, 'Sheet1')
print(frame)
# 如果要读取一个文件中的多个表单，创建ExcelFile会更快，但你也可以将文件名传递到pandas.read_excel
f2 = pd.read_excel('ex1.xlsx', 'Sheet1')
print(f2)

# 如果要将pandas数据写入为Excel格式，你必须首先创建一个ExcelWriter，
# 然后使用pandas对象的to_excel方法将数据写入到其中
writer = pd.ExcelWriter('ex2.xlsx')
frame.to_excel(writer, 'Sheet1')
writer.save()
# 你还可以不使用ExcelWriter，而是传递文件的路径到to_excel
# frame.to_excel('ex2.xlsx')
