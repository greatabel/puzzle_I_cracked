'''
It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five thousand different ways?
'''

import time
from termcolor import colored
import math


def find_allways(total, sizes):
    L = [0 for i in range(total+1)]
    L[0] = 1
    for i in range(len(sizes)):
        for j in range(sizes[i], len(L)):
            L[j] += L[j -sizes[i]]
    print(L[total] )


if __name__ == "__main__":
    tic = time.clock()
    # for i in range(0,20):
    #     print(i,fib(i),len(str(fib(i))))
    # find_allpowers(5,5)
    # find_allpowers(10000,4)

    find_allways(100, list(range(1, 100)))


    toc = time.clock()
    print("time=",toc - tic)