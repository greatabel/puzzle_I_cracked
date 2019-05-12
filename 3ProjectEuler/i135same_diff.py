'''
Given the positive integers, x, y, and z, 

are consecutive terms of an arithmetic progression, 

the least value of the positive integer, n, for which the equation, x2 − y2 − z2 = n, has exactly two solutions is n = 27:

342 − 272 − 202 = 122 − 92 − 62 = 27

It turns out that n = 1155 is the least value which has exactly ten solutions.

How many values of n less than one million have exactly ten distinct solutions?

#----------------------------#

欧拉工程135: 相同的差

已知正整数x，y，z构成等差数列，使得方程x^2 − y^2 − z^2 = n有两个解的最小正整数为n=27：

34^2 − 27^2 − 20^2 = 12^2 − 9^2 − 6^2 = 27
使得方程有十个解的最小正整数为n = 1155。

在小于一百万的数中，有多少个n的取值使得方程恰好有十个不同的解？

'''


import time
from termcolor import colored


limit = 10 ** 6
def main_process():
    # 根据 i135.jpg 分析可知:
    results = [0] * limit
    for m in range(1,2 * limit):
        for k in range(m//5 +1, (m+1)//2):
            n = (m - k) * (5 * k - m)
            if n >= limit:
                break
            results[n] += 1
    result = results.count(10)
    print(colored('mycount=', 'red'), result)

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)
