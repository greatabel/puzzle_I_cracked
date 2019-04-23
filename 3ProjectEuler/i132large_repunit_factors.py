'''
A number consisting entirely of ones is called a repunit. 
We shall define R(k) to be a repunit of length k.

For example, R(10) = 1111111111 = 11×41×271×9091, and the sum of these prime factors is 9414.

Find the sum of the first forty prime factors of R(10^9).

#----------------------------#

欧拉工程/欧拉项目132: 大循环单位数的因数

只包含数字1的数被称为循环单位数，我们定义R(k)是长为k的循环单位数。

例如，R(10) = 1111111111 = 11×41×271×9091，这些质因数的和是9414。

找出R(10^9)的前40个质因数的和。


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