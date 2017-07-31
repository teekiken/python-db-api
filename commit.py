# -*- coding:utf-8 -*-

import MySQLdb
print MySQLdb

conn = MySQLdb.Connect(
	host = '127.0.0.1',
	port = 3306,
	user =' root',
	passwd = '123456',
	db = 'imooc',
	charset = 'utf-8'
	)

cursor = conn.cursor()
sql_isnert = "insert into user(userid, username) values(10,"name10")"
sql_update = "update user set username='name91',where userid=9"
sql_delete = "delete from user where userid<3"

cursor.excute(sql_insert)
print cursor.rowcount
cursor.excute(sql_update)
print cursor.rowcount
cursor.excute(sql_delete)
print cursor.rowcount

conn.commit() #默认关闭自动提交，即conn.autocommit(False)，需要手动添加commit语句进行提交，与select语句不同




cursor.close()
conn.close()