'''
Three distinct points are plotted at random on a Cartesian plane, for which -1000 ≤ x, y ≤ 1000, 
such that a triangle is formed.

Consider the following two triangles:

A(-340,495), B(-153,-910), C(835,-947)

X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC contains the origin, whereas triangle XYZ does not.

Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text file containing 
the co-ordinates of one thousand "random" triangles, find the number of triangles for which the interior 
contains the origin.

NOTE: The first two examples in the file represent the triangles in the example given above.
'''

import time
from termcolor import colored
import re 
import math
import numpy as np



def isContainmentTraingle(triangle):
    X1 = triangle[0] - triangle[2]
    Y1 = triangle[1] - triangle[3]
    X2 = triangle[4] - triangle[2]
    Y2 = triangle[5] - triangle[3]
    S = area(X1,Y1,X2,Y2)
    for i in range(0,4,2):
        for j in range(i+2,5,2):
            S -= area(triangle[i],triangle[i+1],triangle[j],triangle[j+1])
    return S == 0
    
def area(x1,y1,x2,y2):
    S = np.abs(x1*y2 - x2*y1)
    return S
    
def readData(filename):
    mat = list()
    file = open(filename)
    for line in file:
        row = line.split(',')
        row = [int(x) for x in row]
        mat.append(row)
    return mat 
        

def main_process():
    filename = 'i102triangles.txt'
    mat = readData(filename)
    mat = np.array(mat)
    count = 0
    for line in mat:
        if isContainmentTraingle(line):
            count+=1
    print(colored('mycount=', 'red'), count)

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)