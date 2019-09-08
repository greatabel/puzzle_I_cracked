'''

给定数组a1,a2,...,an,找出最大值，最小值。假设数组中的值两两个不相同

#----------------------------#



'''

import time
from termcolor import colored


# python 自带的方式
def find_max_min(arr):
    return max(arr), min(arr)

def find_max_min_by_divide(arr):
    if arr == None:
        return 
    i = 0
    lens = len(arr)
    #2-2分组，小的放在左半部分
    while i < lens-1:
        if arr[i] > arr[i+1]:
            tmp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = tmp
        i += 2
        imax = arr[0]
    imin = arr[0]
    
    i = 2
    while i < lens:
        if arr[i] < imin:
            imin = arr[i]
        i += 2

    imax = arr[1]
    i = 3
    while i < lens:
        if arr[i] > imax:
            imax = arr[i]
        i += 2

    if lens % 2 == 1:
        if imax < arr[lens -1]:
            imax = arr[lens-1]
        if imin > arr[lens-1]:
            imin = arr[lens-1]
    return imax, imin

def main_process():
    array =[7,3,19,40,4,7,1]
    # imax, imin = find_max_min(array)
    imax, imin = find_max_min_by_divide(array)
    print(colored('mycount=', 'red'),imax, imin)

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





