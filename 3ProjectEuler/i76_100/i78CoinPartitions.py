'''
Let p(n) represent the number of different ways in which n coins can be separated into piles. For example, five coins can be separated into piles in exactly seven different ways, so p(5)=7.

OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O
Find the least value of n for which p(n) is divisible by one million.
'''

import time
from termcolor import colored
import math

# 太慢
# def find_allways(total, sizes):
#     L = [0 for i in range(total+1)]
#     L[0] = 1
#     for i in range(len(sizes)):
#         for j in range(sizes[i], len(L)):
#             L[j] += L[j -sizes[i]]

#     # print(L[total])
#     return L[total] + 1

# 太慢too
# def dynamic_parition(n):

#     dp=[[0 for i in range(n+1)] for j in range(n+1)]
#     dp[0][0]=1
#     for i in range(1,n+1):
#         for j in range(1,n+1):
#             if i < j:
#                 dp[i][j]=dp[i][i]
#             elif i==j:
#                 dp[i][j]=1+dp[i][j-1]
#             else:
#                 dp[i][j]=dp[i][j-1]+dp[i-j][j]
#     # print(dp[n][n])
#     return dp[n][n]
from itertools import *

def pentagonal(n):
    return n*(3*n - 1) / 2

partitions = {}
generalized_pentagonals = sorted(map(pentagonal, list(range(-250, 250))))[1:]

# https://zach.se/project-euler-solutions/78/
def partition(n):
    if n <= 1: return 1
    if n not in partitions:
        signs = cycle([1, 1, -1, -1])
        pentagonals = takewhile(lambda p: p <= n, generalized_pentagonals)
        partitions[n] = sum(sign * partition(n - p) for sign, p in zip(signs, pentagonals))

    return partitions[n]



if __name__ == "__main__":
    tic = time.clock()
    print(next((n for n in count(0) if partition(n) % 1000000 == 0)))

    # for n in range(my_estimate, my_estimate + 500):
        # p_n = dynamic_parition(n)
        # if p_n % d == 0:
        #     print('find n=', n , " p_n=", p_n)
        #     break
        # if n % 100 == 0:
        #     print(n)
    # d = 1000
    # my_estimate = 2019
    # for n in range(1, my_estimate):
    #     p_n = find_allways(n, list(range(1, n+1)))
    #     if p_n % d == 0:
    #         print(n, 'p(n)=', p_n)
    #         break
    #     if n % 100 == 0:
    #         print('n=', n)


    toc = time.clock()
    print("time=",toc - tic)