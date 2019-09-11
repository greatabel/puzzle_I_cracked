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

2.http请求的完整过程
https://www.cnblogs.com/konghui/p/10574945.html


3. redis TTL key?
返回key剩余的过期时间。 这种反射能力允许Redis客户端检查指定key在数据集里面剩余的有效期。
redis> SET mykey "Hello"
OK
redis> EXPIRE mykey 10 # 设置mykey 10秒后过期
(integer) 1
redis> TTL mykey # 查看mykey剩余的过期时间
(integer) 10
 TTL怎么实现的
redis针对TTL时间有专门的dict进行存储，就是redisDb当中的dict *expires字段，
dict顾名思义就是一个hashtable，key为对应的rediskey，value为对应的TTL时间。

4 线程的生命周期，线程有几个状态？
当线程被创建并启动后，并不会直接进入执行状态，也不会一直处于执行状态，线程的生命周期中，
它会经历新建（new）、就绪（Ready）、运行（Running）、阻塞（Blocked）和死亡（Dead）5 种状态

5 grep 命令：grep 命令用于查找文件里符合条件的字符串

根据文件内容递归查找目录

# grep ‘energywise’ *           #在当前目录搜索带'energywise'行的文件

# grep -r ‘energywise’ *        #在当前目录及其子目录下搜索'energywise'行的文件
# grep -l -r ‘energywise’ *     #在当前目录及其子目录下搜索'energywise'行的文件，
                            但是不显示匹配的行，只显示匹配的文件

6. yield生成器及其作用？
生成器内部的代码执行到yield会返回，返回的内容为yield后的表达式。
下次再执行生成器的内部代码时将从上次的状态继续开始。
通过yield关键字，我们可以很方便的将一个函数修改为生成器。

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





