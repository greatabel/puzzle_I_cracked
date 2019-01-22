# It is possible to write five as a sum in exactly six different ways:

# 4 + 1
# 3 + 2
# 3 + 1 + 1
# 2 + 2 + 1
# 2 + 1 + 1 + 1
# 1 + 1 + 1 + 1 + 1

# How many different ways can one hundred be written as a sum of at least two positive integers?

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