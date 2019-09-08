'''



#----------------------------#



'''

import time
from termcolor import colored


class A:
    def func(self):
        print('Hi')

    def monkey(self):
        print('Hi monkey!')

## a 这个参数是没有用到的，因为func有一个参数，如果这个函数没有参数的话不能这样直接赋值
def outer_monkey(a):
    print('Hi, outer_monkey')

def main_process():
    t = '''
    Q 11. 什么是猴子补丁？
    在运行期间动态修改一个类或模块
    '''
    print(colored('-'*10, 'red'), t)

    a = A()
    a.func()
    print('使用猴子补丁')
    A.func = A.monkey
    a.func()
    print('其实这根本的原因在于Python语法的灵活性，方法可以像普通对象那样使用!\n')

    print('方法2： 也可以这样使用')
    A.func = outer_monkey
    a.func()

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





