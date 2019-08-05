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


def main_process():
    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





