'''
Using a combination of grey square tiles and oblong tiles chosen from: 
red tiles (measuring two units), green tiles (measuring three units), 
and blue tiles (measuring four units), it is possible to tile a row measuring 
five units in length in exactly fifteen different ways.

png117.png
How many ways can a row measuring fifty units in length be tiled?
'''

import time
from termcolor import colored


len_count_dic = dict()
def f(x, y_min, y_max):

    #添加缓存逻辑
    if x in len_count_dic and len_count_dic[x]!= 0:
        return len_count_dic[x]

    ways_count = 1


    if x < y_min:
        return ways_count

    for blocklen in range(y_min, y_max+1):

        for start_index in range(0, x-blocklen+1):

            ways_count += f(x-start_index-blocklen, y_min, y_max)

    # 添加缓存
    len_count_dic[x] = ways_count
    return ways_count


def main_process():
    x = 50
    ymin = 2
    ymax = 4
    # 测试用小数据
    # x = 5
    mycount = f(x, ymin, ymax)
    print(colored('mycount=', 'red'), mycount)
    # mycount= 16475640049

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)