# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), 
# a 15K text file containing a triangle with one-hundred rows.

# NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, 
# as there are 299 altogether! If you could check one trillion (1012) 
# routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)


import time
from termcolor import colored

def file_handle(filename):
    rows = []
    FILE = open(filename,'r')
    for blob in FILE:
        rows.append([int(i) for i in blob.split(" ")])
    # print(rows[:10])
    return rows

def method1(origin_rows):
    import copy
    rows = copy.deepcopy(origin_rows)
    for i, j in [(i,j) for i in range(len(rows)-2,-1,-1) for j in range(i+1)]:
        rows[i][j] +=  max([rows[i+1][j],rows[i+1][j+1]])
    print(colored('method1 ='+str(rows[0][0]), 'red'), 'results')

def method2(rows):
    result = PathDynamic(rows)
    print(colored('method2 ='+ str(result), 'red'), 'results')

def PathDynamic(triangle):
  lastrow = len(triangle)-1
  if lastrow > 0:
    for i, val in enumerate(triangle[lastrow-1]):
      triangle[lastrow-1][i] = int(val) + max(int(triangle[lastrow][i]), int(triangle[lastrow][i+1]))
    triangle.pop()
    return PathDynamic(triangle)
  else:
    return triangle[0][0]

def main_process():
    origin_rows = file_handle('p067_triangle.txt')

    method1(origin_rows)

    method2(origin_rows)


if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)