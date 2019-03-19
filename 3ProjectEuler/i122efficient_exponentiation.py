'''
The most naive way of computing ^15 requires fourteen multiplications:

n × n × ... × n = n^15

But using a "binary" method you can compute it in six multiplications:

n × n = n^2
n2 × n2 = n^4
n4 × n4 = n^8
n8 × n4 = n^12
n12 × n2 = n^14
n14 × n = n^15

However it is yet possible to compute it in only five multiplications:

n × n = n^2
n2 × n = n^3
n3 × n3 = n^6
n6 × n6 = n^12
n12 × n3 = n^15

We shall define m(k) to be the minimum number of multiplications to compute nk; for example m(15) = 5.

For 1 ≤ k ≤ 200, find ∑ m(k).




#----------------------------#
翻译：
欧拉工程/欧拉项目 122: 高效指数计算

计算n15最朴素的方式需要14次乘法：
n × n × … × n = n^15

但使用一个“二进制”的算法，你可以只用6次乘法：
n × n = n^2
n2 × n2 = n^4
n4 × n4 = n^8
n8 × n4 = n^12
n12 × n2 = n^14
n14 × n = n^15

然而，实际上仅用5次乘法也是可以的：

n × n = n^2
n2 × n = n^3
n3 × n3 = n^6
n6 × n6 = n^12
n12 × n3 = n^15

记m(k)是计算nk所需要的最少次数，例如m(15) = 5。

对于1 ≤ k ≤ 200，求∑m(k)。
'''

#----------------------------#
'''
稍微想一下，euler project的套路就应该明白：肯定不能通过纯直接方案: k很大时候，肯定划分方案搜索量太大


'''

import time
from termcolor import colored


def first_chain(x):
    if x <= 0:
        return []
    if x == 1:
        return [1]
    if x == 2:
        return [1, 2]

    res = []
    arr = [[1, 2]]
    while (1):
        temp = []
        for i in arr:
            for j in i:
                p = i[:]
                p.append(i[-1]+j)
                if p[-1] == x:
                    return p
                elif p[-1] < x:
                    temp.append(p)
        arr = temp[:]


def shortest_chain_len(x):
    return len(first_chain(x))

def main_process():
    isum = 0
    limit = 200
    for i in range(1, limit+1):        
        i_len = shortest_chain_len(i) - 1
        # r = first_chain(i)
        # 读题目 相乘次数永远比加法链 要少1次
        print('processing ', i, i_len)
        isum += i_len
    print(colored('mycount=', 'red'), isum)

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)





