'''

数字1～1000放在含有1001的数组中，其中唯一一个元素重复，其他数字都出现1次
设计一个算法，将重复元素找出来，要求每个数组元素只能访问一次。
如果不使用辅助存储空间，能否设计一个算法实现？

#----------------------------#

（1+1000）*1000/2 = 1001*500= 500500
然后把从第一个开始所有元素相加，然后减去500500 就知道了

'''

import time
from termcolor import colored


def findDuplicate(array):
    dic = dict()
    for i in array:
        if i not in dic.keys():
            dic[i] = i
        else:
            print(i)
        

def main_process():
    array= [1, 3, 4, 2, 5, 3, 6]
    findDuplicate(array)
    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





