# -*- coding: utf-8 -*-

import os, sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

# 初始数据:
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()

def get_score_in(low, high):
#    ' 返回指定分数区间的名字，按分数从低到高排序 '
	L = []
	conn = sqlite3.connect(db_file)
	cursor=conn.cursor()
	cursor.execute('select * from user where score between ? and ?',(low,high))
	values = cursor.fetchall()
	values_sorted = sorted(values,key=lambda i:i[2])
	for i in values_sorted:
		L.append(i[1])
	return L

print get_score_in(0,100)
