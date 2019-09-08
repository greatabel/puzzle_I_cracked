'''
实现一个栈，具有：入栈、出栈、取栈顶元素，判断栈是否为空、
已经获取栈中元素个数


#----------------------------#



'''


import time
from termcolor import colored


class MyStack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def top(self):
        if not self.is_empty():
            return self.items[len(self.items)-1]
        else:
            return None

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            return None

    def push(self, item):
        self.items.append(item)


def main_process():
    s = MyStack()
    s.push(4)
    s.push(5)
    print('top element:', s.top())
    print('size:', s.size())
    print('pop:', s.pop())
    print('size:', s.size())
    
    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





