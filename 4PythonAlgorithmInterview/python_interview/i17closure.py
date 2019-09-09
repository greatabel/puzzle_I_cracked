'''



#----------------------------#



'''

import time
from termcolor import colored

def A(x):
    def B():
        print('in B()', x)
    return B

def main_process():
    t = '''
    q:  Python中的闭包是什么？
    当一个嵌套函数在其外部区域引用了一个值时，该嵌套函数就是一个闭包。
    其意义就是会记录这个值


    '''
    print(colored('mycount=', 'red'), t)
    A(7)()

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





