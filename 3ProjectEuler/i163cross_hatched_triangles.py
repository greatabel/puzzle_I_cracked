'''

Problem 163  Cross-hatched triangles


Consider an equilateral triangle in which straight lines are drawn from each vertex to the middle of the opposite side, such as in the size 1 triangle in the sketch below.


Sixteen triangles of either different shape or size or orientation or location can now be observed in that triangle. Using size 1 triangles as building blocks, larger triangles can be formed, such as the size 2 triangle in the above sketch. One-hundred and four triangles of either different shape or size or orientation or location can now be observed in that size 2 triangle.

It can be observed that the size 2 triangle contains 4 size 1 triangle building blocks. A size 3 triangle would contain 9 size 1 triangle building blocks and a size n triangle would thus contain n2 size 1 triangle building blocks.

If we denote T(n) as the number of triangles present in a triangle of size n, then

T(1) = 16
T(2) = 104

Find T(36).

#----------------------------#

163 纵横交错的三角形

考虑一个等边三角形，从三角形的每个顶点向对边的中点引一条线段，构成如下图所示的1级三角形。


我们可以从这个三角形中数出16个不同形状、不同大小、不同方向、不同位置的三角形。使用1级三角形作为材料，

我们可以构成更大的三角形，比如右边的2级三角形。在2级三角形中可以输出一百零四个不同形状、不同大小、不同方向、不同位置的三角形。

可以看出一个2级三角形包含有4个1级三角形。一个3级三角形包含有9个1级三角形，而一个n级三角形包含有n2个1级三角形。

如果我们用T(n)表示n级三角形中能够数出的三角形个数，那么

T(1) = 16
T(2) = 104

求T(36)

'''




import time
from termcolor import colored

def T(n):
   return (1678*n**3 + 3117*n**2 + 88*n - n%2*345 - n%3*320 - n%4*90 - 
          (n**3 - n**2 + n)%5 * 288) // 240 


def main_process():

    print(colored('mycount=', 'red'), T(1), T(2),'#', T(36))
    # mycount= 16 104 # 343047

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





