'''

招聘要求：熟悉MySQL/Redis/MongoDB

#----------------------------#



'''

import time
from termcolor import colored


def main_process():
    t = '''

    1. 什么是Redis？
    Redis 是一个使用 C 语言写成的，开源的 key-value 数据库。。
    和Memcached类似，它支持存储的value类型相对更多，包括
    string(字符串)、
    list(链表)、
    set(集合)、
    zset(sorted set --有序集合)和
    hash（哈希类型）。

    2. Redis与Memcached的区别与比较？
    1 、Redis不仅仅支持简单的k/v类型的数据，同时还提供list，set，zset，hash等数据结构的存储。memcache支持简单的数据类型，String。
    2 、Redis支持数据的备份，即master-slave模式的数据备份。
    3 、Redis支持数据的持久化，可以将内存中的数据保持在磁盘中，重启的时候可以再次加载进行使用,而Memecache把数据全部存在内存之中
    4、 redis的速度比memcached快很多
    5、Memcached是多线程，非阻塞IO复用的网络模型；Redis使用单线程的IO复用模型。

    3 Redis与Memcached的选择
    终极策略： 使用Redis的String类型做的事，都可以用Memcached替换，以此换取更好的性能提升； 除此以外，优先考虑Redis

    4 redis 好处？
    1. 速度快
    2. 支持丰富数据类型
    3. 支持事务
    4.丰富特性： 可用于缓存，消息，按key设置过期时间，过期后将会自动删除

    5 MySQL里有2000w数据，Redis中只存20w的数据，如何保证Redis中的数据都是热点数据（redis有哪些数据淘汰策略？？？）
    相关知识：redis 内存数据集大小上升到一定大小的时候，就会施行数据淘汰策略（回收策略）。redis 提供 6种数据淘汰策略

    6 Redis常见性能问题和解决方案:

    Master最好不要做任何持久化工作，如RDB内存快照和AOF日志文件
    如果数据比较重要，某个Slave开启AOF备份数据，策略设置为每秒同步一次
    为了主从复制的速度和连接的稳定性，Master和Slave最好在同一个局域网内
    尽量避免在压力很大的主库上增加从库



    '''
    print(colored('-'*20, 'red'), t)

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





