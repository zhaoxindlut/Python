#coding:utf-8
#**第 0001 题：**做为 Apple Store App 独立开发者，你要搞限时促销
#为你的应用**生成激活码**（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）
#脚本涉及到两个标准库random，简单教程：http://fulerbakesi.iteye.com/blog/1589097
#string，简单教程：http://www.cnblogs.com/iwalkfreely/p/4714866.html,   http://biancheng.dnbcw.info/python/455071.html

import random, string
import cPickle as p

result = 'Verification_codes.txt'
def random_str(num, length = 7):
    f = open(result, 'wb')
    for i in range(num):
        chars = string.letters + string.digits
        s = [random.choice(chars) for join in range(length)]
        #s.insert(0, str(i+1))
        #print ''.join(s)
        #p.dump(''.join(s), f)  #保存结果在格式上存在问题
        f.write(''.join(s) + '\n')
    f.close()

if __name__ == '__main__':
    random_str(200)