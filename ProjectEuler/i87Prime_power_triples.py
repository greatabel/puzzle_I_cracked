'''
The smallest number expressible as the sum of a prime square, 
prime cube, and prime fourth power is 28. In fact, 
there are exactly four numbers below fifty that can be expressed in such a way:

28 = 22 + 23 + 24
33 = 32 + 23 + 24
49 = 52 + 23 + 24
47 = 22 + 33 + 24

How many numbers below fifty million can be expressed 
as the sum of a prime square, prime cube, and prime fourth power?
'''

import time
from termcolor import colored
from itertools import product
# def mytry(n):
#     count = 0
#     for i in (2, 3, 5):
#         for j in (2, 3, 5):
#             for k in (2, 3, 5):
#                 mysum = i ** 2 + j ** 3 + k ** 4
#                 if mysum < n:
#                     count += 1
#     print('count=', count)

def sieve_of_eratosthenes(max_integer):
    sieve = [True for _ in range(max_integer + 1)]
    sieve[0:1] = [False, False]
    for start in range(2, max_integer + 1):
        if sieve[start]:
            for i in range(2 * start, max_integer + 1, start):
                sieve[i] = False
    primes = []
    for i in range(2, max_integer + 1):
        if sieve[i]:
            primes.append(i)
    return primes

def loop(seta, setb, setc, limit):
    mylist = set()
    for a, b, c in product(seta, setb, setc):
        isum = a ** 2 + b ** 3 + c ** 4
        
        if isum < limit:
            
            if len(mylist) % 10000 == 0:
                print(a, b, c, 'isum=', isum, len(mylist))
            mylist.add(isum)
        # elif (a > b and b > c):
        #     break
    print('len=', len(mylist))
        


def main_process():
    # mytry(55 * 10**6)
    limit = 5 * 10 ** 7
    # limit = 100
    # t = sieve_of_eratosthenes(20)

    seta, setb, setc = sieve_of_eratosthenes(7072),sieve_of_eratosthenes(369),sieve_of_eratosthenes(85)
    # print('seta=', seta, setb, setc)
    loop(seta, setb, setc, limit)
    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)