'''

给定2个单链表 链表每个节点代表1位数，计算2个数之和。例如：
输入(3->1->5) 和 （5->9->2)，输出 8->0->8，即是513 + 295 = 808
注意个位数在链表头

#----------------------------#

思路1: 最简单：先求出每个链表代表的整数，然后相加，缺点是：当链表代表数很大，就不行了
思路2: 对链表节点直接进行相加操作，然后相加的和存储到新链表对应节点，同时记录相加的进位

代码采用作者方案
'''




import time
from termcolor import colored


class  LNode:  
    def  __init__(self,x=None):  
        self.data=x 
        self.next=None

def  add(h1,h2):
       if  h1 is None or h1.next is None:
            return  h2
       if  h2 is None or h2.next is None:
            return  h1
       c = 0   #用来记录进位
       sums = 0  #用来记录两个结点相加的值
       p1 = h1.next  #用来遍历h1
       p2 = h2.next  #用来遍历h2
       tmp = None  #用来指向新创建的存储相加和的结点  
       resultHead = LNode() #相加后链表头结点
       resultHead.next = None
       p = resultHead #用来指向链表resultHead最后一个结点 
       while  p1 is not None and  p2 is not None:
           tmp = LNode()
           tmp.next = None
           sums = p1.data+p2.data+c
           tmp.data =  int(sums % 10) #两结点相加和
           c = sums/10  #进位
           p.next = tmp
           p = tmp
           p1 = p1.next
           p2 = p2.next
        # 链表h2比h1长，接下来只需要考虑h2剩余结点的值
       if  p1 is None:

          while  p2 is not None:
              tmp = LNode()
              tmp.next = None
              sums = p2.data+c
              tmp.data = int(sums % 10)
              c = sums/10
              p.next = tmp
              p = tmp
              p2 = p2.next
        # 链表h1比h2长，接下来只需要考虑h1剩余结点的值
       if  p2 is None:
            while  p1 is not None:
               tmp = LNode()
               tmp.next = None
               sums = p1.data+c
               tmp.data = int(sums % 10)
               c = sums/10
               p.next = tmp
               p = tmp
               p1 = p1.next
        # 如果计算完成后还有进位，则增加新的结点
       if  c == 1:
           tmp = LNode()
           tmp.next = None
           tmp.data = 1
           p.next = tmp   
       return  resultHead

def main_process():
    i = 1
    head1 = LNode()
    head1.next = None
    head2 = LNode()
    head2.next = None
    tmp = None
    cur = head1    
    addResult = None   
     # 构造第一个链表
    while  i<7:
       tmp = LNode()
       tmp.data = i+2
       tmp.next = None
       cur.next = tmp
       cur = tmp
       i += 1    
    cur = head2
    # 构造第二个链表
    i = 9
    while  i>4:
       tmp = LNode()

       tmp.data = i
       tmp.next = None
       cur.next = tmp
       cur = tmp
       i -= 1    
    print("\nHead1: ")
    cur = head1.next
    while  cur is not None:
       print(cur.data)
       cur = cur.next  
    print("\nHead2: ")
    cur = head2.next
    while  cur is not None:
       print(cur.data)
       cur = cur.next
    addResult = add(head1,head2)
    print("\n相加后: ")
    cur = addResult.next
    while  cur is not None:
        print(cur.data)
        cur = cur.next

    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





