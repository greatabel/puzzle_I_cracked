'''

1.2 给定一个没有排序的连标，去掉重复项，并保留顺序
例如1->3->1->5->5->7
变成1->3->5->7

#----------------------------#

参考：https://www.youtube.com/watch?v=e2TjJMhe08U


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
        curr = self.head
        while curr:
            if curr.nextnode:
                print(curr.data, ' -> ', end='')
            else:
                print(curr.data)
            curr = curr.nextnode
        print('\n')

    def remove_duplicate(self):
        curr = self.head
        while curr:
            # if curr.nextnode:
            #     print(curr.data, ' -> ', end='')
            # else:
            #     print(curr.data)
            myprev = curr
            mynext = curr.nextnode
            while mynext:
                if mynext.data == curr.data:
                    # print('curr=', curr.data, 'prev=', myprev.data, 'next=', mynext.data)
                    myprev.nextnode = mynext.nextnode
                myprev = myprev.nextnode
                mynext = mynext.nextnode
            curr = curr.nextnode

    # 方法3: 考虑实用字典, 空间换时间
    def remove_with_dict(self):
        cur = self.head
        prev = None
        dup_values = dict()

        while cur:
            if cur.data in dup_values:
                # remove
                prev.nextnode = cur.nextnode
                cur = None
            else:
                dup_values[cur.data] = 1
                prev = cur
                # print('#', cur.data)
            cur = prev.nextnode

# 递归方法
def remove_dups(lst):
    if len(lst)>1:

        if lst[0] != lst[1]:
            return [lst[0]] + remove_dups(lst[1:])

        del lst[1]
        return remove_dups(lst)
    else:
        return lst


def main_process():
    linkedlist = LinkedList()
    for i in reversed(range(1, 7+1)):      
        linkedlist.add_node(i)
        if i % 2 == 0:
            linkedlist.add_node(i)
        print('i=', i)

    linkedlist.print_node()

    import copy
    linkedlist_a = copy.deepcopy(linkedlist)
    print('remove_duplicate')
    linkedlist.remove_duplicate()
    linkedlist.print_node()

    print('remove_with_dict')
    linkedlist_a.remove_with_dict()
    linkedlist_a.print_node()


    print('remove_duplicate recursive 递归方法')
    print(remove_dups([1,2,2,3,4,4,5,6,6,7]))

    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





