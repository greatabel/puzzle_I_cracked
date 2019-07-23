'''

A triomino is a shape consisting of three squares joined via the edges. There are two basic forms:



If all possible orientations are taken into account there are six:



Any n by m grid for which nxm is divisible by 3 can be tiled with triominoes.
If we consider tilings that can be obtained by reflection or rotation from another tiling as different there are 41 ways a 2 by 9 grid can be tiled with triominoes:



In how many ways can a 9 by 12 grid be tiled in this way by triominoes?

#----------------------------#

欧拉工程161: 三联骨牌

三联骨牌是由三个正方形方块拼接而成的骨牌，它一共有两种基本形状：


如果计入旋转，则一共有六种可能的形状：


任何n乘m的方阵，只要nxm能够被3整除，就能用三联骨牌拼出来。
如果我们认为翻转或旋转是不同的拼法，那一个2乘9的方阵有一共有41种拼法：


一个9乘12的方阵有多少种拼法？

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





