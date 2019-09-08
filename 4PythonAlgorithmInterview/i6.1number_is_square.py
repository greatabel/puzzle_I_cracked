'''

设计一个算法，判断给定一个数n是否是某个数的平方，不能使用开平方运算

#----------------------------#



'''

import time
from termcolor import colored


def is_power(n):
    i = 1
    while i**2 <= n:
        if n % i == 0 and n / i == i:
            return True
        i += 1
    return False

def main_process():
    for i in range(1, 17):
        if is_power(i):
            print(i)
    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





