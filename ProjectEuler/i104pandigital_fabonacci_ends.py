'''
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
It turns out that F541, which contains 113 digits, is the first Fibonacci number 
for which the last nine digits are 1-9 pandigital (contain all the digits 1 to 9,
 but not necessarily in order). And F2749, which contains 575 digits, is the first Fibonacci 
 number for which the first nine digits are 1-9 pandigital.

Given that Fk is the first Fibonacci number for which the first nine digits AND the last 
nine digits are 1-9 pandigital, find k.
'''

import time
from termcolor import colored
import math


def is_pandigital(n):
    nlist = []
    for ch in str(n):
        nlist.append(int(ch))
    # print('n=', nlist)
    sorted_n = sorted(nlist)
    # print('sorted_n=', sorted_n)
    if sorted_n == list(range(1, 10)):
        # print('True')
        return True
    else:
        return False

def top_digits(n):
    t = n * 0.20898764024997873 + (-0.3494850021680094)
    t = int((pow(10, t - int(t) + 8)))
    return t

def brute_approach():
    fk, f0, f1 = 2, 1, 1
    while not is_pandigital(f1) or not is_pandigital(top_digits(fk)):
        f0, f1 = f1, (f1+f0) % 10**9
        fk += 1
    print("Project Euler 104 Solution =", fk)


def main_process():
    # print(is_pandigital(98991))
    # print(is_pandigital(934581267))
    # https://blog.dreamshire.com/project-euler-104-solution/
    brute_approach()
    # print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)