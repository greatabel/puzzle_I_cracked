'''
Working from left-to-right if no digit is exceeded by the digit to its left it is called 
an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; 
for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; 
for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers 
below one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy
 numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion
 of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%.
'''

import time
from termcolor import colored


def is_increase(n):
    n = str(n)
    for i in range(len(n)-1):
        if int(n[i+1]) < int(n[i]):
            return False
    return True

def construct_increase(limit):
    return 0

def construct_decrease(limit):
    return 0

def main_process():
    total = 100
    inc = construct_increase(total)
    dec = construct_decrease(total)
    for i in range(190, 210):
        print(i, 'is_increase=', is_increase(i))
        
    print(colored('mycount=', 'red'), total - inc  - dec)

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)