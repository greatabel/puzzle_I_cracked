'''
There are some prime values, p, for which there exists a positive integer, n, 
such that the expression n3 + n^2p is a perfect cube.

For example, when p = 19, 8^3 + 8^2×19 = 12^3.

What is perhaps most surprising is that for each prime with this property the value of n is unique, 
and there are only four such primes below one-hundred.

How many primes below one million have this remarkable property?

#----------------------------#

欧拉工程/欧拉项目131: 素数立方数组合

对于某些素数p，存在正整数n，使得表达式n3 + n^2p是立方数。

例如，对于p = 19，8^3 + 8^2×19 = 12^3

非常奇特的是，对于满足这个性质的素数，n的值都是唯一的。在小于一百的素数中，只有四个素数满足这个性质。

在小于一百万的素数中，有多少个素数满足这个神奇的性质？

'''




import itertools
from itertools import count, islice
from math import sqrt, gcd
import time
from termcolor import colored


def isprime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def p(i):
    return 3 * i * i + 3 * i + 1

# 3 * 577 * 577 + 3 * 577 + 1 = 1000519
def main_process():
    r = 0 
    for i in range(1, 577):
        if isprime(p(i)):
            r += 1
    print(colored('mycount=', 'red'), r)

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)