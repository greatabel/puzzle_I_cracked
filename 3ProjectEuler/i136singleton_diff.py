'''
The positive integers, x, y, and z, are consecutive terms of an arithmetic progression. 

Given that n is a positive integer, the equation, x2 − y2 − z2 = n, has exactly one solution when n = 20:

132 − 102 − 72 = 20

In fact there are twenty-five values of n below one hundred for which the equation has a unique solution.

How many values of n less than fifty million have exactly one solution?

#----------------------------#

欧拉工程136: 唯一的差

正整数x，y，z构成等差数列。取正整数n=20，此时方程x2 − y2 − z2 = n只有一个解：

132 − 102 − 72 = 20
事实上，在小于一百的数中，有25个n的取值使得方程有唯一解。

在小于五千万的数中，有多少个n的取值使得方程有唯一解？

'''










import time
from termcolor import colored


def main_process():
    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)
