# -*- coding:utf-8 -*-
#@Time  :    2020/3/11 17:54
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    class.py
#@Description：

class Counter(object):
    def __init__(self, start, stop):
        self.current = start
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.current > self.stop:
            raise StopIteration
        else:
            c = self.current
            self.current += 1
        return c

# 装饰器
def uppercase(func):
    def wrapper():
        original_result = func()
        modified_restult = original_result.upper()
        return modified_restult
    return wrapper

@uppercase
def an_output():
    return 'The quick brown fox jumps over the lazy dog.'
print(an_output())

def a():
    pass
def b():
    pass
def c():
    pass
def decorator(func):
    print('Start %s' % func)
    func()

def main():
    decorator(a)
    decorator(b)
    decorator(c)
if __name__ == '__main__':
    c = Counter(11, 12)
    print(next(c))
    print(next(c))
    print(next(c))
    for c in Counter(101, 105):
        print(c, end=', ')
    print(type(Counter))