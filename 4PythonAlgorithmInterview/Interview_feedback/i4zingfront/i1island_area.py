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


def transfer_to_status(original_matrix):
    row_len = len(original_matrix)
    col_len = len(original_matrix[0])
    print(row_len, col_len)


def main_process():
    transfer_to_status(island_matrix)
    print('results')


if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",  toc - tic)
