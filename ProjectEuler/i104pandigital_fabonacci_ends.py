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

fn1 = 1
fn2 = 1
tailcut = 10 ** 9
n = 2
found = False

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

def brute_approach():
    while not found:
        n += 1
        fn = fn1 + fn2
        tail = fn % tailcut


def main_process():
    print(is_pandigital(98991))
    print(is_pandigital(934581267))
    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)