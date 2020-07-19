# -*-coding:utf-8-*-

# 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券）
# 使用 Python 如何生成 200 个激活码（或者优惠券）？

from uuid import uuid4

coupon_prefix = "0720REG"
coupon_list = []
coupon_qty = 200

def gen_coupon(qty, prefix):
    tmp_list = []
    tmp_coupon = ''
    while qty > 0:
        tmp_coupon = prefix + str(uuid4())[:6]
        if tmp_coupon not in tmp_list:
            tmp_list.append(tmp_coupon)
            qty -= 1
    return tmp_list

coupon_list = gen_coupon(coupon_qty, coupon_prefix)
print(coupon_list)
