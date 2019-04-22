'''
A number consisting entirely of ones is called a repunit. 
We shall define R(k) to be a repunit of length k; for example, R(6) = 111111.

Given that n is a positive integer and GCD(n, 10) = 1, 
it can be shown that there always exists a value, k, 
for which R(k) is divisible by n, and let A(n) be the least such value of k; 
for example, A(7) = 6 and A(41) = 5.

You are given that for all primes, p > 5, that p − 1 is divisible by A(p). 
For example, when p = 41, A(41) = 5, and 40 is divisible by 5.

However, there are rare composite values for which this is also true; 
the first five examples being 91, 259, 451, 481, and 703.

Find the sum of the first twenty-five composite values of n for which
GCD(n, 10) = 1 and n − 1 is divisible by A(n).

#----------------------------#

欧拉工程130: 满足素数循环单位数性质的合数

只包含数字1的数被称为循环单位数，我们定义R(k)是长为k的循环单位数，例如，R(6) = 111111。

如果n是一个整数，且GCD(n, 10) = 1，可以验证总存在k使得R(k)能够被n整除，并且记A(n)是这些k中最小的一个。
例如，A(7) = 6，而A(41) = 5。

已知对于素数p > 5，p − 1能够被A(p)整除。例如，当p = 41时，A(41) = 5，而40能够被5整除。

然而，有很少的一部分合数也满足这条性质，前5个这样的数分别是91，259，451，481以及703。

找出前25个合数n满足
GCD(n, 10) = 1且n − 1能够被A(n)整除，并求它们的和。

'''

import itertools
from itertools import count, islice
from math import sqrt, gcd
import time
from termcolor import colored


def isprime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))


def A(n):
    if isprime(n) or gcd(n, 10)!= 1:
        return 0
    x, k = 1, 1
    while x != 0:
        x = (x * 10 + 1) % n
        k += 1
    return k

limit = 25
counter = 0

n = 1
result = 0

def main_process():
    global counter, n, result
    while ( counter < limit):
        n += 1
        if isprime(n):
            continue
        a = A(n)
        if a != 0 and (n-1) % a == 0:
            result += n
            counter += 1

    print(colored('mycount=', 'red'), result)

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)
