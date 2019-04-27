'''

Consider the consecutive primes p1 = 19 and p2 = 23. 

It can be verified that 1219 is the smallest number such 

that the last digits are formed by p1 whilst also being divisible by p2.

In fact, with the exception of p1 = 3 and p2 = 5, 

for every pair of consecutive primes, p2 > p1, 

there exist values of n for which the last digits are formed 

by p1 and n is divisible by p2. Let S be the smallest of these values of n.

Find ∑ S for every pair of consecutive primes with 5 ≤ p1 ≤ 1000000.

#----------------------------#

欧拉工程134: 质数对连接

考虑连续的质数p1 = 19和p2 = 23。可以验证，

1219是所有以p1结尾并且能被p2整除的数中最小的一个。

事实上，除了p1 = 3和p2 = 5这一对之外，对于任意一对连续质数p2 > p1，

都存在一系列的数n，其尾数是p1，且能够被p2整除。记S是所有的n中的最小值。

对于5 ≤ p1 ≤ 1000000内的所有连续质数对，求∑ S。

'''

import time
from termcolor import colored


def main_process():
    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)
