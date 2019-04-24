'''
A number consisting entirely of ones is called a repunit. 

We shall define R(k) to be a repunit of length k; 

for example, R(6) = 111111.

Let us consider repunits of the form R(10n).

Although R(10), R(100), or R(1000) are not divisible by 17, 
R(10000) is divisible by 17. Yet there is no value of n for which R(10n) will divide by 19. 
In fact, it is remarkable that 11, 17, 41, and 73 are the only four primes below one-hundred 
that can be a factor of R(10n).

Find the sum of all the primes below one-hundred thousand that will never be a factor of R(10n).


#----------------------------#

欧拉工程133: 循环单位数的非质因数

只包含数字1的数被称为循环单位数，我们定义R(k)是长为k的循环单位数；例如，R(6)=111111。

考虑形如R(10n)的循环单位数。

尽管R(10)，R(100)和R(1000)都不能被17整除，R(10000)却能够被17整除。

然而，不存在n使得R(10n)能被19整除。

事实上，在小于100的质数中，只有11，17，41和73能够成为R(10^n)的质因数。

找出所有小于十万且永远不会成为R(10^n)的质因数的质数之和。

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

