'''

Starting from zero the natural numbers are written down in base 10 like this: 
0 1 2 3 4 5 6 7 8 9 10 11 12....

Consider the digit d=1. After we write down each number n, we will update the number of ones
that have occurred and call this number f(n,1). The first values for f(n,1), then, are as follows:

n   f(n,1)
0   0
1   1
2   1
3   1
4   1
5   1
6   1
7   1
8   1
9   1
10  2
11  4
12  5
Note that f(n,1) never equals 3. 
So the first two solutions of the equation f(n,1)=n are n=0 and n=1. The next solution is n=199981.

In the same manner the function f(n,d) gives the total number of digits d that have been written
 down after the number n has been written. 
In fact, for every digit d ≠ 0, 0 is the first solution of the equation f(n,d)=n.

Let s(d) be the sum of all the solutions for which f(n,d)=n. 
You are given that s(1)=22786974071.

Find ∑ s(d) for 1 ≤ d ≤ 9.

Note: if, for some n, f(n,d)=n for more than one value of d this value of n is counted again 
for every value of d for which f(n,d)=n.

#----------------------------#

数字计数

从零开始的自然数在十进制中如下表示：
0 1 2 3 4 5 6 7 8 9 10 11 12….

考虑数字d=1。当我们写下数n之后，我们计算一下到目前为止数字1出现的次数，并记为f(n,1)。f(n,1)的前面一部分值如下所示：

n   f(n,1)
0   0
1   1
2   1
3   1
4   1
5   1
6   1
7   1
8   1
9   1
10  2
11  4
12  5
注意到f(n,1)从不等于3。
等式f(n,1)=n的前两个解是n=0和n=1，下一个解是n=199981。

同样地我们记f(n,d)表示在写下n之后d出现的次数。
事实上，对于任意一个数字d ≠ 0，0都是方程f(n,d)=n的第一个解。

记s(d)是所有f(n,d)=n的解的和。
已知s(1)=22786974071。

对于1 ≤ d ≤ 9，求∑ s(d)。

注意：如果对于某些n，对于多于一个的d均满足f(n,d)=n，这个数n对于每个d都要计算一遍。



'''




import time
from termcolor import colored





'''
step 1:
详细分析在：i156_f(n,d)_step1.png
先根据10， 100， 1000，1000的规律找出每个数字出现频率，
'''
def guess_patternI():
    # f_guessI(0, 1)
    dic = {}
    for i in range(1, 10):
        dic[i] = 0
    print(dic)

    for limit in (10, 100, 1000, 10000, 100000):
        for i in range(limit):
            digits = [int(x) for x in str(i)]
            for digit in digits:
                if digit in dic:
                    dic[digit] += 1
            # print(digits)

        print('limit=', limit, dic)
        dic = {}
        for i in range(1, 10):
            dic[i] = 0


'''
step 2: 
详细分析在：i156_f(n,d)_step1.png
然后结合下面分析 👇：
 https://math.stackexchange.com/questions/47477/number-of-occurrences-of
 -the-digit-1-in-the-numbers-from-0-to-n

实现出f(n, d)
'''
def f(n, d):
    count = 0
    t = 1
    while n // t != 0:
        lower = n - (n // t) * t
        num = (n // t) % 10
        higher = n // (t * 10)
        if num < d:
            count += higher * t
        elif num == d:
            count += higher * t + lower + 1
        else:
            count += (higher + 1) * t
        t *= 10
    return count

'''
step 3:
既然0，1，2，……9 这些数字的频率是一样的，我们在考察s(d)的时候我们可以
忽略具体的数字。选1吧，然后我们跑不同范围的1000，10000，10000……
可以看到f(n,d) 的增长趋势是超过n的：
f( 100000000 , 1 )= 0.80000001
f( 200000000 , 1 )= 1.3
f( 300000000 , 1 )= 1.1333333333333333
f( 400000000 , 1 )= 1.05
f( 500000000 , 1 )= 1.0
f( 600000000 , 1 )= 0.9666666666666667
f( 700000000 , 1 )= 0.9428571428571428
f( 800000000 , 1 )= 0.925
f( 900000000 , 1 )= 0.9111111111111111
time= 78.168046

然后我们找出这个点的大致范围：

n= 10000 指数i: 4
0.4001  0.4  0.4  0.4  0.4  0.4  0.4  0.4  0.4  

n= 100000 指数i: 5
0.50001  0.5  0.5  0.5  0.5  0.5  0.5  0.5  0.5  

n= 1000000 指数i: 6
0.600001  0.6  0.6  0.6  0.6  0.6  0.6  0.6  0.6  

n= 10000000 指数i: 7
0.7000001  0.7  0.7  0.7  0.7  0.7  0.7  0.7  0.7  

n= 100000000 指数i: 8
0.80000001  0.8  0.8  0.8  0.8  0.8  0.8  0.8  0.8  

n= 1000000000 指数i: 9
0.900000001  0.9  0.9  0.9  0.9  0.9  0.9  0.9  0.9  

n= 10000000000 指数i: 10
1.0000000001  1.0  1.0  1.0  1.0  1.0  1.0  1.0  1.0 

可知基本大于 10**10 范围，不用考虑，不会有相等的情况发生 =>
'''
limit = 10**11
finals = []

def bsearch(lower, upper, digit):
    global finals
    if lower + 1 == upper:
        if f(lower, digit) == lower:
            finals.append(lower)
            # print('@',len(finals))
        return
    middle = (lower + upper) // 2
    lower_value = f(lower, digit)
    upper_value = f(upper, digit)
    middle_value = f(middle, digit)
    if middle_value >= lower and middle >= lower_value:
        bsearch(lower, middle, digit)
    if upper_value >= middle and upper >= middle_value:     
        bsearch(middle, upper, digit)


def main_process():
    global finals
    # step 1 ---->
    # guess_patternI()

    # for i in range(1, 10**9):
    #     # for d in range(1, 10):
    #     if i % 10**8 == 0:
    #         print("f(",i, ',', 1, ')=', f(i, 1)/i)
    
    # step 2 ---->
    # for i in range(11):
    #     n = 10 ** i
    #     print('\n\nn=', n, '指数i:', i)
    #     for d in range(1, 10):
    #         print(f(n, d)/n, ' ', end='')
    total = 0
    for d in range(1, 10):
        finals = []
        bsearch(1, limit, d)
        # print(d, '#'*5, sum(finals))
        total += sum(finals)

    print(colored('mycount=', 'red'), total)
    # mycount= 21295121502550


if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)
