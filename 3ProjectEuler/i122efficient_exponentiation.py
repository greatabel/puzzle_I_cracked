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


def main_process():

    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)





