# -*- coding:utf-8 -*-
#@Time  :    2020/3/13 23:15
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    regex.py
#@Description：


import re

str = 'begin began begun bigins begining'
pttn = r'beg[iau]n'
re.findall(pttn, str)