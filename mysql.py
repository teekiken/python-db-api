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
sql = 'select * from user'
cursor.excute(sql)
print cursor.rowcount
rs = cursor.fetchone()
print rs
rs = cursor.fetchmany(3)
print rs
rs = cursor.fetchall(3) 	#返回元组
for row in rs:
	print "userid=%s, username=%s"%row

#print conn
#print cursor
cursor.close()
conn.close()