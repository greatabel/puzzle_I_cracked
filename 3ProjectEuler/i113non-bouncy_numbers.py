'''
Working from left-to-right if no digit is exceeded by the digit to its left 
it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; 
for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; 
for example, 155349.

As n increases, the proportion of bouncy numbers below n increases such that there are 
only 12951 numbers below one-million that are not bouncy and only 277032 non-bouncy numbers below 1010.

How many numbers below a googol (10100) are not bouncy?
'''

# 很明显不能用i112思路了，而是要在 < 10**10 有277032 个不是bouncy 数的基础上，
# 构造出其他的 升序数和 降序数，然后 277032 + 这些构造出来的数的数目
import time
from termcolor import colored


def combination(n, k):
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in range(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0

def increase_situation(n):
    '''
    # 影射二进制字符串算法：
    https://mathschallenge.net/full/never_decreasing_digits
    example: 1223 <-> + # + # # + #
    里面+ 表示+1 （起始值为0），# 表示打印一个数字
    于是，就有了n 个#， 9个 + ，我们可以选择怎么选择在n中插入9个+
    变成从 n+9 中选择9个位置的组合问题

    需要注意的是：减去为0的情况
    '''
    return combination(n+9, 9) - 1

def decrease_situation(n):
    '''
    和升序类似，只不过起始值从0变成9，然后操作符是减法 -
    exmaple： 9887 <-->  # - # # - #
    与增加不同的是 我们可以插入0，因为不是在开头了
    于是问题变成了 n个#，10个-，我们于是有了 n+10 中选择 10个插入位置

    但是参考 i113decrease_situation.jpeg 的右下角可知
    都为0的情况，可以有n+1种
    '''
    return combination(n+10, 10) - (n+1)

def main_process():
    n = 100
    increase_num = increase_situation(n)
    decrease_num = decrease_situation(n)
    '''
    但是increase_num 和 decrease_num 有重复的部分：
    1， 11， 111， …… 111···1 共有n个
    2， 22， 222， ……, 222···2 共有n个
    ……
    9， 99 ……， 999····9 共有n个
    总共9n个
    '''
    not_bouncy = increase_num + decrease_num - 9 * n
    # for i in range(1, 6):
    #     print('combination(6, ' + str(i) +')=', combination(6, i))
    # ans is 51161058134250
    print(colored('mycount=', 'red'), not_bouncy)

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)