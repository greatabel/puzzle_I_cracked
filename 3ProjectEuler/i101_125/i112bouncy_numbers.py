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

def is_decrease(n):
    n = str(n)
    for i in range(len(n)-1):
        if int(n[i+1]) > int(n[i]):
            return False
    return True

def is_bouncy(n):
    increase = is_increase(n)
    decrease = is_decrease(n)
    if not increase and not decrease:
        return True
    else:
        return False


def main_process():
    i = 0 
    t = 0
    bouncy_count = 0
    while t < 0.99:
        i += 1
        if is_bouncy(i):
            bouncy_count += 1
        t = bouncy_count / i

        if i % 10 ** 4 == 0:
            print(i)


    # for i in range(190, 220):
    #     print(i, 'is_increase=', is_increase(i), 'is_decrease=', is_decrease(i))

    print(colored('mycount=', 'red'), i)

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)