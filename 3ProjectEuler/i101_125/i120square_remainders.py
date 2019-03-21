'''
Let r be the remainder when (a−1)n + (a+1)n is divided by a^2.

For example, if a = 7 and n = 3, then r = 42: 6^3 + 8^3 = 728 ≡ 42 mod 49. 
And as n varies, so too will r, but for a = 7 it turns out that rmax = 42.

For 3 ≤ a ≤ 1000, find ∑ rmax.
'''

'''
欧拉工程项目第120
这个可以是个纯数学题目，具体分析思路见：i120.jpg
'''

import time
from termcolor import colored


def calculateR(a):
    r = 0
    if a % 2 == 0:
        # 偶数
        r = a ** 2 - 2 * a
    else:
        # 奇数
        r = a ** 2 - a
    return r

def main_process():
    isum = 0
    for i in range(3, 1000+1):
        isum += calculateR(i)
    print(colored('mycount=', 'red'), isum)

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)