'''



#----------------------------#



'''

import time
from termcolor import colored


def main_process():
    t = '''
    q: 如何以就地操作方式打乱一个列表的元素？

    为了达到这个目的，我们从random模块中导入shuffle()函数。
    '''
    print(colored('mycount=', 'red'), t)

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





