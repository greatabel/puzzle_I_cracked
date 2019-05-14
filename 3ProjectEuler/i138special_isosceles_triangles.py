'''

Consider the isosceles triangle with base length, b = 16, and legs, L = 17.


By using the Pythagorean theorem it can be seen that the height of the triangle, h = √(172 − 82) = 15, 

which is one less than the base length.

With b = 272 and L = 305, we get h = 273, which is one more than the base length, 

and this is the second smallest isosceles triangle with the property that h = b ± 1.

Find ∑ L for the twelve smallest isosceles triangles for which h = b ± 1 and b, L are positive integers.

#----------------------------#

欧拉项目138: 特殊等腰三角形

考虑底为b = 16，腰为L = 17的等腰三角形。


使用毕达哥拉斯定理，我们可以求出三角形的高是h = √(172 − 82) = 15，恰好比底长小1。

当b = 272而L = 305时，可以算出h = 273，恰好比底长大1，而且这是满足性质h = b ± 1的三角形中第二小的。

对于最小的12个满足h = b ± 1且b，L均为正整数的等腰三角形，求∑ L。



'''



import time
from termcolor import colored
import functools


@functools.lru_cache(None)
def F(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return F(n-1) + F(n-2)

def main_process():
    index = 0
    mysum = 0
    for i in range(1, 13):
        i = 6 * i + 3
        index += 1
        print(index, F(i)/2)
        mysum += F(i)/2



    print(colored('mycount=', 'red'), mysum)
    # mycount= 1118049290473932
    
if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)
