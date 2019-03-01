'''
It is easily proved that no equilateral triangle exists with integral length sides and integral area. 
However, the almost equilateral triangle 5-5-6 has an area of 12 square units.

We shall define an almost equilateral triangle to be a triangle for which two sides are equal
 and the third differs by no more than one unit.

Find the sum of the perimeters of all almost equilateral triangles with integral side lengths 
and area and whose perimeters do not exceed one billion (1,000,000,000).
'''
        
import time
from termcolor import colored

# https://blog.dreamshire.com/project-euler-94-solution/
limit = 10 ** 9
def main_process():
    side0, side, s, p, m = 1, 1, 0, 0, 1

    L = 10**9
    while p < L:
        side0, side, m = side, 4*side - side0 + 2*m, -m
        s += p
        p = 3*side - m

    print("Sum of perimeters less than", L, " =", s)
    # print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)