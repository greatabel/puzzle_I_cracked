'''

https://zhuanlan.zhihu.com/p/46368084

#----------------------------#

来由：看python的缺点时候，想起
GIL是什么？GIL的全称是Global Interpreter Lock(全局解释器锁)

问题：描述Python GIL的概念， 以及它对python多线程的影响？阐明多线程抓取程序是否可比单线程性能有提升，并解释原因。
参考答案:
Python语言和GIL没有半毛钱关系。仅仅是由于历史原因在Cpython虚拟机(解释器)，难以移除GIL。
GIL：全局解释器锁。每个线程在执行的过程都需要先获取GIL，保证同一时刻只有一个线程可以执行代码。
线程释放GIL锁的情况： 在IO操作等可能会引起阻塞的system call之前,可以暂时释放GIL,但在执行完毕后,
必须重新获取GIL Python 3.x使用计时器（执行时间达到阈值后，当前线程释放GIL）或Python 2.x，tickets计数达到100
Python使用多进程是可以利用多核的CPU资源的。
多线程爬取比单线程性能有提升，因为遇到IO阻塞会自动释放GIL锁
————————————————


进而想起来 解决GIL锁方法：
1:更换解释器 比如使用jpython(java实现的python解释器)
2:使用多进程完成多任务的处理

才有了在1个process的 d1in_one_process

'''

import time
from termcolor import colored
import os


def long_time_task():
    print('当前进程: {}'.format(os.getpid()))
    time.sleep(3)
    print("结果: {}".format(8**20))


def main_process():
    print('当前母进程：{}'.format(os.getpid()))
    for i in range(2):
        long_time_task()

if __name__ == "__main__":
    tic = time.time()
    
    main_process()

    toc = time.time()
    print("time=",toc - tic)





