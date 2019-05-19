'''

147 Rectangles in cross-hatched grids

Problem 147
In a 3x2 cross-hatched grid, a total of 37 different rectangles could be situated within that grid as indicated in the sketch.


There are 5 grids smaller than 3x2, vertical and horizontal dimensions being important, i.e. 1x1, 2x1, 3x1, 1x2 and 2x2. If each of them is cross-hatched, the following number of different rectangles could be situated within those smaller grids:

1x1 1
2x1 4
3x1 8
1x2 4
2x2 18
Adding those to the 37 of the 3x2 grid, a total of 72 different rectangles could be situated within 3x2 and smaller grids.

How many different rectangles could be situated within 47x43 and smaller grids?

#----------------------------#



'''



import time
from termcolor import colored

# 不想解决这种类型题目，跳过，使用其他人方案：
def nrect(m, n):
    if m < n: m, n = n, m
    hvr = m*(m + 1) * n*(n + 1) // 4
    dr = n*((2*m - n) * (4*n*n - 1) - 3) // 6
    return hvr + dr


def main_process():
    w, h = 47, 43
    result = sum(nrect(m, n) for m in range(1, w+1) for n in range(1, h+1))
    print(colored('mycount=', 'red'), result)

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)
    # mycount= 846910284
