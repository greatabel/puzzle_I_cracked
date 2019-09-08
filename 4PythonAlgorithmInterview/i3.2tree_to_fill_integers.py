'''

如何把一个有序整数数组放到二叉树

#----------------------------#



'''

import time
from termcolor import colored


class BiTNode:
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None

# 把有序数组转换为二叉树
def array_to_tree(arr, start, end):
    root = None
    if end >= start:
        root = BiTNode()
        mid = int((start + end + 1 )/2)
        # print('mid=', mid)
        root.data = arr[mid]

        #递归用左半部分构建root左子树
        root.lchild = array_to_tree(arr, start, mid-1)
        root.rchild = array_to_tree(arr, mid+1, end)
    else:
        root = None
    return root

# 用中序遍历到方式打印出二叉树节点内容
def print_tree_mid_order(root):
    if root == None:
        return 
    if root.lchild != None:
        print_tree_mid_order(root.lchild)
    print(root.data)
    if root.rchild != None:
        print_tree_mid_order(root.rchild)


def main_process():
    arr = list(range(1, 11))
    print('len(arr)=', len(arr), arr)
    root = array_to_tree(arr, 0, len(arr)-1)
    print_tree_mid_order(root)

    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





