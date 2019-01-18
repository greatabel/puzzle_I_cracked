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



def phi_function(n):
    # https://zh.wikipedia.org/wiki/%E6%AC%A7%E6%8B%89%E5%87%BD%E6%95%B0
    relateively_primes = []
    if n == 1:
        relateively_primes = [1]
    else:
        for i in range(1, n):
            if gcd(i, n) == 1: 
                relateively_primes.append(i)
    # print(" relateively_primes=", relateively_primes)
    return len(relateively_primes)
    

def main_process():
    phi = phi_function(87109)
    print('phi=', phi)

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print(colored('time=', 'red'), toc - tic)