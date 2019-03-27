'''
A number consisting entirely of ones is called a repunit. We shall define R(k) to be a repunit of length k;
 for example, R(6) = 111111.

Given that n is a positive integer and GCD(n, 10) = 1, it can be shown that there always exists a value, k, 

for which R(k) is divisible by n, and let A(n) be the least such value of k; for example, A(7) = 6 and A(41) = 5.

The least value of n for which A(n) first exceeds ten is 17.

Find the least value of n for which A(n) first exceeds one-million.
#----------------------------#

欧拉工程129: 循环单位数整除性

只包含数字1的数被称为循环单位数，我们定义R(k)是长为k的循环单位数，例如，R(6) = 111111。

如果n是一个整数，且GCD(n, 10) = 1，可以验证总存在k使得R(k)能够被n整除，并且记A(n)是这些k中最小的一个。

例如，A(7) = 6，而A(41) = 5。

使得A(n)第一次超过十的n是17。

求使得A(n)第一次超过一千万的n
#----------------------------#

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