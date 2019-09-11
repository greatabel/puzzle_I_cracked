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

# 测试第二个岛的情况
# island_matrix = [  [1, 1, 1, 1, 1, 1],
#             [1, 1, 0, 0, 0, 1],
#             [1, 0, 0, 0, 1, 0],
#             [1, 1, 0, 1, 1, 1],
#             [0, 1, 0, 1, 0, 1],
#             [1, 1, 1, 1, 1, 1]
#          ]

row_len = len(island_matrix)
col_len = len(island_matrix[0])

#标示经过计算满足条件的岛屿0
flag_value = -1
processed_value = 2

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
               source_mx[i][j] = flag_value

# 因为需要找出所有的满足条件的岛，然后根据岛size排序，找出第2个
# 所以需要遍历 状态矩阵的每个元素，统计改元素所在的岛的大小，如果
# 已经统计了该岛的面积，我们就从状态矩阵中踢出
def get_unique_island_size(status_mx, i, j):
    if 0 <= i < row_len and 0 <= j < col_len \
        and status_mx[i][j] == flag_value:
        status_mx[i][j] = processed_value
        return 1 + get_unique_island_size(status_mx, i+1, j) + \
                   get_unique_island_size(status_mx, i-1, j) + \
                   get_unique_island_size(status_mx, i, j+1) + \
                   get_unique_island_size(status_mx, i, j-1)
    # 非环绕岛屿节点为0
    return 0

# 从满足条件的岛元素上遍历，找出一个岛，然后从状态矩阵中去除掉整个岛
# 遍历需要计算的周边岛元素越来越少，防止堆栈溢出
# 求得的面积列表，进行大小逆序排列
def get_island_sizes(status_mx):
    island_sizes = []
    for i in range(1, row_len):
        for j in range(1, col_len):
            if status_mx[i][j] == flag_value:
                island_size = get_unique_island_size(status_mx, i, j)
                island_sizes.append(island_size)
    # 倒序排列所有的岛面积
    island_sizes.sort(reverse=True)
    return island_sizes


def main_process():
    # print(island_matrix, '\n')
    transfer_to_status(island_matrix)
    # print(island_matrix)
    size_list = get_island_sizes(island_matrix)

    print('面积列表', size_list)
    if len(size_list) == 1:
        print('最大岛面积：', size_list[0])
    else:
        print('第2大岛面积：', size_list[1])

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",  toc - tic)
