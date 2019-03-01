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


def find_factor(n):
    # print("the:",n)
    factors = []
    for i in range(1, int(math.sqrt(n))+1 ):
        # print("i=",i)
        if n % i == 0:
            factors.append(i)
            if i != n//i:
                factors.append(n//i)
            
    return factors


def factor(numberToFactor, arr=list()):
    i = 2
    maximum = numberToFactor / 2 + 1
    while i < maximum:
        if numberToFactor % i == 0:
            return factor(numberToFactor/i,arr + [i])
        i += 1
    return sorted(list(set(arr + [numberToFactor])))


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

def logN(plist, alist):
    for index, item in enumerate(plist):
        print(item, ' ^p=', alist[index])

def main_process():
    p = genprimes(45)
    primes = [i for i in p]
    logN(primes, [1] * 14 )
    print(len(primes), '<= len, is :', primes)

    # prod = 1
    # for i in primes:
    #     prod *= i
    # print(factor(9350130049860600))
    # print(prod, math.sqrt(13082761331670030), (13082761331670030/9350130049860600))

    print(colored('mycount=', 'red'), 'results')

# 9350130049860600
# 13082761331670030
if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)