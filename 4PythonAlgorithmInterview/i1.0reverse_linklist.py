'''
1.1 给定一个带头节点的单链表，将其逆序
即如果单链表原来为 head -> 1 -> 2 -> 3 逆序后变成 head -> 3 -> 2 -> 1

#----------------------------#

参考链接：
https://stackoverflow.com/questions/29242000/how-can-i-write-a-recursive-function-to-reverse-a-linked-list


'''


import time
from termcolor import colored


class Node:
    def __init__(self, data, nextnode=None):
        self.data = data
        self.nextnode = nextnode


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def add_node(self, data):
        new_node = Node(data, self.head)
        self.head = new_node
        self.size += 1

    def print_node(self):
        print('单链表的head -> ', end='')
        curr = self.head
        while curr:
            if curr.nextnode:
                print(curr.data, ' -> ', end='')
            else:
                print(curr.data)
            curr = curr.nextnode
        print('\n')

    def reverse_list(self):
        prev = None
        curr = self.head
        while curr:
            next = curr.nextnode
            curr.nextnode = prev
            prev = curr
            curr = next
        self.head = prev

    def reverse_list_recursive(self,item):
        if item.nextnode == None:
            self.head = item
            return
        self.reverse_list_recursive(item.nextnode)
        temp = item.nextnode
        temp.nextnode = item
        item.nextnode = None





def main_process():
    linkedlist = LinkedList()
    for i in reversed(range(1, 7+1)):        
        linkedlist.add_node(i)
        print('i=', i)


    linkedlist.print_node()

    print('reverse_list: 就地逆序')
    linkedlist.reverse_list()
    linkedlist.print_node()

    print('reverse_list_recursive:递归法')
    linkedlist.reverse_list_recursive(linkedlist.head)
    linkedlist.print_node()


    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





