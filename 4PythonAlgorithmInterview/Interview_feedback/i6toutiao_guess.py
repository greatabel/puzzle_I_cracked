'''

2sum 问题：

给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]



#----------------------------#

hash方法：https://coderbyte.com/algorithm/two-sum-problem

'''

import time
from termcolor import colored


def naive_solve_2sum(nums, target):
    i = 0
    j = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            # print(i, j, 'value=', nums[i], nums[j])
            if nums[i] + nums[j] == target:
                print(i, j)

def hash_2sum(nums, target):
    ht = {}
    i = 0
    for i in range(len(nums)):
        remain = target - nums[i]
        if remain not in ht:
            ht[nums[i]] = i
        else:
            print(i, ht[remain])


def main_process():
    nums = [2, 7, 11, 15]
    target = 9
    naive_solve_2sum(nums, target)
    hash_2sum(nums, target)
    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





