# -*- coding:utf-8 -*-
"""
@project = 0422-1
@file = 6_7
@author = Liangjisheng
@create_time = 2018/4/22 0022 下午 12:08
"""
# 在商业场景下，大多数数据可能不是存储在文本或Excel文件中。
# 基于SQL的关系型数据库（如SQL Server、PostgreSQL和MySQL等）使用非常广泛
# 使用SQLite数据库（通过Python内置的sqlite3驱动器）
import sqlite3
query = """
CREATE TABLE test
(a VARCHAR(20), b VARCHAR(20),
c REAL, d INTEGER);"""

con = sqlite3.connect('mydata.sqlite')
print(con.execute(query))
con.commit()

# 然后插入几行数据
data = [('Atlanta', 'Georgia', 1.25, 6),
        ('Tallahassee', 'Florida', 2.6, 3),
        ('Sacramento', 'California', 1.7, 5)]
stmt = "INSERT INTO test VALUES(?, ?, ?, ?)"
print(con.executemany(stmt, data))

# 从表中选取数据时，大部分Python SQL驱动器（PyODBC、psycopg2、MySQLdb、pymssql等）
# 都会返回一个元组列表
cursor = con.execute('select * from test')
rows = cursor.fetchall()
print(rows)
