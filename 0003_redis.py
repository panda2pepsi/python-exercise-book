# -*-coding:utf-8-*-

# 第 0003 题： 将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。

import redis

redis_conn = redis.Redis(host="localhost", port=6379, decode_responses=True)
coupon_file = r"E:\Codes\Python\Internet_Projects\Exercise Book\0001_coupon_out.txt"
key_prefix = "coupon"

def get_coupon_lists(filename):
    tmp = []
    try:
        with open(filename, "r") as f:
            for line in f.readlines():
                line = line.strip("\n")
                tmp.append(line)
            return tmp
    except FileNotFoundError:
        pass

coupon_list = get_coupon_lists(coupon_file)

def coupon_to_redis(lists, prefix):
    for i in lists:
        redis_conn.set(prefix+"_"+str(lists.index(i)), i)
        print(redis_conn[prefix+"_"+str(lists.index(i))])

coupon_to_redis(coupon_list, key_prefix)
print(len(redis_conn.keys()))