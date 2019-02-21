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

def sum_to(i1, i2, j, matrix):
    x1 = min(i1, i2)
    x2 = max(i1, i2)
    return sum([matrix[x][j] for x in range(x1, x2+1)])

# Returns the minimum path sum that goes from any entry in the                                                                                          
# leftmost column to entry (i, j).                                                                                                                      
def compute_min_path_entry(i, j, matrix, min_path):
    n = len(matrix)
    # Possible paths: take the minimum cost path to somewhere in the                                                                                    
    # (j-1)th column, go right, and then go up or down until reaching                                                                                   
    # (i, j).                                                                                                                                           
    possibilities = [min_path[x][j-1] + sum_to(x, i, j, matrix)
                     for x in range(n)]
    return min(possibilities)

def main_process():
    myfile = open('i82_matrix.txt').read()
    matrix = []
    for line in myfile.split('\n'):
        if line and line != '':
            row = [int(r) for r in line.split(',')]
            matrix.append(row)

    n = len(matrix) # assumes matrix is square                                                                                                              

    # Initialize min_path.                                                                                                                                  
    # min_path[x,y] will hold the minimal path sum starting at any entry in the                                                                             
    # leftmost column and ending at (x,y).                                                                                                                  
    min_path = [[-1 for y in row] for row in matrix]
    for i in range(n):
        min_path[i][0] = matrix[i][0]

    # When min_path has been filled up to the j'th column, we can fill in                                                                                   
    # the (j+1)st column.                                                                                                                                   
    for j in range(1, n):
        for i in range(n):
            min_path[i][j] = compute_min_path_entry(i, j, matrix, min_path)

    result = min([min_path[i][n-1] for i in range(n)])
    
    print(colored('mycount=', 'red'), result)

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)