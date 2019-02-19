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


def main_process():
    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)