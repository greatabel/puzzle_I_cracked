'''

164: Numbers for which no three consecutive digits have a sum greater than a given value

How many 20 digit numbers n (without any leading zero) exist such 

that no three consecutive digits of n have a sum greater than 9?
#----------------------------#

欧拉工程164: 没有连续三位数字的和超过给定值的数

有多少个20位数字n（不包括前导0）满足，不存在连续三位数字的和超过9？

'''




import time
from termcolor import colored
import numpy as np


MaxNum = 9
NumDigitals = 20
counts = np.zeros((10,10, NumDigitals)) 

def count_per_len(d1, d2, remain):
    if remain == 0:
        return 1
    else:
        # print('d1,d2=', d1, d2, remain)
        if counts[d1][d2][remain] == 0:
            for i in range(0, MaxNum-d1-d2+1):
                counts[d1][d2][remain] += count_per_len(d2, i, remain-1)
        return counts[d1][d2][remain]


def main_process():
    results = 0
    for i in range(1, 9+1):
        results += count_per_len(0, i, NumDigitals-1)
    print(colored('mycount=', 'red'), int(results))
    # 378158756814587


if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





