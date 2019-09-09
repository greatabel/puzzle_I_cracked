'''



#----------------------------#



'''
from random import shuffle
import time
from termcolor import colored


def main_process():
    t = '''
    q: 如何以就地操作方式打乱一个列表的元素？

    为了达到这个目的，我们从random模块中导入shuffle()函数。
    '''
    print(colored('mycount=', 'red'), t)

    mylist = list(range(1,10))
    shuffle(mylist)
    print(mylist)

    print('numpy 也有shuffle')
    import numpy as np
    arr = np.arange(0, 20, 1)
    print(arr)
    np.random.shuffle(arr)
    print(arr)

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





