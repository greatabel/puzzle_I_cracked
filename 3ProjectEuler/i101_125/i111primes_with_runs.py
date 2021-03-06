'''
Considering 4-digit primes containing repeated digits it is clear that they cannot all be the same: 
1111 is divisible by 11, 2222 is divisible by 22, and so on. But there are nine 4-digit primes 
containing three ones:

1117, 1151, 1171, 1181, 1511, 1811, 2111, 4111, 8111

We shall say that M(n, d) represents the maximum number of repeated digits for an n-digit prime 
where d is the repeated digit, N(n, d) represents the number of such primes, and S(n, d) represents 
the sum of these primes.

So M(4, 1) = 3 is the maximum number of repeated digits for a 4-digit prime where one is the repeated digit, 
there are N(4, 1) = 9 such primes, and the sum of these primes is S(4, 1) = 22275. It turns out that for d = 0, 
it is only possible to have M(4, 0) = 2 repeated digits, but there are N(4, 0) = 13 such cases.

In the same way we obtain the following results for 4-digit primes.

Digit, d    M(4, d) N(4, d) S(4, d)
0   2   13  67061
1   3   9   22275
2   3   1   2221
3   3   12  46214
4   3   2   8888
5   3   1   5557
6   3   1   6661
7   3   9   57863
8   3   1   8887
9   3   7   48073
For d = 0 to 9, the sum of all S(4, d) is 273700.

Find the sum of all S(10, d).
'''

'''
思路：欧拉工程套路都模式化了，暴力肯定不行的，在10**10范围内，除非能连上学校的超算
得想其他道道: 
1. 所有一样数字的10位数肯定不行，但是替换其中1位，看看是否是质数
2. 泡一轮看看1的情况是否包含所有的情况，然后发现有3个数字不行，这3个数字
   我们考虑替换2位数字，然后遍历，然后发现替换2位确实可以都涵盖了

'''
import time
from termcolor import colored
from math import sqrt
from itertools import count, islice
from itertools import product

Limit_bits = 10

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))


def generate_perfectlist(n):
    perfectlist = []
    perfectlist.append('0000000000')
    start = 1111111111
    for i in range(1, n):
        perfectlist.append(str(i * start))
    return perfectlist


def main_process():
    mysum = 0
    myprimes = []
    perfectlist = generate_perfectlist(Limit_bits)
    print(perfectlist)
    # for i in range(1, 10):
    #     if isPrime(i):
    #         print(i)
    targetlist = perfectlist.copy()
    print('targetlist=', targetlist)
    # 替换其中一位，看看是否就是素数
    for perfect in perfectlist:
        print('\nperfect=', perfect)
        flag = False
        # i 代表改成 哪个数字
        for i in range(0, 10):
            print('i=', i, '\n')    
            # j 代表改 哪个位置
            for j in range(0, 10):
                r = perfect
                r = r[:j] + str(i) + r[j + 1:]
                if isPrime(int(r)) and int(r) > 10 ** 9:
                    flag = True
                    if int(r) not in myprimes:
                        myprimes.append(int(r))
                        mysum += int(r)
                        print('r=', r)
        if flag:
            targetlist.remove(perfect)
    print('targetlist=', targetlist)

    # for i in product(list(range(0, 10)), repeat=2):
    #     print(p)
    for target in targetlist:
        for i in product(list(range(0, 10)), repeat=2):
            print('i=', i[0], '#', i[1])
            for j in product(list(range(0, 10)), repeat=2):
                t = target
                t = t[:j[0]] + str(i[0]) + t[j[0]+1:]

                t = t[:j[1]] + str(i[1]) + t[j[1]+1:]

                if isPrime(int(t)) and int(t) > 10 ** 9:
                    flag = True                    
                    if int(t) not in myprimes:
                        myprimes.append(int(t))
                        mysum += int(t)
                        print('t=', t)

    # 没找到的数字，我们试着替换2位
    # for remain in targetlist:
    #     for i in range(0, 10):
    #         for j in range(0, 10):
    #             r = perfect
    #             r = r[:j] + str(i) + r[j + 1:]
    #             for k in range(0, 10):

    print(colored('mycount=', 'red'), mysum)

    # 612407567715

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)



