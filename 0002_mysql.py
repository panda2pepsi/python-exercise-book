# -*-coding:utf-8-*-

# 第 0002 题: 将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。

import pymysql
from datetime import datetime
import time

mysql_db = pymysql.connect("localhost", "root", "panda2pepsi", "py_exercise_book")
mysql_cursor = mysql_db.cursor()
sql_table = """CREATE TABLE IF NOT EXISTS COUPON(
            coupon_id INT AUTO_INCREMENT,
            coupon_key VARCHAR(15) UNIQUE NOT NULL,
            coupon_active DATE,
            coupon_inactive DATE,
            coupon_gen_time TIMESTAMP,
            coupon_used TINYINT,
            PRIMARY KEY (coupon_id))"""

mysql_cursor.execute(sql_table)
coupon_file = r"E:\Codes\Python\Internet_Projects\Exercise Book\0001_coupon_out.txt"
coupon_active = "2020-07-22"
coupon_inactive = "2020-08-22"

def get_coupon_keys(filename):
    tmp = []
    try:
        with open(filename, "r") as f:
            for line in f.readlines():
                line = line.strip("\n")
                tmp.append(line)
            return tmp
    except FileNotFoundError:
        pass

coupon_lists = get_coupon_keys(coupon_file)

def coupon_to_mysql(active, inactive, lists):
    for i in lists:
        sql = "INSERT INTO COUPON( \
            coupon_key, coupon_active, coupon_inactive, coupon_used) \
            VALUES('%s', '%s', '%s', '%s')" % \
            (i, active, inactive, 0)
        print(sql)
        try:
            mysql_cursor.execute(sql)
            mysql_db.commit()
            print("success")
        except:
            mysql_db.rollback()

coupon_to_mysql(coupon_active, coupon_inactive, coupon_lists)
mysql_db.close()