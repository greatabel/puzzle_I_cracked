'''

Consider the infinite polynomial series AF(x) = xF1 + x2F2 + x3F3 + ..., 

where Fk is the kth term in the Fibonacci sequence: 1, 1, 2, 3, 5, 8, ... ; 

that is, Fk = Fk−1 + Fk−2, F1 = 1 and F2 = 1.

For this problem we shall be interested in values of x for which AF(x) is a positive integer.

Surprisingly AF(1/2)     =  (1/2).1 + (1/2)2.1 + (1/2)3.2 + (1/2)4.3 + (1/2)5.5 + ...
     =  1/2 + 1/4 + 2/8 + 3/16 + 5/32 + ...
     =  2
The corresponding values of x for the first five natural numbers are shown below.

x   AF(x)
√2−1    1
1/2 2
(√13−2)/3   3
(√89−5)/8   4
(√34−3)/5   5
We shall call AF(x) a golden nugget if x is rational, because they become increasingly rarer; 

for example, the 10th golden nugget is 74049690.

Find the 15th golden nugget.

#----------------------------#

欧拉工程137: 斐波那契金块

考虑无穷级数AF(x) = xF1 + x2F2 + x3F3 + …, 其中Fk是斐波那契数列的第k项：

1, 1, 2, 3, 5, 8, …；该数列由如下方式定义：Fk = Fk−1 + Fk−2，其中F1 = 1且F2 = 1。

在这个问题中，我们感兴趣的是那些使得AF(x)为正整数的x。

其中一个特别的解是：

         
AF(1/2) =   (1/2).1 + (1/2)2.1 + (1/2)3.2 + (1/2)4.3 + (1/2)5.5 + …
    =   1/2 + 1/4 + 2/8 + 3/16 + 5/32 + …
    =   2
对应于前五个自然数的x如下所示。

x   AF(x)
√2−1    1
1/2 2
(√13−2)/3   3
(√89−5)/8   4
(√34−3)/5   5
当x是有理数时，我们称AF(x)是一个斐波那契金块，因为这样的数将会变得越来越稀少，

例如，第10个斐波那契金块将是74049690。

求第15个斐波那契金块。

#----------------------------#

感觉这种题目，应该拉马努金这种喜欢连分数的人来一下搞定

'''



import time
from termcolor import colored
import math
import functools

# too slow version, need to speed up

@functools.lru_cache(None)
def F(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return F(n-1) + F(n-2)


def observe_phase_of_square():
    i = 0
    for n in range(0, 10**5):
        s = 5 * n**2 + 2*n + 1
        root = math.sqrt(s)
        if root.is_integer():
            print('i=', i, n, 'sum=', s, root)
            i += 1


def observe_F():
    for i in range(20):
        print('F(', i, ')=', F(i))


def n_assumption_from_observe(i):
    return F(2*i) * F(2*i+1)


def x_assumption(n):
    s = 5 * n**2 + 2*n + 1
    item = math.sqrt(s)
    x =( - (n+1) + item ) / 2*n
    return x

def main_process():
    # observe_phase_of_square()
    # observe_F()
    # 从 上面的探索和 i137.png 分析可知
    index = 0
    for i in range(100):
        n = n_assumption_from_observe(i)
        x = x_assumption(n)
        if x.is_integer():
            index += 1
            print(i, 'n=', n, 'x=', x, 'index=', index)
            if index >= 16:
                # 0 要排除，因为x 需要是正整数
                break

    print(colored('mycount=', 'red'), 'results')
    # 15 n= 1120149658760 x= 7.754690363390088e+23

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)
