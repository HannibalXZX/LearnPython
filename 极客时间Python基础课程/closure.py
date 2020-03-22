# -*- coding:utf-8 -*-
#@Time  :    2020/3/21 13:53
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    closure.py
#@Description：


# 实现计数器

def counter():
    # 这里的列表为全局变量
    cnt = [0]
    # a = 0
    print("调用了counter函数")
    def add_one():
        print("调用了add_one函数")
        cnt[0] += 1
        # a += 1
        # return cnt[0]
        return a
    return add_one


if __name__ == '__main__':
    n = counter()
    print(n)
    print(n())
    # 每次调用后，
    print(n())
    # print(n())
    # print(n())
    # print(n())
    # print(n())