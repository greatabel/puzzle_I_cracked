'''
The radical of n, rad(n), is the product of distinct prime factors of n. 

For example, 504 = 23 × 32 × 7, so rad(504) = 2 × 3 × 7 = 42.

We shall define the triplet of positive integers (a, b, c) to be an abc-hit if:

GCD(a, b) = GCD(a, c) = GCD(b, c) = 1
a < b
a + b = c
rad(abc) < c
For example, (5, 27, 32) is an abc-hit, because:

GCD(5, 27) = GCD(5, 32) = GCD(27, 32) = 1
5 < 27
5 + 27 = 32
rad(4320) = 30 < 32
It turns out that abc-hits are quite rare and there are only thirty-one abc-hits for c < 1000, with ∑c = 12523.

Find ∑c for c < 120000.


#----------------------------#

欧拉工程127: abc匹配

数n的基rad(n)被定义为n的不同质因数之积。例如504 = 23 × 32 × 7，所以rad(504) = 2 × 3 × 7 = 42。

我们定义正整数三元组(a, b, c)为abc匹配，当其满足如下条件：

GCD(a, b) = GCD(a, c) = GCD(b, c) = 1
a < b
a + b = c
rad(abc) < c
例如，(5, 27, 32)是一个abc匹配，因为：

GCD(5, 27) = GCD(5, 32) = GCD(27, 32) = 1
5 < 27
5 + 27 = 32
rad(4320) = 30 < 32
实际上，abc匹配是非常稀少的，对于c < 1000，只有31组abc匹配，在这些匹配中∑c = 12523。

对于c < 120000，求∑c。

#----------------------------#
思路：
rad(a * b * c) = rad (a) * rad(b) * rad(c)

'''




import time
from termcolor import colored
from math import gcd


limit = 120000

# 测试小范围数据
# limit = 1000
# limit = 20

def main_process():
    radicals = []
    for i in range(0, limit):
        radicals.append(1)
    # print(radicals)

    for i in range(2, limit):
        if radicals[i] == 1:
            radicals[i] = i
            # print(colored('i=', 'red'), i)
            for j in range(i * 2, limit, i):
                radicals[j] *= i
                # print(' i=', i,'j=', j,  'radicals[' , j , ']=', radicals[j])
    index = 0
    for item in radicals:
        # print(index, '=>', item)
        index += 1

    ans = 0
    # 太慢了

    # for a in range(1, limit):
    #     for b in range(a+1, limit-a):
    #         if radicals[a] * radicals[b] * radicals[a+b] >= (a+b):
    #             continue
    #         if gcd(a, b) != 1:
    #             continue
    #         result += (a+b)
    #         # print('c=', a+b)
    #         if a % 100 == 0:
    #             print(a)

    # 加速的方法
    sortedrads = sorted((rad, n) for (n, rad) in enumerate(radicals))
    # print(sortedrads)
    for c in range(2, limit):
        for (rad, a) in sortedrads:
            rad *= radicals[c]
            if rad >= c:
                break
            b = c - a
            if a < b and rad * radicals[b] < c and gcd(a, b) == 1:
                ans += c

    print(colored('mycount=', 'red'), ans)
    # 18407904

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)

