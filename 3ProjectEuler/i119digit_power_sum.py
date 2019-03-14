'''
The number 512 is interesting because it is equal to the sum of its digits 
raised to some power: 5 + 1 + 2 = 8, and 8^3 = 512. 

Another example of a number with this property is 614656 = 28^4.

We shall define an to be the nth term of this sequence and 

insist that a number must contain at least two digits to have a sum.

You are given that a2 = 512 and a10 = 614656.

Find a30.
'''

import math
import time
from termcolor import colored


def digit_sum(n):
    num_str = str(n)
    sum = 0
    for i in range(0, len(num_str)):
        sum += int(num_str[i])
    return sum


def interesting(n):
    x = digit_sum(n)
    if x < 2:
        return False
    y = math.log(n, x)
    decimal_y = y % 1
    # python log bug
    # print(' ', n, 'decimal_y=', decimal_y)
    if decimal_y < 0.0000001 or decimal_y > 0.9999999:
        return True
    

def main_process():

    mycount = 0
    i = 50
    while mycount < 30:
        i += 1
        if interesting(i):
            mycount += 1
            print('mycount:',mycount, i)


    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)