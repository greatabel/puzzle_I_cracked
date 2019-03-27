'''
A hexagonal tile with number 1 is surrounded by a ring of six hexagonal tiles, 
starting at "12 o'clock" and numbering the tiles 2 to 7 in an anti-clockwise direction.

New rings are added in the same fashion, with the next rings being numbered 8 to 19, 
20 to 37, 38 to 61, and so on. The diagram below shows the first three rings.


By finding the difference between tile n and each of its six neighbours 
we shall define PD(n) to be the number of those differences which are prime.

For example, working clockwise around tile 8 the differences are 12, 29, 11, 6, 1, and 13. So PD(8) = 3.

In the same way, the differences around tile 17 are 1, 17, 16, 1, 11, and 10, hence PD(17) = 2.

It can be shown that the maximum value of PD(n) is 3.

If all of the tiles for which PD(n) = 3 are listed in ascending order to form a sequence,
 the 10th tile would be 271.

Find the 2000th tile in this sequence.

#----------------------------#

欧拉工程/项目 128: 六边形地砖的差

标有数1的六边形地砖被一圈六个六边形地砖包围，这些地砖从12点钟方向（正上方）开始沿逆时针顺序依次标记为2至7。

在这个图形的外面，继续加上新的六边形地砖，接下来的几圈分别按照同样的规则标上8至19，20至37，38至61，

依此类推。下图显示了前三圈所构成的图形。


考虑标有n的地砖与其周围六块地砖的差，我们定义PD(n)是这些差中素数的数目。

例如，按顺时针顺序，标有8的地砖与周围地砖的差是12，29，11，6，1和13。所以PD(8) = 3。

同样的，标有17的地砖与周围地砖的差是1，17，16，1，11和10，所以PD(17) = 2。

可以验证，PD(n)的最大值就是3。

如果所有PD(n) = 3的地砖构成从小到大排列的序列，那么第10块将是标有271的地砖。

找出这个序列中的第2000块地砖所标的数。

#----------------------------#
这题完全是数学分析题目，跳过此题，不想解这道题
'''



import itertools
from itertools import count, islice
from math import sqrt
import time
from termcolor import colored


def isprime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def main_process():
    count = 1
    limit = 2000
    # limit = 10
    n = 0
    number = 0

    while (count < limit):
        n+=1
        if (isprime(6 * n - 1) and isprime(6 * n + 1) and isprime(12 * n + 5)):
            count += 1
            number = (3 * n * n - 3*n + 2)
            if (count >= limit):
                break
        
        if (isprime(6 * n + 5) and isprime(6 * n - 1) and isprime(12 * n - 7) and n != 1):
            count += 1
            number = (3 * n * n + 3*n + 1)                                    
        
    

    print(colored('mycount=', 'red'), number)
    # 14516824220

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)