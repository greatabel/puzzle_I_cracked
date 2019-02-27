'''
In the following equation x, y, and n are positive integers.

1
x
+   
1
y
=   
1
n
For n = 4 there are exactly three distinct solutions:

1
5
+   
1
20
=   
1
4
1
6
+   
1
12
=   
1
4
1
8
+   
1
8
=   
1
4
What is the least value of n for which the number of distinct solutions exceeds one-thousand?

NOTE: This problem is an easier version of Problem 110; it is strongly advised that you solve this one first.
'''

import math
import time
from termcolor import colored

def find_factor(n):
    # print("the:",n)
    factors = []
    for i in range(1, int(math.sqrt(n))+1 ):
        # print("i=",i)
        if n % i == 0:
            factors.append(i)
            if i != n//i:
                factors.append(n//i)
            
    return factors

def main_process():
    estimate_bound = 32464832000 # 25878772920 pair_count= 1024
    for i in range( estimate_bound - 10**3 ,  estimate_bound + 10 ** 3):
        factors = find_factor(i)
        pair_count = 0
        if len(factors) % 2 == 0:
            pair_count = len(factors) // 2
        else:
            pair_count = len(factors) // 2 + 1
        if pair_count > 100:
            print(i, 'pair_count=', pair_count)
        if pair_count > 1000:
            print(math.sqrt(i), 'found !', 'pair_count=', pair_count)
            break
    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)




