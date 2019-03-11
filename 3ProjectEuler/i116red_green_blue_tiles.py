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
def f(x, y):

    #添加缓存逻辑
    if x in len_count_dic and len_count_dic[x]!= 0:
        return len_count_dic[x]


    ways_count = 0

    if x < y:
        return ways_count

    for start_index in range(0, x-y+1):
        # print(colored("开始的index=", "red"), start_index)
        
        # 可以填充1个
        ways_count += 1

        ways_count += f(x-start_index-y, y)

    # 添加缓存
    len_count_dic[x] = ways_count
    return ways_count


def main_process():
    
    x = 50
    mycount = 0
    # 直接先不停测试上限，先试验了100不行，再200就可以了
    for y in range(2, 5):
        print('y=', y)
        mycount += f(x, y)

    print(colored('mycount=', 'red'), mycount)
      
    # mycount= 1053389 x= 168

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)