'''
In the following equation x, y, and n are positive integers.

1
x
+   
1
y
=   
1
n
It can be verified that when n = 1260 there are 113 distinct solutions and
 this is the least value of n for which the total number of distinct solutions exceeds one hundred.

What is the least value of n for which the number of distinct solutions exceeds four million?

NOTE: This problem is a much more difficult version of Problem 108 and as it is well
 beyond the limitations of a brute force approach it requires a clever implementation.
'''

import time
from termcolor import colored
import math
import itertools


# def find_factor(n):
#     # print("the:",n)
#     factors = []
#     for i in range(1, int(math.sqrt(n))+1 ):
#         # print("i=",i)
#         if n % i == 0:
#             factors.append(i)
#             if i != n//i:
#                 factors.append(n//i)
            
#     return factors


# def get_num_factors(num):
#     list0=[]
#     tmp=2
#     if num==tmp:
#         return num
#     else:
#         while (num>=tmp):
#             k=num%tmp
#             if( k == 0):
#                 list0.append(str(tmp))
#                 num=num/tmp  #更新
#             else:
#                 tmp=tmp+1  #同时更新除数值，不必每次都从头开始
#     return ' '.join(list0)+' '



def genprimes(limit): # derived from 
                      # Code by David Eppstein, UC Irvine, 28 Feb 2002
    D = {}            # http://code.activestate.com/recipes/117119/
    q = 2

    while q <= limit:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1

def measure_N_func(plist, alist):
    mysum = 0 
    for index, p in enumerate(plist):
        # print(' alist[index], p=>',  alist[index], p)
        mysum +=  alist[index] * math.log(p, 10)
        # print(p, ' ^p=', alist[index])
    # print('make N is smallest, now the mysum =>', mysum)
    return mysum

def measure_dN_func(alist):
    prod = 1
    for p in alist:
        prod *= (2 * p + 1)
    # print('prod=', prod, prod >=  2 * 4 * 10 ** 6)
    return prod >= 2 * 4 * 10 ** 6

def main_process():
    # get the first 14 primes ,as 'i110solve.jpeg' analyzed
    primes = [i for i in genprimes(45)]




    x = [1, 2, 3]
    subs = [p for p in itertools.product(x, repeat=4)]
    # mymin set a large value
    mymin = 100
    target_N = []
    for sub in subs:
        t = [1] * 14
        # I tried , but [1] * 14 too large
        t[12], t[13] =  0, 0

        t[0] += sub[0]
        t[1] += sub[1]
        t[2] += sub[2]
        t[3] += sub[3]
        # print(t)
        measue_N = measure_dN_func(t)
        if measue_N:
            N = measure_N_func(primes, t)
            if N < mymin:
                mymin = N
                target_N = t
    print(mymin, target_N)


    prod = 1
    for index, p in enumerate(primes):
        prod *= p ** target_N[index]
    print( 'len(primes) = ', len(primes), primes)
    print(colored('mycount=', 'red'), prod)


if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)
