'''

A composite number can be factored many different ways. For instance,

 not including multiplication by one, 24 can be factored in 7 distinct ways:

24 = 2x2x2x3
24 = 2x3x4
24 = 2x2x6
24 = 4x6
24 = 3x8
24 = 2x12
24 = 24
Recall that the digital root of a number, in base 10, is found by adding together the digits of that number, 

and repeating that process until a number is arrived at that is less than 10. Thus the digital root of 467 is 8.

We shall call a Digital Root Sum (DRS) the sum of the digital roots of the individual factors of our number.
The chart below demonstrates all of the DRS values for 24.

Factorisation   Digital Root Sum
2x2x2x3
9
2x3x4
9
2x2x6
10
4x6
10
3x8
11
2x12
5
24
6
The maximum Digital Root Sum of 24 is 11.
The function mdrs(n) gives the maximum Digital Root Sum of n. So mdrs(24)=11.
Find ∑mdrs(n) for 1 < n < 1,000,000.

#----------------------------#

欧拉工程159: 分解约数数字根之和

每个合数都有很多种分解约数的方式。例如，如果不允许多次乘1，有7种不同的方式分解24的约数：

24 = 2x2x2x3
24 = 2x3x4
24 = 2x2x6
24 = 4x6
24 = 3x8
24 = 2x12
24 = 24

在十进制下，一个数的数字根是不断重复将其各位数字相加，直到得到的结果小于10为止。因此467的数字根是8。

我们记数字根和（DRS）是所有分解出的约数的数字根之和。
下表是24的所有约数分解的DRS值。

约数分解    数字根和
2x2x2x3 9
2x3x4   9
2x2x6   10
4x6 10
3x8 11
2x12    5
24  6
对于24的所有分解，最大的数字根和是11。
函数mdrs(n)表示对于n的不同分解最大的数字根和。因此mdrs(24)=11。
对于1 < n < 1,000,000，求∑mdrs(n)。



'''



from functools import reduce
import time
from termcolor import colored


def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

ds = {}

def digital_root(n):
    if n in ds:
        return ds[n]
    else:
        out_n = n
        while n >= 10:
            sn = str(n)
            n = sum(int(d) for d in sn)
        ds[out_n] = n
        return n

    


def main_process():
    fs = factors(24)
    ds = digital_root(24)
    print(fs, ds)
    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





