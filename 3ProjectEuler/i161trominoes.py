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


#----------------------------#
skip this problem , use Meng-Gen's solution
'''



import time
from termcolor import colored


class Grid():
    def __init__(self):
        self.n = None
        self.triomino_list = [
            [(0, 0), (1, 0), (0, 1)],
            [(0, 0), (1, 0), (1, 1)],
            [(0, 0), (0, 1), (1, 1)],
            [(0, 0), (1, 0), (1, -1)],
            [(0, 0), (0, 1), (0, 2)],
            [(0, 0), (1, 0), (2, 0)],
        ]

    def get(self, n):
        self.n = n
        start_grid = tuple(tuple(False for j in range(9)) for i in range(self.n))
        end_grid = tuple(tuple(True for j in range(9)) for i in range(self.n))
        counting = [{} for i in range(3 * self.n + 1)]
        counting[0][start_grid] = 1
        for i in range(3 * self.n):
            for top in counting[i]:
                empty_cell = self.__get_first_empty_cell(top)
                for triomino in self.triomino_list:
                    next_grid = self.__place_triomino(top, triomino, empty_cell)
                    if not next_grid:
                        continue
                    if next_grid not in counting[i + 1]:
                        counting[i + 1][next_grid] = 0
                    counting[i + 1][next_grid] += counting[i][top]
        return counting[3 * self.n][end_grid]

    def __get_first_empty_cell(self, grid):
        for i in range(self.n):
            for j in range(9):
                if not grid[i][j]:
                    return (i, j)
        return None

    def __place_triomino(self, grid, triomino, empty_cell):
        empty_cell_x, empty_cell_y = empty_cell
        for triomino_x, triomino_y in triomino:
            x = empty_cell_x + triomino_x
            y = empty_cell_y + triomino_y
            if x < 0 or x >= self.n or y < 0 or y >= 9:
                return None
            if grid[x][y]:
                return None
        result = [[False for j in range(9)] for i in range(self.n)]
        for i in range(self.n):
            for j in range(9):
                result[i][j] = grid[i][j]
        for triomino_x, triomino_y in triomino:
            x = empty_cell_x + triomino_x
            y = empty_cell_y + triomino_y
            result[x][y] = True
        return self.__list_to_tuple(result)

    def __dump_grid(self, grid):
        if not grid:
            return
        print('+' + '-' * 9 + '+')
        for i in range(self.n):
            print('|' + ''.join(['*' if grid[i][j] else '.' for j in range(9)]) + '|')
        print('+' + '-' * 9 + '+')

    def __list_to_tuple(self, grid):
        return tuple(tuple(row) for row in grid)

    def __tuple_to_list(self, grid):
        return [list(row) for row in grid]


def main_process():
    for n in [2, 12]:
        print(n, '=>', Grid().get(n))
    print(colored('mycount=', 'red'), 'results')
    # 20574308184277971

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





