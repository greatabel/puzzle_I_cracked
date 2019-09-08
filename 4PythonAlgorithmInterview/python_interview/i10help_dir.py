'''



#----------------------------#



'''

import copy
import time
from termcolor import colored


def main_process():

    t = '''
    q: 解释Python中的help()和dir()函数？

    Help()函数是一个内置函数，用于查看函数或模块用途的详细说明

    Dir()函数也是Python内置函数，dir() 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；
    带参数时，返回参数的属性、方法列表
    '''
    print(colored('mycount=', 'red'), t, help(copy.copy),'#'*10,
            dir(copy.copy))

    

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





