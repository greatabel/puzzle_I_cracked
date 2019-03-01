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
# I do not want to solve this problem , solution use:
# https://github.com/AntonKueltz/project-euler/blob/master/python/euler96.py
import time
from termcolor import colored
def read_in_puzzles():
    f = open("i96sudoku.txt", "r")
    lines = f.read().split("\n")

    puzzles = []
    puzzle = []
    for i, line in enumerate(lines):
        if line[:4] == "Grid":
            puzzle = []
        else:
            puzzle.append([int(c) for c in line])
            if i % 10 == 9:
                puzzles.append(puzzle)

    return puzzles

def rowcol_elim(puzzle, row, col, not_in_box):
    for val in list(not_in_box):
        can_go_elsewhere = False
        
        for i in range(int(row/3)*3, int(row/3)*3+3):
            for j in range(int(col/3)*3, int(col/3)*3+3):
                if (i, j) == (row, col): continue
                if puzzle[i][j] != 0: continue
                if val in puzzle[i]: continue

                column = []
                for k in range(len(puzzle)):
                    column.append(puzzle[k][j])
                if val in column: continue

                can_go_elsewhere = True

        if not can_go_elsewhere: return val
    return 0    

def solve_square(puzzle, row, col, backtrack=False):
    tmp = []
    for i in range(len(puzzle[row])):
        if puzzle[row][i] != 0: tmp.append(puzzle[row][i])
    not_in_row = set(range(1,10)).difference(set(tmp))

    tmp = []
    for i in range(len(puzzle)):
        if puzzle[i][col] != 0: tmp.append(puzzle[i][col])
    not_in_col = set(range(1,10)).difference(set(tmp))

    tmp = []
    for i in range(int(row/3)*3, int(row/3)*3+3):
        for j in range(int(col/3)*3, int(col/3)*3+3):
            if puzzle[i][j] != 0: tmp.append(puzzle[i][j])
    not_in_box = set(range(1,10)).difference(set(tmp))

    candidates = not_in_row.intersection(not_in_col.intersection(not_in_box))
    if backtrack: return list(candidates)
    if len(candidates) == 1: return list(candidates)[0]
    else: return rowcol_elim(puzzle, row, col, not_in_box)

def valid(puzzle, row, col, val):
    column = []
    for i in range(len(puzzle)):
        if i != row: column.append(puzzle[i][col])

    row_ = []
    for i in range(len(puzzle[row])):
        if i != col: row_.append(puzzle[row][i])

    box = []
    for i in range(int(row/3)*3, int(row/3)*3+3):
        for j in range(int(col/3)*3, int(col/3)*3+3):
            if (i, j) != (row, col): box.append(puzzle[i][j])
    
    return (not val in row_) and \
           (not val in column) and \
           (not val in box)

def validpuzzle(puzzle):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0: return False
            if not valid(puzzle, i, j, puzzle[i][j]): return False
    return True

def backtrack(puzzle):
    if validpuzzle(puzzle): return puzzle

    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                for val in range(1,10):
                    if valid(puzzle, i, j, val):
                        puzzle[i][j] = val
                        solved = backtrack(puzzle)
                        if solved != None: return solved
                        else: puzzle[i][j] = 0
                        
                return None

def solve(puzzle):
    solved = False
    puzzle_before_guess = []
    
    while not solved:
        prev_round = [[i for i in row] for row in puzzle]
        solved = True
        
        for row in range(len(puzzle)):
            for col in range(len(puzzle[row])):
                if puzzle[row][col] == 0:
                    solved = False
                    val = solve_square(puzzle, row, col)
                    puzzle[row][col] = val

        # shortcut
        if(puzzle[0][0] != 0 and puzzle[0][1] != 0 and puzzle[0][2] != 0):
            return

        # puzzle solution cannot be logically deduced, do brute force :(  
        if prev_round == puzzle and not solved:
            backtrack(puzzle)
            return

def euler96():
    puzzles = read_in_puzzles()
    assert(len(puzzles) == 50)
    acc = 0

    for puzzle in puzzles:
        solve(puzzle)
        acc += (100*puzzle[0][0] + 10*puzzle[0][1] + puzzle[0][2])

    return acc

if __name__ == "__main__":
    print(euler96())


