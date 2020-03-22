# -*- coding:utf-8 -*-
#@Time  :    2020/3/8 14:55
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    function.py
#@Description：涉及到函数相关

# 杂乱的知识点在这里
def _all():
    import keyword
    print(keyword.kwlist)
#     函数返回对象的唯一标识符，标识符是一个整数。
    print(id())

# 是把 names 这个参数当作容器处理
def say_hi(*names):
    for name in names:
        print(f'Hi, {name}!')

# ** must be a mapping
def say_hi_2(**names):
    for name in names:
        print(f'Hi, {name}!')

# lambda_expr ::= "lambda" [parameter_list] ":" expression
def _lambda():
    add = lambda x, y : x+y
    print(add(1,2))
    f = make_incrementor(10)
    print(f(2))
    f = make_incrementor(13)
    print(f(2))


def square(x):
    return x**2

# map() 会根据提供的函数对指定序列做映射。
# map(function, iterable, ...)
def _map():
    a = [1, 2, 3, 4, 5]
    print(list(map(square, a)))
    print(list(map(lambda x: x**2, a)))
    pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
    f = lambda p: p[1]
    print(f([1,2]))
    # 该函数可以用来对字典进行排序
    pairs.sort(key=lambda p: p[0])
    print(pairs)



def make_incrementor(n):
    return lambda x: x + n

if __name__ == '__main__':
    # names = ('mike', 'john', 'zeo')
    # say_hi(*names)
    # names_2 = {'name': 'mike', 'john':'name'}
    # say_hi_2(**names_2)
    # _all()
    # _lambda()
    _map()