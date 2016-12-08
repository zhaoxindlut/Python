#!/usr/bin/python
#coding:utf-8
#将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
import MySQLdb as db
import verification_code

HOST = 'localhost'
USER = 'root'
PASSWORD = ''
PORT = 3306
DB = 'python'

#连接数据库
conn = db.connect(
    host = HOST,
    user = USER,
    passwd = PASSWORD,
    port = PORT,
    db = DB 
)

#调用cursor()方法生成查询管理对象
cur = conn.cursor()
#创建表用于保存激活码
AAA = 'CREATE TABLE IF NOT EXISTS code(code VARCHAR(50))'
cur.execute(AAA)
#生成激活码
codelist = verification_code.generate(200)
#将生成的激活码插入数据库中
for i in xrange(200):
    sql = 'INSERT INTO code (code) VALUES (\'%s\')' % codelist[i]
    cur.execute(sql)

conn.commit()
cur.close()
conn.close()
