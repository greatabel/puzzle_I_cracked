'''
A number consisting entirely of ones is called a repunit. 
We shall define R(k) to be a repunit of length k.

For example, R(10) = 1111111111 = 11×41×271×9091, and the sum of these prime factors is 9414.

Find the sum of the first forty prime factors of R(10^9).

#----------------------------#

欧拉工程/欧拉项目132: 大循环单位数的因数

只包含数字1的数被称为循环单位数，我们定义R(k)是长为k的循环单位数。

例如，R(10) = 1111111111 = 11×41×271×9091，这些质因数的和是9414。

找出R(10^9)的前40个质因数的和。


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

def main_process():
    primes = primeSieve(200000)
    print('primes ', len(primes), primes[0])
    mysum = 0
    counter = 0
    # k = 10 ** 10
    k = 10 ** (10 ** 9)
    i = 0
    limit = 40
    while counter < limit:

        if i < len(primes) and (k-1) % (9 * primes[i]) == 0 :
            print(primes[i])
            mysum += primes[i]
            counter += 1
        i += 1


    print(colored('mycount=', 'red'), mysum)

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)
