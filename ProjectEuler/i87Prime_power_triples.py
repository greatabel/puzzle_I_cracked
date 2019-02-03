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

def mytry(n):
    count = 0
    for i in (2, 3, 5):
        for j in (2, 3, 5):
            for k in (2, 3, 5):
                mysum = i ** 2 + j ** 3 + k ** 4
                if mysum < n:
                    count += 1
    print('count=', count)

def main_process():
    mytry(55 * 10**6)
    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)