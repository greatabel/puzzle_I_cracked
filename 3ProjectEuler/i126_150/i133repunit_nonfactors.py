'''
A number consisting entirely of ones is called a repunit. 

We shall define R(k) to be a repunit of length k; 

for example, R(6) = 111111.

Let us consider repunits of the form R(10n).

Although R(10), R(100), or R(1000) are not divisible by 17, 
R(10000) is divisible by 17. Yet there is no value of n for which R(10n) will divide by 19. 
In fact, it is remarkable that 11, 17, 41, and 73 are the only four primes below one-hundred 
that can be a factor of R(10n).

Find the sum of all the primes below one-hundred thousand that will never be a factor of R(10n).


#----------------------------#

欧拉工程133: 循环单位数的非质因数

只包含数字1的数被称为循环单位数，我们定义R(k)是长为k的循环单位数；例如，R(6)=111111。

考虑形如R(10n)的循环单位数。

尽管R(10)，R(100)和R(1000)都不能被17整除，R(10000)却能够被17整除。

然而，不存在n使得R(10^n)能被19整除。

事实上，在小于100的质数中，只有11，17，41和73能够成为R(10^n)的质因数。

找出所有小于十万且永远不会成为R(10^n)的质因数的质数之和。

#----------------------------#
思路分析：
    根据 i33.jpg的分析 我们可知“R(k) 当k在证书内整除性满足结合律”
找到最够大的10^n' 可以被所有 n0,n1,n2…… n'-1 所整除，所以我们测试某个足够大的n' 就可以知道
小于 10^5的质数 是否满足条件，然后统计相关不是这个R(10^n')的质数之和就满足条件了
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
    mysum = 0
    primes = primeSieve(100000)
    print('primes ', len(primes), primes[0:10],primes[-10:])
    assuming_k = pow(10, 16)
    for prime in primes:
        # 根据 i132.jpg 关于整除的分析， 我们可以简化检查
        # prime 是否是 assuming_k 因子的过程
        if pow(10, assuming_k, 9*prime) != 1:
            mysum += prime
    print(colored('mycount=', 'red'), mysum)
    # mycount= 453647705

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)
