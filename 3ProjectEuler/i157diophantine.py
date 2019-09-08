'''

Solving the diophantine equation 1/a+1/b= p/10n

Problem 157
Consider the diophantine equation 1/a+1/b= p/10n with a, b, p, n positive integers and a ≤ b.
For n=1 this equation has 20 solutions that are listed below:

1/1+1/1=20/10   1/1+1/2=15/10   1/1+1/5=12/10   1/1+1/10=11/10  1/2+1/2=10/10
1/2+1/5=7/10    1/2+1/10=6/10   1/3+1/6=5/10    1/3+1/15=4/10   1/4+1/4=5/10
1/4+1/20=3/10   1/5+1/5=4/10    1/5+1/10=3/10   1/6+1/30=2/10   1/10+1/10=2/10
1/11+1/110=1/10 1/12+1/60=1/10  1/14+1/35=1/10  1/15+1/30=1/10  1/20+1/20=1/10
How many solutions has this equation for 1 ≤ n ≤ 9?

#----------------------------#

解不定方程1/a+1/b= p/10n

考虑不定方程1/a+1/b= p/10n，其中a, b, p, n均为正整数，且a ≤ b。
对于n=1，这个方程有20个解，如下所示：

                 
1/1+1/1=20/10   1/1+1/2=15/10   1/1+1/5=12/10   1/1+1/10=11/10  1/2+1/2=10/10
1/2+1/5=7/10    1/2+1/10=6/10   1/3+1/6=5/10    1/3+1/15=4/10   1/4+1/4=5/10
1/4+1/20=3/10   1/5+1/5=4/10    1/5+1/10=3/10   1/6+1/30=2/10   1/10+1/10=2/10
1/11+1/110=1/10 1/12+1/60=1/10  1/14+1/35=1/10  1/15+1/30=1/10  1/20+1/20=1/10
对于1 ≤ n ≤ 9，方程一共有多少个解？

#----------------------------#

跳过此题，解决方案来自：桃の天然水

'''


from itertools import product
from math import sqrt
import fractions
import time
from termcolor import colored


def make_primes(limit):
    for n in range(3, limit + 1, 2):
        if is_prime(n):
            primes.append(n)
    return primes

def is_prime(n):
    for p in primes:
        if p * p > n:
            return True
        elif n % p == 0:
            return False
    return True

def num_divisors(n, p0 = 1):
    if n == 1:
        return 1
    for p in primes:
        if p * p > n:
            return 2
        if p <= p0:
            continue
        if n % p == 0:
            n /= p
            rep = 1
            while n % p == 0:
                n /= p
                rep += 1
            return (rep + 1) * num_divisors(n, p)
    return 2

def e(n, p):
    counter = 0
    while n % p == 0:
        counter += 1
        n /= p
    return counter

def gen_exp(n):
    for q, r in product(range(n + 1), repeat = 2):
        k = 2 ** q
        l = 5 ** r
        yield k, l, n - q + 1, n - r + 1
        if q > 0 and r > 0:
            yield 1, k * l, n - q + 1, n - r + 1

def num_solutions(n):
    counter = 0
    for k, l, s, t in gen_exp(n):
        kl = k + l
        ds = e(kl, 2)
        dt = e(kl, 5)
        s += ds
        t += dt
        kl /= 2 ** ds * 5 ** dt
        
        counter += num_divisors(kl) * s * t
    # print(counter)
    return counter

N = 9
primes = [ 2 ]


def main_process():
    make_primes(int(sqrt(2 ** N + 5 ** N + 0.5)))
    print(colored('mycount=', 'red'), sum(map(num_solutions, range(1, N + 1))))
    # mycount= 53490

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)




