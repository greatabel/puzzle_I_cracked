'''

问题描述：给定形如下 的矩阵， 
    1 1 1 1 1 1 
     1 1 0 0 0 1 
     1 0 0 0 1 0 
     1 1 0 1 1 1 
     0 1 0 1 0 0 
     1 1 1 1 1 1 
上面矩阵的中的1代表海岸线，0代表小岛。

求第二岛的面积(即被1中包围的0的个数，如果只有一个小岛，输出最大岛的面积)。 

#----------------------------#

分析：

'''

import time

island_matrix = [  [1, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 0],
            [1, 1, 0, 1, 1, 1],
            [0, 1, 0, 1, 0, 0],
            [1, 1, 1, 1, 1, 1]
         ]

row_len = len(island_matrix)
col_len = len(island_matrix[0])

def transfer_to_status(source_mx):
    # 第i = 0位置不需要考虑，肯定不符合要求，左边肯定不是0
    # 最i = len 位置也不需要，右边肯定不符合要求
    for i in range(1, row_len):
        for j in range(1, col_len):
           if source_mx[i][j] == 0:
            lefts = [source_mx[i][x] for x in range(j)]
            rights = [source_mx[i][x] for x in range(j+1, col_len)]
            tops = [source_mx[x][j] for x in range(i)]
            bottoms = [source_mx[x][j] for x in range(i+1, row_len)]
            if 1 in lefts and \
               1 in rights and \
               1 in tops and \
               1 in bottoms:
               source_mx[i][j] = -1

    
def main_process():
    print(island_matrix, '\n')
    transfer_to_status(island_matrix)
    print(island_matrix)


if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",  toc - tic)
