# Combinatoric selections
# Problem 53
# There are exactly ten ways of selecting three from five, 12345:

# 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

# In combinatorics, we use the notation, 5C3 = 10.

# In general,

# nCr =   
# n!
# r!(n−r)!
# ,where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
# It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

# How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?
import time
from termcolor import colored
from math import factorial

def ncr(n,r):
    return factorial(n) / (factorial(r) * factorial(n-r))

def main_process():
    count = 0
    for x in range(1,100+1):
        for y in range(0,x):
            if ncr(x, y) > 10**6:
                count += 1
                print(x,y)

    print(colored('mycount=', 'red'), count)

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)