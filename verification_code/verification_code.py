#coding:utf-8
#**第 0001 题：**做为 Apple Store App 独立开发者，你要搞限时促销
#为你的应用**生成激活码**（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）
#脚本涉及到两个标准库random，简单教程：http://fulerbakesi.iteye.com/blog/1589097
#string，简单教程：http://www.cnblogs.com/iwalkfreely/p/4714866.html,   http://biancheng.dnbcw.info/python/455071.html

#生成****-****-****-****格式的激活码

import random, string
import os

#存储器，实现数据的存取
#p.dump(保存内容, 文件对象)
#p.load(文件对象)
#import cPickle as p  

result = 'Verification_codes.txt'
#基础字母和数字
chars = string.letters + string.digits

#获得四个字母和数字的随机组合
def getRandom():
    return ''.join(random.sample(chars, 4))

#每个验证码由四段四元组组成
def construct(group=4):
    return '-'.join([getRandom() for i in range(group)])

def generate(num):
    return [construct() for i in range(num)]

if __name__ == '__main__':
    f = open(result, 'w')
    codes = generate(200)
    code = os.sep.join(codes)
    print code
    f.write(os.sep.join(codes))
    f.close()
