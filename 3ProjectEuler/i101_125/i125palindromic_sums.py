'''
The palindromic number 595 is interesting because it can be written as the 
sum of consecutive squares: 6^2 + 7^2 + 8^2 + 9^2 + 10^2 + 11^2 + 12^2.
There are exactly eleven palindromes below one-thousand that can be written 
as consecutive square sums, and the sum of these palindromes is 4164. 
Note that 1 = 0^2 + 1^2 has not been included as this problem is 
concerned with the squares of positive integers.
Find the sum of all the numbers less than 10^8 that are both palindromic and 
can be written as the sum of consecutive squares.

#----------------------------#
翻译：欧拉工程/欧拉项目 125 : 回文和

回文数595很有趣，因为它可以写成连续平方数的和：
6^2 + 7^2 + 8^2 + 9^2 + 10^2 + 11^2 + 12^2
恰好有十一个小于一千的回文数可以写成连续平方数的和，这些回文数的和是4164。
注意 1 = 0^2 + 1^2并没有算在内，因为本题只考虑正整数的平方。

在小于10^8的数中，找出所有可以写成连续平方数的和的回文数，并求它们的和。

#----------------------------#
解题思路:
平方和计算公式：
n^2 + (n-1)^2 + ... + 1^2 = n* (n+1)*(2n+1)/6
然后可以看到 这些数的上限在 更号（limit）之类
然后我们在这个范围里面遍历所有可能的平方和，通过我们的公式（其实
通过数学方法肯定可以 化简 slice_square_sum，但是算了）

检验是否是回文就行了，是的就加上

'''

import math
import time
from termcolor import colored


# copy from i04
def palindromic(num):
    # print('num=', num)
    results = []
    while num > 0:
        results.append(num%10)
        num = round((num-num%10 )/10)
    # print("results=", results)
    flag = (results == list(reversed(results)))
    # if flag:
    #     print("flag:",list(reversed(results)))

    return flag


total_limit = 10**8
# total_limit = 1000
limit = int(math.sqrt(total_limit))

def square_sum(n):
    return n * (n+1) * (2*n + 1)/6


def slice_square_sum(start, end):
    return square_sum(end) - square_sum(start) + start ** 2


def main_process():
    # for i in range(100, 135):
    #     palindromic(i)
    pset = set()
    flag = False
    for i in range(1, limit):
        for j in range(i+1, limit):
            p = slice_square_sum(i, j)
            if p < total_limit:
                if palindromic(p) and (p!=0) and (p!=1):                
                        pset.add(p)
                # if i % 100 == 0:
                #     print(i, j, 'palindromic sum:', p)
            else:
                break
              

    print(colored('mycount=', 'red'), int(sum(pset)))
    # mycount= 2906969179

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)


