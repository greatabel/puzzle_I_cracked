'''
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by moving left, right, up, and down, 
is indicated in bold red and is equal to 2297.

⎛⎝⎜⎜⎜⎜⎜⎜131201630537805673968036997322343427464975241039654221213718150111956331⎞⎠⎟⎟⎟⎟⎟⎟
Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."),
 a 31K text file containing a 80 by 80 matrix, 
 from the top left to the bottom right by moving left, right, up, and down.
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