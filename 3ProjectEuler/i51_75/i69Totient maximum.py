import time
from termcolor import colored

from math import gcd as bltin_gcd
# https://stackoverflow.com/questions/39678984/efficient-check-if-two-numbers-are-co-primes-relatively-primes
def coprime2(a, b):
    return bltin_gcd(a, b) == 1

# https://zh.wikipedia.org/wiki/%E6%AC%A7%E6%8B%89%E5%87%BD%E6%95%B0
# def main_process(bound_n):
#     target_n = 2
#     target_radio = 1
#     for i in range(2, bound_n+1):
#         count_cprime2 = 0
#         for j in range(i):
#             if coprime2(i, j+1):
#                 count_cprime2 += 1
#                 # print(i+1, j+1)
#         radio = i/count_cprime2

#         if radio > target_radio:
#             target_radio = radio
#             target_n = i
#         if i % 1000 == 0:
#             print(i, '#', count_cprime2,radio )
        
#     print(colored('target_n=', 'red'), target_n)
def prime_factors(n):
    # print('n=',n)
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            if i not in factors:
                # print(i,'not in', factors)
                factors.append(i)
    if n > 1 and (n not in factors):
        factors.append(n)
    return factors

def target(n):
    # https://zh.wikipedia.org/wiki/%E6%AC%A7%E6%8B%89%E5%87%BD%E6%95%B0
    factors = prime_factors(n)
    # print('factors=', factors)
    target = 1
    for p in factors:
        target *= 1/(1 - 1/p)
    return target


def main_process(bound_n):
    target_n = 2
    target_radio = 1
    for i in range(2, bound_n+1):

        radio = target(i)

        if radio > target_radio:
            target_radio = radio
            target_n = i
        if i % 10000 == 0:
            print(i, '#',radio )
        
    print(colored('target_n=', 'red'), target_n)

if __name__ == "__main__":
    tic = time.clock()
    # for i in range(1,10):
    #     print(prime_factors(i))
    main_process(1000000)
    # main_process(10)

    toc = time.clock()
    print("time=",toc - tic)