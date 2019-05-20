'''

There are several ways to write the number 1/2 as a sum of inverse squares using distinct integers.

For instance, the numbers {2,3,4,5,7,12,15,20,28,35} can be used:

12=122+132+142+152+172+1122+1152+1202+1282+1352
In fact, only using integers between 2 and 45 inclusive, there are exactly three ways to do it, 

the remaining two being: {2,3,4,6,7,9,10,20,28,35,36,45} and {2,3,4,6,7,9,12,15,28,30,35,36,45}.

How many ways are there to write the number 1/2 as a sum of inverse squares using distinct integers 

between 2 and 80 inclusive?

#----------------------------#

欧拉工程152: 将1/2写成平方数的倒数和

有许多种方式将1/2写成一系列不同整数的平方的倒数和。

例如，可以用这些数{2,3,4,5,7,12,15,20,28,35}：


事实上，只用2至45之间的数的方式一共有三种，另两种分别是：{2,3,4,6,7,9,10,20,28,35,36,45}和

{2,3,4,6,7,9,12,15,28,30,35,36,45}。

如果只用2至80之间的数，将1/2写成不同整数的平方的倒数和共有多少种方式？

'''










import time
from termcolor import colored


def main_process():
    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)
