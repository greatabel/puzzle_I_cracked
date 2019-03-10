'''
A row measuring seven units in length has red blocks with a minimum length of three units placed on it, 
such that any two red blocks (which are allowed to be different lengths) are separated 
by at least one grey square. 
There are exactly seventeen ways of doing this.

p114.png
How many ways can a row measuring fifty units in length be filled?

NOTE: Although the example above does not lend itself to the possibility, 
in general it is permitted to mix block sizes. For example, 
on a row measuring eight units in length you could use red (3), grey (1), and red (4).
'''


import time
from termcolor import colored


def f(x, y):
    # 一行有x个单元， 我们用y个连续红色单元填充到里面， x >= y
    # 第一种就是没有用红色划分，全黑的情况
    ways_count = 1

    # 当红色单元以及超过需要填充的行单元数，应该终止程序
    if x < y:
        return ways_count

    for start_index in range(0, x-y+1):
        print(colored("开始的index=", "red"), start_index)
        for red_len in range(y, x-start_index+1):
            print(' 红单元长度=', red_len)
            print('#' * start_index, colored('#', 'red') * red_len, '#' * (x - start_index - red_len))
            ways_count += 1
            # print(' x-start_index-red_len=', x-start_index-red_len)
    return ways_count


def main_process():
    x = 50
    y = 3
    # 测试用小数据
    x = 7
    mycount = f(x, y)
    print(colored('mycount=', 'red'), mycount)

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)