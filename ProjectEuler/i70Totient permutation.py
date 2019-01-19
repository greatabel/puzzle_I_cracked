# Euler's Totient function, φ(n) [sometimes called the phi function], 
# is used to determine the number of positive numbers less than 
# or equal to n which are relatively prime to n. For example, 
# as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
# The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

# Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

# Find the value of n, 1 < n < 107, for which φ(n) is a permutation of n and the ratio n/φ(n) 

# produces a minimum.

import time
from termcolor import colored
from fractions import gcd
from itertools import permutations  
from functools import reduce
import math
# https://stackoverflow.com/questions/6800193/
# what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
def prime_factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

'''

** 思路参考 https://www.mathblog.dk/
project-euler-70-investigate-values-of-n-for-which-%CF%86n-is-a-permutation-of-n/

'''

# 太慢了
# def phi_function(n):
#     # https://zh.wikipedia.org/wiki/%E6%AC%A7%E6%8B%89%E5%87%BD%E6%95%B0
#     relateively_primes = []
#     if n == 1:
#         relateively_primes = [1]
#     else:
#         for i in range(1, n):
#             if gcd(i, n) == 1: 
#                 relateively_primes.append(i)
#     # print(" relateively_primes=", relateively_primes)
#     return len(relateively_primes)

# def prime_factors(n):
#     # print('n=',n)
#     i = 2
#     factors = []
#     while i * i <= n:
#         if n % i:
#             i += 1
#         else:
#             n //= i
#             if i not in factors:
#                 # print(i,'not in', factors)
#                 factors.append(i)
#     if n > 1 and (n not in factors):
#         factors.append(n)
#     return factors

# def n_divide_phi(n):
#     # https://zh.wikipedia.org/wiki/%E6%AC%A7%E6%8B%89%E5%87%BD%E6%95%B0
#     factors = prime_factors(n)
#     # print('factors=', factors)
#     target = 1
#     for p in factors:
#         target *= 1/(1 - 1/p)
#     return target

# 太慢
# def permutation_of_number(n):
#     perms = [ int(''.join(p)) for p in permutations(str(n))]
#     # print('permutations=', perms)
#     return perms

def is_perm(a,b):
    return sorted(str(a))==sorted(str(b))

def main_process():
    target_n = 0
    target_ratio = 2
    primes = []
    for i in range( int(math.sqrt(10**7)/2), int(math.sqrt(10**7)) *2):
        if len(prime_factors(i)) == 2:
            primes.append(i)
    for p1 in primes:
        for p2 in primes:
            phi = (p1 - 1) * (p2 - 1)
            n = p1 * p2
            radio = n / phi
            if n < 10**7 and is_perm(phi, n) and (target_ratio > radio):
                target_ratio = radio
                target_n = n
                print(target_n, ' target_n=', target_ratio)
    # for i in range(1, int(10e7)):
    #     target_n = i

    #     ratio = n_divide_phi(i)
    #     phi = int(i / ratio)
    #     # print('phi=', phi, ' i=', i)
    #     # perms = permutation_of_number(i)
    #     if is_perm(phi, i) and (target_ratio < ratio):
    #         target_ratio = ratio
    #         target_n = i
    #         print(target_n, target_ratio)

    #     if i % int(10e5) == 0:
    #         print(i)
    # print('target_n=', target_n)

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print(colored('time=', 'red'), toc - tic)