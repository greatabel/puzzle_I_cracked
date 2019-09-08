'''

实现一个队列，具有入队、出队、查看首位元素、
查看队列大小等


#----------------------------#

思路：数组实现, 原书版本太绕了，写了个更简洁的

'''

import time
from termcolor import colored

class Queue :
    def __init__(self):
        self.items=[]

    def isEmpty(self) :
        return self.items==[]

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def printqueue(self):
        for items in self.items:
            print(items)
    

def main_process():
    q = Queue()
    for i in range(0, 5):
        print('入队：', i)
        q.enqueue(i)
    print(q.isEmpty(), q.size())
    print('printqueue')
    q.printqueue()
    print(q.dequeue(), q.size())
    q.enqueue(10)
    print(q.size())
    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





