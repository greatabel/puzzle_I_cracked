'''
A row of five grey square tiles is to have a number of its tiles replaced with 
coloured oblong tiles chosen from red (length two), green (length three), or blue (length four).

If red tiles are chosen there are exactly seven ways this can be done.

png116_1.png
If green tiles are chosen there are three ways.

png116_2.png
And if blue tiles are chosen there are two ways.

png116_3.png
Assuming that colours cannot be mixed there are 7 + 3 + 2 = 12 ways of replacing 
the grey tiles in a row measuring five units in length.

How many different ways can the grey tiles in a row measuring fifty units 
in length be replaced if colours cannot be mixed and at least one coloured tile must be used?

NOTE: This is related to Problem 117.
'''

import time
from termcolor import colored


len_count_dic = dict()
len_count_dic.clear()


def f(x, y):




    # 一行有x个单元， 我们用y个连续红色单元填充到里面， x >= y
    # 第一种就是没有用红色划分，全黑的情况
    ways_count = 0

    # 当红色单元以及超过需要填充的行单元数，应该终止程序
    if x < y:
        return ways_count
    #添加缓存逻辑
    if x in len_count_dic and len_count_dic[x]!= 0:
        return len_count_dic[x]

    for start_index in range(0, x-y+1):
        # print(colored("开始的index=", "red"), start_index)

        ways_count += 1
        ways_count += f(x-start_index-y, y)

    # 添加缓存
    len_count_dic[x] = ways_count
    print(x, y, ways_count)
    return ways_count


def main_process():
    mysum = 0
    x = 50
    # 测试用小数据
    # x = 7
    # 直接先不停测试上限，先试验了100不行，再200就可以了
    for yi in range(2 , 5):
        len_count_dic.clear()
        mycount = f(x, yi)
        mysum += mycount
    # right  = 20492570929
    # mysum=   61095033219
    print('mysum=', mysum)

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)