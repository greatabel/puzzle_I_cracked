'''

https://juejin.im/post/5b6bc1d16fb9a04f9c43edc3

#----------------------------#



'''

import time
from termcolor import colored


def main_process():
    t = '''
    13. 请解释使用*args和**kwargs的含义?

    当我们不知道向函数传递多少参数时，比如我们向传递一个列表或元组，我们就使用*args。


    '''
    print(colored('-'*20, 'red'), t)

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





