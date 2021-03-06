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
from math import log

file_url = 'i99base_exp.txt'

def main_process():
    pairs = open(file_url).read().split('\n')
    # print(len(pairs))
    mv , ml = 0, 0
    for lnumber, line in enumerate(pairs):
        b, e = line.split(',')
        # print('lnumber=', lnumber, b, 'e=', e)
        v = int(e) * log(int(b))
        if v > mv:
            mv, ml = v, lnumber

    print(colored('mycount=', 'red'), ml + 1)

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)