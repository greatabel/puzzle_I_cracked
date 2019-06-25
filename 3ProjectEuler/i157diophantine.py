'''

Solving the diophantine equation 1/a+1/b= p/10n

Problem 157
Consider the diophantine equation 1/a+1/b= p/10n with a, b, p, n positive integers and a ≤ b.
For n=1 this equation has 20 solutions that are listed below:

1/1+1/1=20/10   1/1+1/2=15/10   1/1+1/5=12/10   1/1+1/10=11/10  1/2+1/2=10/10
1/2+1/5=7/10    1/2+1/10=6/10   1/3+1/6=5/10    1/3+1/15=4/10   1/4+1/4=5/10
1/4+1/20=3/10   1/5+1/5=4/10    1/5+1/10=3/10   1/6+1/30=2/10   1/10+1/10=2/10
1/11+1/110=1/10 1/12+1/60=1/10  1/14+1/35=1/10  1/15+1/30=1/10  1/20+1/20=1/10
How many solutions has this equation for 1 ≤ n ≤ 9?

#----------------------------#

解不定方程1/a+1/b= p/10n

考虑不定方程1/a+1/b= p/10n，其中a, b, p, n均为正整数，且a ≤ b。
对于n=1，这个方程有20个解，如下所示：

                 
1/1+1/1=20/10   1/1+1/2=15/10   1/1+1/5=12/10   1/1+1/10=11/10  1/2+1/2=10/10
1/2+1/5=7/10    1/2+1/10=6/10   1/3+1/6=5/10    1/3+1/15=4/10   1/4+1/4=5/10
1/4+1/20=3/10   1/5+1/5=4/10    1/5+1/10=3/10   1/6+1/30=2/10   1/10+1/10=2/10
1/11+1/110=1/10 1/12+1/60=1/10  1/14+1/35=1/10  1/15+1/30=1/10  1/20+1/20=1/10
对于1 ≤ n ≤ 9，方程一共有多少个解？

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





