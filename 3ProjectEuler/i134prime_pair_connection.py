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
思路分析：肯定不可能硬解决，速度不行。


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


def reciprocal_mod(t, b):
    assert 0 <= t < b    
    # Based on a sibplification of the ettended Euclidean algorithm
    y = t
    t = b
    a = 0
    b = 1
    while y != 0:
        a, b = b, a - t // y * b
        t, y = y, t % y
    if t == 1:
        return a % b

limit = 10**6
# limit = 100

def main_process():

    primes = primeSieve(limit )
    # 对于5 ≤ p1
    primes.remove(2)
    primes.remove(3)
    # 因为 p2 是可以在limit之外的
    primes.append(1000003)
    mysum = 0
    print(primes, len(primes))
    for key, v in enumerate(primes):
        if key < len(primes)-1:
            i = len(str(primes[key+1]))
            # print('index=', key, 'value=', v, primes[key], primes[key+1], 'i=', i, 10**i)
            p = primes[key]
            q = primes[key+1]

            k = 1
            while k < p:
                k *= 10
            m = (q - p) * reciprocal_mod(k % q, q) % q

            combine =  m * k + p
            # if key % 100 == 0:
            #     print(p, q, combine)
            mysum += combine
          


    print(colored('mycount=', 'red'), mysum)

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)
