'''

Consider the infinite polynomial series AF(x) = xF1 + x2F2 + x3F3 + ..., 

where Fk is the kth term in the Fibonacci sequence: 1, 1, 2, 3, 5, 8, ... ; 

that is, Fk = Fk−1 + Fk−2, F1 = 1 and F2 = 1.

For this problem we shall be interested in values of x for which AF(x) is a positive integer.

Surprisingly AF(1/2)     =  (1/2).1 + (1/2)2.1 + (1/2)3.2 + (1/2)4.3 + (1/2)5.5 + ...
     =  1/2 + 1/4 + 2/8 + 3/16 + 5/32 + ...
     =  2
The corresponding values of x for the first five natural numbers are shown below.

x   AF(x)
√2−1    1
1/2 2
(√13−2)/3   3
(√89−5)/8   4
(√34−3)/5   5
We shall call AF(x) a golden nugget if x is rational, because they become increasingly rarer; 

for example, the 10th golden nugget is 74049690.

Find the 15th golden nugget.

#----------------------------#


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
