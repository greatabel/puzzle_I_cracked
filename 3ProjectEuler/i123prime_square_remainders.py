'''
Let pn be the nth prime: 2, 3, 5, 7, 11, ..., 
and let r be the remainder when (pn−1)^n + (pn+1)^n is divided by pn^2.

For example, when n = 3, p3 = 5, and 4^3 + 6^3 = 280 ≡ 5 mod 25.

The least value of n for which the remainder first exceeds 10^9 is 7037.

Find the least value of n for which the remainder first exceeds 10^10.

#----------------------------#
翻译：
欧拉工程/欧拉项目 123: 质数平方的余数们

记pn是第n个素数：2、3、5、7、11……；记r是(pn−1)^n + (pn+1)^n被pn^2除所得的余数。

例如，当n = 3时，p3 = 5，而4^3 + 6^3 = 280 ≡ 5 mod 25。

使余数首次超过109的最小n值是7037。

求使余数首次超过10^10的最小n值。

#----------------------------#
思路分析：肯定不可能暴力破解了，看看10^10就知道了，得先数学上分析下有没有trick

欧拉工程项目第120
这个可以是个纯数学题目，具体分析思路见：i120.jpg

根据分析可知当n 为 偶数， 余数是2 
而          n 为 奇数， 余数是2an = 2* Pn * n
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


limit = 10 ** 10
def main_process():
    ps = primeSieve(45000)
    print(len(ps), ps[:10])
    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()


    toc = time.clock()
    print("time=",toc - tic)