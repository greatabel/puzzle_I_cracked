'''
https://www.zhihu.com/question/20122137

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

2. 边缘计算？
边缘计算最开始，是因为传统海量数据传输非常费资源，且数据频率和数据质量都会受大量数据传输影响。
这里举一个不严谨的例子：比如我们想算个加速度，可是由于某些原因无法安装MPU6050类似的元件，只能通过速度求导，
可数据上传到云端之后再计算，已经面目全非了，缺失的、误码的、时间频率不均匀的，想计算精确的加速度较为困难。
于是人们就想，能不能把海量数据中这些速度的时间序列先进行一级计算，再将计算结果传到云端，这样既快速，又可靠。恩，这就是边缘计算了。



    '''
    print(t)

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





