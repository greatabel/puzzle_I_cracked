'''
It is well known that if the square root of a natural number is not an integer, 
then it is irrational. The decimal expansion of such square roots is infinite 
without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., 
and the digital sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums 
of the first one hundred decimal digits for all the irrational square roots.
'''

import time
from termcolor import colored
from decimal import Decimal, localcontext


def main_process():
    total = 0
    for x in range(1,100):
        print('x=', x)
        with localcontext() as ctx:
            ctx.prec = 105
            if len(str(Decimal(x).sqrt())) == 1:
                total += 0
            else:
                a = sum([int(i) for i in str(Decimal(x).sqrt())[2:101]])+int(str(Decimal(x).sqrt())[0])
                print('a=', a)
                total += a

    print(colored('mycount=', 'red'), total)

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)