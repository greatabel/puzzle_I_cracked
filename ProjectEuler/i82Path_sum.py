'''
The minimal path sum in the 5 by 5 matrix below, by starting in any cell 
in the left column and finishing in any cell in the right column, and only moving up, down, 
and right, is indicated in red and bold; the sum is equal to 994.

⎛⎝⎜⎜⎜⎜⎜⎜131201630537805673968036997322343427464975241039654221213718150111956331⎞⎠⎟⎟⎟⎟⎟⎟
Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), 
a 31K text file containing a 80 by 80 matrix, from the left column to the right column.
'''

import time
from termcolor import colored


def main_process():
    myfile = open('i82_matrix.txt').read()
    matrix = []
    for line in myfile.split('\n'):
        if line and line != '':
            row = [int(r) for r in line.split(',')]
            matrix.append(row)
    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)