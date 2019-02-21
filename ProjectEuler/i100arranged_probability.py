'''
If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, 
and two discs were taken at random, it can be seen that the probability of taking two blue discs,
 P(BB) = (15/21)×(14/20) = 1/2.

The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, 
is a box containing eighty-five blue discs and thirty-five red discs.

By finding the first arrangement to contain over 1012 = 1,000,000,000,000 discs in total, 
determine the number of blue discs that the box would contain.
'''

import time
from termcolor import colored

low_bound = 10 ** 12

# 在想过推理的帮助下 i100analysis.jpg
def main_process():
    n = 120
    b = 85
    while n <= low_bound:
        tempb = 3 * b + 2 * n - 2
        tempn = 4 * b + 3 * n - 3
        b = tempb
        n = tempn

    print(colored('mycount=', 'red'), 'total n=', n, 'b=', b)

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)