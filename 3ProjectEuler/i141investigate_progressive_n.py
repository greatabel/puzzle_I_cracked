'''

nvestigating progressive numbers, n, which are also square

Problem 141
A positive integer, n, is divided by d and the quotient and remainder are q and r respectively. 

In addition d, q, and r are consecutive positive integer terms in a geometric sequence, 

but not necessarily in that order.

For example, 58 divided by 6 has quotient 9 and remainder 4. 

It can also be seen that 4, 6, 9 are consecutive terms in a geometric sequence (common ratio 3/2).

We will call such numbers, n, progressive.

Some progressive numbers, such as 9 and 10404 = 1022, happen to also be perfect squares.

The sum of all progressive perfect squares below one hundred thousand is 124657.

Find the sum of all progressive perfect squares below one trillion (1012).

#----------------------------#

欧拉工程141: 累进平方数n的研究

正整数n被d的商和余数分别是q和r，除此之外，d，q，r

恰好是一个等比数列中的连续三个正整数项，但其对应顺序不一定一致。

例如，58被6除商9余4，可以发现4，6，9构成等比数列的连续三项，公比是3/2。
我们称这样的数n为累进数。

有些累进数，例如9或者10404=1022，恰好也是完全平方数。
所有小于十万的累进平方数的和是124657。

求所有小于一万亿（1012）的累进平方数之和。

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
