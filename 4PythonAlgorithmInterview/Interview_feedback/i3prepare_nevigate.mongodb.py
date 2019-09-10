'''

招聘要求：熟悉MySQL/Redis/MongoDB

#----------------------------#

1. MySQL中事务是如何实现的？

原子性：记录之前的版本，允许回滚
一致性：事务开始和结束之间的中间状态不会被其他事务看到
隔离性：适当的破坏一致性来提升性能与并行度 例如：最终一致~=读未提交。
持久性：每一次的事务提交后就会保证不会丢失

我们只需要知道事务保证了一系列的操作要么全部执行，要么一个也不执行，同时一旦事务提交，
则其所做的修改会永久保存到数据库即可。

事务的原子性是通过 undo log 来实现的
事务的持久性性是通过 redo log 来实现的
事务的隔离性是通过 (读写锁+MVCC)来实现的
而事务的终极大boss 一致性是通过原子性，持久性，隔离性来实现的！！
https://juejin.im/post/5cb2e3b46fb9a0686e40c5cb

'''

import time
from termcolor import colored


def main_process():
    t = '''





    '''
    print(colored('-'*20, 'red'), t)

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





