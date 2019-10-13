'''


#----------------------------#



'''

import time
from termcolor import colored



def main_process():
    t = '''
@ 1.epoll 或者 kqueue 的原理是什么？
简单的说，就是一个生产者，消费者的方式。底层生成数据，放到readylist，用户用epoll_wait去取。

epoll用红黑树存储，用list存储就绪事件（与select和poll不同，select是bitmap，poll是数组存储），
之所以是e-poll，是因为它是event事件驱动，也就是说就通知这方面而言是异步的，
但是unp中仍然将epoll定义为同步的多路复用io模型，因此在很多地方epoll又有人称为伪异步。


    '''
    print(t)

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





