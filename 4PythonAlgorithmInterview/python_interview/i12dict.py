'''



#----------------------------#



'''

import time
from termcolor import colored


def main_process():
    t = '''
    q: Python中的字典是什么？
    Python 中的字典是Python中一个键值映射的数据结构
    '''
    print(colored('mycount=', 'red'), t)

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





