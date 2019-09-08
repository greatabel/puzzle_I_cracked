'''
The positive integers, x, y, and z, are consecutive terms of an arithmetic progression. 

Given that n is a positive integer, the equation, x2 − y2 − z2 = n, has exactly one solution when n = 20:

132 − 102 − 72 = 20

In fact there are twenty-five values of n below one hundred for which the equation has a unique solution.

How many values of n less than fifty million have exactly one solution?

#----------------------------#

欧拉工程136: 唯一的差

正整数x，y，z构成等差数列。取正整数n=20，此时方程x2 − y2 − z2 = n只有一个解：

13^2 − 10^2 − 7^2 = 20
事实上，在小于一百的数中，有25个n的取值使得方程有唯一解。

在小于五千万的数中，有多少个n的取值使得方程有唯一解？

#----------------------------#
简单：直接使用135的方案，只需要改一些参数 ，😄
'''

import time
from termcolor import colored


limit = 5 * 10 ** 7
def main_process():
    # 根据 i135.jpg 分析可知:
    results = [0] * limit
    for m in range(1,2 * limit):

        for k in range(m//5 +1, (m+1)//2):
            n = (m - k) * (5 * k - m)
            if n >= limit:
                break
            results[n] += 1
    result = results.count(1)
    print(colored('mycount=', 'red'), result)
    # mycount= 2544559
    # time= 121.343906

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)
