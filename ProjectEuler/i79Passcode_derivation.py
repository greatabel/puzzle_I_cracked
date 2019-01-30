'''
A common security method used for online banking is to ask the user 
for three random characters from a passcode. For example, if the passcode was 531278, 
they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse 
the file so as to determine the shortest possible secret passcode of unknown length.
'''

import time
from termcolor import colored
from itertools import *
from collections import defaultdict



def main_process():
    myfile = open('i79_keylog.txt').read()
    known_nums = []
    for i in myfile.split('\n'):
        if i != '' and i not in known_nums:
            known_nums.append(i)

    print(colored('mycount=', 'red'), known_nums, len(known_nums))
    
    appearances = defaultdict(list)
    for attempt in known_nums:
        for i, n in enumerate(attempt):
            appearances[n].append(i)

    average_positions = {}
    for k,v in list(appearances.items()):
        average_positions[k] = float(sum(v))/float(len(v))

    a = [k for k,v in sorted(list(average_positions.items()), key=lambda a: a[1])]
    print(''.join(str(x) for x in a))


if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)