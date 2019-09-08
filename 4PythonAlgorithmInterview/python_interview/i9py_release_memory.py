'''



#----------------------------#

https://www.zhihu.com/question/34895986

'''

from pympler import asizeof, tracker
import random
import gc

import time
from termcolor import colored


def main_process():
    t = '''
    q: 当退出Python时，是否释放全部内存？
    ans:答案是No。循环引用其它对象或引用自全局命名空间的对象的模块，在Python退出时并非完全释放。
    另外，也不会释放C库保留的内存部分
    '''
    print(colored('mycount=', 'red'), t)


    obj = [1, 2, (3, 4), 'text']
    print(asizeof.asizeof(obj))
    print(asizeof.asized(obj, detail=1).format())

    tr = tracker.SummaryTracker()
    a = [[random.random() for i in range(2000)] for i in range(2000)]
    tr.print_diff()

    gc.collect()
    from sys import getsizeof
    print('-'*20, getsizeof(a))

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





