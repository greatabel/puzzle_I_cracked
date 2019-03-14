'''
The number 512 is interesting because it is equal to the sum of its digits 
raised to some power: 5 + 1 + 2 = 8, and 8^3 = 512. 

Another example of a number with this property is 614656 = 28^4.

We shall define an to be the nth term of this sequence and 

insist that a number must contain at least two digits to have a sum.

You are given that a2 = 512 and a10 = 614656.

Find a30.
'''

import time
from termcolor import colored


def check(n):
    x = sum(int(digit) for digit in str(n))
    for i in range(0, 5):
        print(i, x ** i)
    

def main_process():
    check(512)
    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)