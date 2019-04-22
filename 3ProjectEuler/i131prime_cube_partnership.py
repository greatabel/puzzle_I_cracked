'''
There are some prime values, p, for which there exists a positive integer, n, 
such that the expression n3 + n2p is a perfect cube.

For example, when p = 19, 8^3 + 8^2×19 = 12^3.

What is perhaps most surprising is that for each prime with this property the value of n is unique, 
and there are only four such primes below one-hundred.

How many primes below one million have this remarkable property?

#----------------------------#

欧拉工程/欧拉项目131: 素数立方数组合

对于某些素数p，存在正整数n，使得表达式n3 + n2p是立方数。

例如，对于p = 19，8^3 + 8^2×19 = 12^3

非常奇特的是，对于满足这个性质的素数，n的值都是唯一的。在小于一百的素数中，只有四个素数满足这个性质。

在小于一百万的素数中，有多少个素数满足这个神奇的性质？

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