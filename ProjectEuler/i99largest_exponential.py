'''
Comparing two numbers written in index form like 211 and 37 is not difficult, 
as any calculator would confirm that 211 = 2048 < 37 = 2187.

However, confirming that 632382518061 > 519432525806 would be much more difficult,
 as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file 
containing one thousand lines with a base/exponent pair on each line, determine
 which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.
'''

import time
from termcolor import colored


def main_process():
    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)