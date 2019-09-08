'''

给定一颗二叉树，要求逐层打印二叉树节点的数据，例如有如下二叉树：
     1
  2    3
 4 5  6 7

#----------------------------#

递归方法

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

# --------本题真正解题代码---------------#
def  print_by_level(root,level):

    if  root==None or level < 0:
        return  0
    elif  level == 0:
        print(root.data)
        return  1
    else:
        # 把打印根结点level层的结点转换为求解根结点的孩子结点的level-1层的结点。
        return  print_by_level(root.lchild, level - 1) \
                +print_by_level(root.rchild, level - 1)

def main_process():
    arr = [4, 2, 5, 1, 6, 3, 7]
    print('len(arr)=', len(arr), arr)
    root = array_to_tree(arr, 0, len(arr)-1)
    print_tree_mid_order(root)
    
    print('print_by_level:')
    print_by_level(root, 2)
    print_by_level(root, 1)
    print_by_level(root, 0)
    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)











