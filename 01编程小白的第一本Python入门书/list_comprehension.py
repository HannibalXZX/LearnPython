# -*- coding:utf-8 -*-
#@Time  :    2019/11/2 4:53 PM
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    list_comprehension.py


def basic_info():
    # list = [item for item in iterable]
    a = [i**2 for i in range(10)]
    c = [n for n in range(1,10) if n % 2 ==0]
    #print(a)
    #letters = ['a','b','c','d','e','f','g']
    letters = [letter.lower() for letter in 'ABCDEFGHIJKLMN']
    for num,letter in enumerate(letters):
        print(letter,'is',num+1)


#比较效率
import  time
def compare_effience():
    a = []
    #t0 = time.clock()
    #time.clock has been deprecated in Python 3.3 and will be removed from Python 3.8: use time.perf_counter or time.process_time instead
    t0 = time.process_time()
    for i in range(1,200000):
        a.append(i)
    print(time.process_time()-t0,"seconds process time") #0.108708

    t1 = time.process_time()
    b = [i for i in range(1,200000)]
    print(time.process_time()-t1,"seconds process time") #0.019594


#项目——词频统计
#文本下载地址:http://pan.baidu.com/s/1075GKZ4
import string
def Word_():
    # path = 'data/Walden.txt'
    # with open(path,'r') as text:
    #     words = [raw_word.strip(string.punctuation).lower()for raw_word in text.read().split()]
    #     words_index = set(words)
    #     counts_dict = {index:words.count(index) for index in words_index}git config core.excludesfile .idea


    print(string.punctuation) #


    # for word in sorted(counts_dict,key=lambda  x:counts_dict[x],reverse=True):
    #     print('{} -- {} times '.format(word,counts_dict[word]))


if __name__ == '__main__':
    basic_info()
    #compare_effience()
    print("列表效率高")