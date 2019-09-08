'''

Python中如何实现多线程？

#----------------------------#



'''
import logging
import threading
import time
from termcolor import colored


def thread_function(name):
    logging.info("线程 %s: starting", name)
    time.sleep(2)
    logging.info("线程 %s: finishing", name)



if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("主线程    : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,))
    logging.info("主线程    : before running thread")
    x.start()
    logging.info("主线程    : wait for the thread to finish")
    # x.join()
    logging.info("主线程    : all done")

    print(colored('--------------------', 'green'), '解答', 
            colored('-'*20, 'red'))
    q = '在Python中如何实现多线程？'
    ans = '一个线程就是一个轻量级进程，多线程能让我们一次执行多个线程。我们都知道，Python是多线程语言，其内置有多线程工具包。\
            Python中的GIL（全局解释器锁）确保一次执行单个线程。一个线程保存GIL并在将其传递给下个线程之前执行一些操作，\
            这会让我们产生并行运行的错觉。但实际上，只是线程在CPU上轮流运行。当然，所有的传递会增加程序执行的内存压力'
    print(q, ans)




