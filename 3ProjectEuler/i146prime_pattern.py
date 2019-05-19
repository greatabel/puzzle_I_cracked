'''

Investigating a Prime Pattern

Problem 146
The smallest positive integer n for which the numbers 

n2+1, n2+3, n2+7, n2+9, n2+13, and n2+27 are consecutive primes is 10. 

The sum of all such integers n below one-million is 1242490.

What is the sum of all such integers n below 150 million?



#----------------------------#

欧拉工程146: 素数模式研究

使得n2+1，n2+3，n2+7，n2+9，n2+13以及n2+27为连续素数的最小的n是10。

在小于一百万的整数中，所有满足这一条件的整数n的总和为1242490。

在小于一亿五千万的数中，所有满足这一条件的整数n的总和是多少？

'''



from itertools import count, islice
from math import sqrt, gcd
import time
from termcolor import colored


limit = 15 * 10 ** 7
# test
limit = 10 ** 6


def isprime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def check(sq):
    if isprime(sq + 1) and isprime(sq + 3) and \
       isprime(sq + 7) and isprime(sq + 9) and \
       isprime(sq + 13) and isprime(sq + 27):
        return True
    else:
        return False

def main_process():
    results = 0
    for i in range(10, limit + 1, 10):
        sq = i ** 2
        if sq % 3 != 1:
            continue
        if check(sq):
            results += sq
    print(colored('mycount=', 'red'), results)

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)








