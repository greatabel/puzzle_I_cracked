'''
Su Doku (Japanese meaning number place) is the name given to a popular puzzle concept.
 Its origin is unclear, but credit must be attributed to Leonhard Euler who invented a similar, 
 and much more difficult, puzzle idea called Latin Squares. The objective of Su Doku puzzles, 
 however, is to replace the blanks (or zeros) in a 9 by 9 grid in such that each row, 
 column, and 3 by 3 box contains each of the digits 1 to 9. Below is an example of a typical 
 starting puzzle grid and its solution grid.

0 0 3
9 0 0
0 0 1   0 2 0
3 0 5
8 0 6   6 0 0
0 0 1
4 0 0
0 0 8
7 0 0
0 0 6   1 0 2
0 0 0
7 0 8   9 0 0
0 0 8
2 0 0
0 0 2
8 0 0
0 0 5   6 0 9
2 0 3
0 1 0   5 0 0
0 0 9
3 0 0

4 8 3
9 6 7
2 5 1   9 2 1
3 4 5
8 7 6   6 5 7
8 2 1
4 9 3
5 4 8
7 2 9
1 3 6   1 3 2
5 6 4
7 9 8   9 7 6
1 3 8
2 4 5
3 7 2
8 1 4
6 9 5   6 8 9
2 5 3
4 1 7   5 1 4
7 6 9
3 8 2
A well constructed Su Doku puzzle has a unique solution and can be solved by logic,
 although it may be necessary to employ "guess and test" methods in order to 
 eliminate options (there is much contested opinion over this). The complexity of the search
  determines the difficulty of the puzzle; the example above is considered easy because it can
   be solved by straight forward direct deduction.

The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'), 
contains fifty different Su Doku puzzles ranging in difficulty, but all with unique solutions 
(the first puzzle in the file is the example above).

By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left 
corner of each solution grid; for example, 483 is the 3-digit number found in the top left corner of 
the solution grid above.

'''

# https://blog.dreamshire.com/project-euler-96-solution/
import time
from termcolor import colored


s = 0
def same_row(i,j):
    return (i/9 == j/9)

def same_col(i,j):
    return (i-j) % 9 == 0

def same_block(i,j):
    return (i/27 == j/27 and (i % 9)/3 == (j % 9)/3)

def r(a):
    global s
    i = a.find('0')
    if i == -1:
        s+=int(a[0:3])

    excluded_numbers = set()
    for j in range(81):
        if same_row(i,j) or same_col(i,j) or same_block(i,j):
            excluded_numbers.add(a[j])

    for m in '123456789':
        if m not in excluded_numbers:
            r(a[:i] + m + a[i+1:])

def main_process():
    file = open('i96sudoku.txt','r').readlines()
    fx = ''.join([line[:9] for line in file if not 'Grid' in line])
    fx = [fx[i:(i+81)] for i in range(0,len(fx),81)]
    print('here')
    [r(p) for p in fx]
    print(colored('mycount=', 'red'), s)

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)













    