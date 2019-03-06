'''
Working from left-to-right if no digit is exceeded by the digit to its left 
it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; 
for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; 
for example, 155349.

As n increases, the proportion of bouncy numbers below n increases such that there are 
only 12951 numbers below one-million that are not bouncy and only 277032 non-bouncy numbers below 1010.

How many numbers below a googol (10100) are not bouncy?
'''

# 很明显不能用i112思路了，而是要在 < 10**10 有277032 个不是bouncy 数的基础上，
# 构造出其他的 升序数和 降序数，然后 277032 + 这些构造出来的数的数目
import time
from termcolor import colored


def generate_increase(n):
    if n < 10:
        for i in range(1, n+1):
            print(i)


def main_process():
    generate_increase(9)
    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)