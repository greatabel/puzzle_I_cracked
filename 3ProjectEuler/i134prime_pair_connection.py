'''

Consider the consecutive primes p1 = 19 and p2 = 23. 

It can be verified that 1219 is the smallest number such 

that the last digits are formed by p1 whilst also being divisible by p2.

In fact, with the exception of p1 = 3 and p2 = 5, 

for every pair of consecutive primes, p2 > p1, 

there exist values of n for which the last digits are formed 

by p1 and n is divisible by p2. Let S be the smallest of these values of n.

Find ∑ S for every pair of consecutive primes with 5 ≤ p1 ≤ 1000000.

#----------------------------#

欧拉工程134: 质数对连接

考虑连续的质数p1 = 19和p2 = 23。可以验证，

1219是所有以p1结尾并且能被p2整除的数中最小的一个。

事实上，除了p1 = 3和p2 = 5这一对之外，对于任意一对连续质数p2 > p1，

都存在一系列的数n，其尾数是p1，且能够被p2整除。记S是所有的n中的最小值。

对于5 ≤ p1 ≤ 1000000内的所有连续质数对，求∑ S。

#----------------------------#
思路分析：肯定不可能硬解决，速度不行。不许数学化问题：


'''

import math
import time
from termcolor import colored


def primeSieve(sieveSize):
    # Returns a list of prime numbers calculated using
    # the Sieve of Eratosthenes algorithm.
    sieve = [True] * sieveSize

    sieve[0] = False # zero and one are not prime numbers
    sieve[1] = False

    # create the sieve
    for i in range(2, int(math.sqrt(sieveSize)) + 1):
        pointer = i * 2
        while pointer < sieveSize:
            sieve[pointer] = False
            pointer += i


    # compile the list of primes
    primes = []
    for i in range(sieveSize):
        if sieve[i] == True:
            primes.append(i)
    return primes

limit = 100
def main_process():
    primes = primeSieve(limit)
    print(primes, len(primes))
    for k, v in enumerate(primes):
        if v!= 3 and k < len(primes)-1:
            i = len(str(primes[k+1]))
            print('index=', k, 'value=', v, primes[k], primes[k+1], 'i=', i, 10**i)
            j = 1
            combine = j * (10**i) + primes[k]            
            while combine % primes[k+1] != 0:
                j += 1
                combine = j * (10**i) + primes[k]
            print('combine=', combine)


    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)
