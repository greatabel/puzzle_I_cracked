'''



#----------------------------#



'''
import logging
import time
from termcolor import colored

def foo():
    print('I am foo!')


def bar():
    print('We are bars!')


def use_logging(func):
    logging.warning("%s is running" % func.__name__)
    func()


def use_logging_decorator(func):

    def wrapper(*args, **kwargs):
        logging.warning("%s is running" % func.__name__)
        return func(*args, **kwargs)

    return wrapper


@use_logging_decorator
def bar_b():
    print('bar_b')


def main_process():
    t = '''
    q:  Python中的装饰器是什么？
    装饰器是个python函数，让其他函数在不需要做任何代码变动的前提下增加额外功能。
    装饰器返回值也是一个函数对象。
    勇于有切面需求的场景：插入日志、性能测试、事物处理。有了装饰器，我们可以抽离
    大量与函数功能本身无关的雷同代码并继续重用。
    装饰器作用就是为依据存在的对象添加额外功能


    '''

    print(colored('-'*20, 'red'), t)

    use_logging(foo)
    use_logging(bar)

    print(colored('='*30, 'blue'))

    def bar_a():
        print('bar_a')

    bar_a = use_logging_decorator(bar_a)
    bar_a()


    print('@符号是装饰器的语法糖，在定义函数的时候使用，避免再一次赋值操作')
    bar_b()

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





