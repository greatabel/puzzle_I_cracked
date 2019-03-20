'''
The radical of n, rad(n), is the product of the distinct prime factors of n. For example, 
504 = 23 × 32 × 7, so rad(504) = 2 × 3 × 7 = 42.

If we calculate rad(n) for 1 ≤ n ≤ 10, then sort them on rad(n), and sorting on n 
if the radical values are equal, we get:

    Unsorted            Sorted   
n   rad(n)      n   rad(n)  k
1   1            1      1   1
2   2            2      2   2
3   3            4      2   3
4   2            8      2   4
5   5            3      3   5
6   6            9      3   6
7   7            5      5   7
8   2            6      6   8
9   3            7      7   9
10  10           10     10  10
Let E(k) be the kth element in the sorted n column; for example, E(4) = 8 and E(6) = 9.

If rad(n) is sorted for 1 ≤ n ≤ 100000, find E(10000).



#----------------------------#
翻译：欧拉工程 124: 基排序

数n的基rad(n)，是指n的不同质因数之积。例如，504 = 23 × 32 × 7，所以rad(504) = 2 × 3 × 7 = 42。

如果我们计算1 ≤ n ≤ 10的rad(n)，并先按照rad(n)再按照n从小到大排序，我们得到：

    Unsorted            Sorted   
n   rad(n)      n   rad(n)  k
1   1            1      1   1
2   2            2      2   2
3   3            4      2   3
4   2            8      2   4
5   5            3      3   5
6   6            9      3   6
7   7            5      5   7
8   2            6      6   8
9   3            7      7   9
10  10           10     10  10

记E(k)是前n个数排序后的第k个数，例如，E(4) = 8以及E(6) = 9。

对1 ≤ n ≤ 100000按照rad(n)排序后，求E(10000)。

#----------------------------#
思路：
老套路了，不可能硬来，我们先把 要求区间的所有素数找出来
然后创造一个每个数n 和 对应的基数rad(n), 作为一个数对，然后放入列表中
然后我们就使用筛法：默认每个i 属于n，开始基数都是1
从每一个素数开始，如果可以被整除，就 rad(i) 乘上这个素数，
…… 进行下去，因为素数列表的长度应该大大小于 n 的搜索空间
我们把所有的区间内的素数筛选所有的i 之后，基数就算好了，
然后就简单了，对列表进行根据基数排序
然后找到问题需要的第1w个是多少就行了。

'''



import time
from termcolor import colored
from i123primeSieve_demo import primeSieve

def main_process():
    limit = 10**5
    primes = primeSieve(limit)
    print(primes)
    print(colored('-'*20, 'red', attrs=['reverse', 'bold']))

    rads = [[1, i] for i in range(limit + 1)]
    print(rads)

    for p in primes:
        # print('\n', colored(p, 'red', attrs=['blink', 'bold']))
        for i in range(p, limit+1, p):
            # print(i, ' ', end='')
            rads[i][0] *= p
            # print('\n', rads)
    print(sorted(rads)[10000][1])
    print(colored('mycount=', 'red'), 'results')
    # 21417

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)



