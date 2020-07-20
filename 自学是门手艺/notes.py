# -*- coding:utf-8 -*-
#@Time  :    2020/2/24 16:49
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    str_notes.py
#@Description：

def other():
    divmod(11, 3) # (3, 2)
#
def _asicc():
    # 10 返回ASICC编码
    print(ord('\n'))
    #
    print(chr(10)) # 换行
    # 憨
    print(chr(25000))
    # ord('A') 65  ord('a') 97
def _strcode():
    '''
    编码流程
    string -> encode() -> bytes -> decode() -> string
    encode和decode默认的编码都是 utf-8
    '''
    # 字符串没有decode函数，只有encode() 二进制字符才能decode
    s = "哈"
    print(s.encode('unicode_escape'))
    print(s.encode('utf-8'))
    print(s.encode())
    print(s.encode().decode())
    print(b'\xe5\x93\x88'.decode())
    print(b'\xe5\x93\x88'.decode('unicode_escape'))

def _strip():
    s = "Simple is better than complex."
    # print(s.strip('Six.p'))
    # print(s.lstrip('Six.p'))
    # p 全部处理完之后，p 并不在尾部，所以原字符串中的 p 字母不受影响；
    # 跟字母顺序无关
    # print(s.strip('iS') )
    print(s.strip('pSix.mle'))
    print(s.strip('pSix.mle ') )

def _list():
    # c_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # # 拷贝一个列表
    # d_list = c_list.copy()
    # print(d_list)
    # del d_list[6:8]
    # print(d_list)  # [1, 2, 3, 4, 5, 6, 9, 10]
    # print(c_list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # # 对一个拷贝操作，不会更改 “原件”
    #
    # # 演示拷贝 .copy() 与赋值 = 的不同
    # e_list = d_list
    # del e_list[6:8]
    # print(e_list)   # [1, 2, 3, 4, 5, 6]
    # print(d_list)    # [1, 2, 3, 4, 5, 6]
    # # 对 e_list 操作，相等于对 d_list 操作

    # 更新，如果一个词典有重复的值，则取最后一个
    phonebook1 = {'ann': 6575, 'bob': 8982, 'joe': 2598, 'zoe': 1225, 'ann': 6585}
    phonebook2 = {'john': 9876, 'mike': 5603, 'stan': 6898, 'eric': 7898}

    phonebook1.update(phonebook2)
    print(phonebook1)

# 元组是不可变序列，所以，你没办法从里面删除元素。
# Tuple 相对于 List 占用更小的内存
def _tuple():
    a = 2,  # 注意这个末尾的逗号 , 它使得 a 变量被定义为一个元组，而不是数字
    print(type(a))
    b = 2  # 整数，赋值
    print(type(b))
    c = (2)  # 不是元组
    print(type(c))  # 还是 int
    d = (2,)  # 这才是元组
#     range(6) 就相当于 (0, 1, 2, 3, 4, 5)。

# 图形化界面
def _matp():
    # !pip install matplotlib
    # !pip install matplotlib-venn
    import matplotlib.pyplot as plt
    from matplotlib_venn import venn2

    admins = {'Moose', 'Joker', 'Joker'}
    moderators = {'Ann', 'Chris', 'Jane', 'Moose', 'Zero'}

    v = venn2(subsets=(admins, moderators), set_labels=('admins', 'moderators'))
    v.get_label_by_id('11').set_text('\n'.join(admins & moderators))
    v.get_label_by_id('10').set_text('\n'.join(admins - moderators))
    v.get_label_by_id('01').set_text('\n'.join(moderators - admins))

    plt.show()


if __name__ == '__main__':
    # _list()
    # _matp()
    _asicc()