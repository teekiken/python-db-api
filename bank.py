# -*- coding:utf-8 -*-
import sys
import MySQLdb

class TransMoney(object):
  def __init__(self,conn):     #1. 定义构造函数
    self.conn = conn

  def check_account(acctid):
    cursor = self.conn.cursor()
    try:       
      sql = "select * from account where acctid=%s"%acctid
      cursor.excute(sql)
      print "check account"
      rs = cursor.fetchall()
      if len(rs) != 1:
        raise Exception("账号%s不存在"%acctid)
    finally:
      cursor.close()

  def check_money(self,acctid,money):
    cursor = self.conn.cursor()
    try:       
      sql = "select * from account where acctid=%s and money > %s"%(acctid,money)
      cursor.excute(sql)
      print "check money"
      rs = cursor.fetchall()
      if len(rs) != 1:
        raise Exception("余额不足，无法转账")
    finally:
      cursor.close()

    def reduce_money(self,source_id,money):
        cursor = self.conn.cursor()
      try:       
        sql = "update account set money=money-%s where acctid=%s"%(money,acctid)
        cursor.excute(sql)
        print "reducing money"          
        if cursor.rowcount != 1:
          raise Exception("用户%s转账失败"%source_id)
      finally:
        cursor.close()

    def add_money(self,target_id,money):
      cursor = self.conn.cursor()
      try:       
        sql = "update account set money=money-%s where acctid=%s"%(money,acctid)
        cursor.excute(sql)
        print "reducing money"          
        if cursor.rowcount != 1:
          raise Exception("用户%s收款失败"%target_id)
      finally:
        cursor.close()

    def changeMoney(self,source_id,target_id,money):
      try:
        self.check_account(source_id)
        self.check_account(target_id)
        self.check_money(money)
        self.reduce_money(money)
        self.add_money(money)
        self.conn.commit()
      except Exception as e:
        self.conn.rollback()
        raise e


if __name__ =="__main__":
    source_id = sys.argv[1]
    aim_id=sys.argv[2]
    money=sys.argv[3]
    conn = MySQLdb.Connect(
      host='127.0.0.1',
      port=3306,
      user='root',
      passwd='root',
      db='test',
      charset='utf8'
      )
    trans = TransMoney(conn)
    
    try:
        trans.changeMoney(source_id,target_id,money)
    except Exception as e:
        print '出现问题'+str(e)
    finally:
        conn.close()