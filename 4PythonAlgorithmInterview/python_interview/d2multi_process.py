'''

https://zhuanlan.zhihu.com/p/46368084

#----------------------------#

来由：看python的缺点时候，想起
GIL是什么？GIL的全称是Global Interpreter Lock(全局解释器锁)


进而想起来 解决GIL锁方法：
1:更换解释器 比如使用jpython(java实现的python解释器)
2:使用多进程完成多任务的处理

才有了在1个process的 d1in_one_process

'''

import time
from termcolor import colored
import os
from multiprocessing import Process


def long_time_task(i):
    print('子进程: {} - 任务{}'.format(os.getpid(), i))
    time.sleep(3)
    print("结果: {}".format(8**20))


def main_process():
    print('当前母进程：{}'.format(os.getpid()))
    p1 = Process(target=long_time_task, args=(1,))
    p2 = Process(target=long_time_task, args=(2,))
    print('等待所有子进程完成。')
    p1.start()
    p2.start()
    p1.join()
    p2.join()

if __name__ == "__main__":
    tic = time.time()
    
    main_process()

    toc = time.time()
    print("time=",toc - tic)





