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

import time
from termcolor import colored


def main_process():
    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)




