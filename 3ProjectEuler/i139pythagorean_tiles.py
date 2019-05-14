'''
Let (a, b, c) represent the three sides of a right angle triangle with integral length sides. 

It is possible to place four such triangles together to form a square with length c.

For example, (3, 4, 5) triangles can be placed together to form a 5 by 5 square 

with a 1 by 1 hole in the middle and it can be seen that the 5 by 5 

square can be tiled with twenty-five 1 by 1 squares.


However, if (5, 12, 13) triangles were used then the hole would measure 7 by 7 

and these could not be used to tile the 13 by 13 square.

Given that the perimeter of the right triangle is less than one-hundred million,

how many Pythagorean triangles would allow such a tiling to take place?

#----------------------------#

欧拉工程139： 毕达哥拉斯地砖

用(a, b, c)表示边长为整数的直角三角形的三边，可以将四个这样的三角形放在一起，使其外框构成边长为c的正方形。

例如，边长为(3, 4, 5)的三角形可以构成一个5x5的正方形，中间留有一个1x1的洞。

而这个5x5的正方形又恰好可以用25个1x1的小正方形组成。


然而，如果我们用(5, 12, 13)的三角形，则中间的洞将会是7x7大小，不能用来组成13x13的大正方形。

考虑边长小于一亿的直角三角形，有多少个毕达哥拉斯三角形可以用中间留下的空洞大小的地砖恰好铺满外围的大正方形？

'''










import time
from termcolor import colored


def main_process():
    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)
