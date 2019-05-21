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



limit = 100

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


def f(n, d):
    count = 0
    t = 1
    while n // t != 0:
        lower_number = n - (n // t) * t
        curr_number = (n // t) % 10
        higher_number = n // (t * 10)
        if curr_number < d:
            count += higher_number * t
        elif curr_number == d:
            count += higher_number * t + lower_number + 1
        else:
            count += (higher_number + 1) * t
        t *= 10
    return count

def main_process():
    # guess_patternI()
    for i in range(25):
        print(i, f(i, 1))

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)







