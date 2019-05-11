'''
Given the positive integers, x, y, and z, 

are consecutive terms of an arithmetic progression, 

the least value of the positive integer, n, for which the equation, x2 − y2 − z2 = n, has exactly two solutions is n = 27:

342 − 272 − 202 = 122 − 92 − 62 = 27

It turns out that n = 1155 is the least value which has exactly ten solutions.

How many values of n less than one million have exactly ten distinct solutions?

#----------------------------#

欧拉工程135: 相同的差

已知正整数x，y，z构成等差数列，使得方程x2 − y2 − z2 = n有两个解的最小正整数为n=27：

342 − 272 − 202 = 122 − 92 − 62 = 27
使得方程有十个解的最小正整数为n = 1155。

在小于一百万的数中，有多少个n的取值使得方程恰好有十个不同的解？

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
