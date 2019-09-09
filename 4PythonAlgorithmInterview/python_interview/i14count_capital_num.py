'''

请写一个Python逻辑，计算一个文件中的大写字母数量

#----------------------------#



'''

import os
import time
from termcolor import colored


def main_process():
    count = 0
    with open('i14today.txt') as today:
        
        for i in today.read():
            print('i=', i)
            if i.isupper():
                count += 1
    print('count=', count)

    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





