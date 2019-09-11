'''

问题描述：给定一组数字， 一组有9个数字，将这9个数字填写到3*3的九宫格内;
使得横，竖，斜对角一条线上的三个数字之和相等;如果无解则打印无解

#----------------------------#

分析：
先生成一组随机不等的9个数字（假设为整数吧）
    一组数字的和如果都不能3等分，肯定就不可能有解，直接返回
    如果可以三等分，至少有可能找到一个解：由于才3x3的数据量，可以以排列方式挑选：
    第1个位置 可以有9个选择
    第2个位置，减去上一个还有8个
    ……
    第8个位置，还有2个选择
    第9个没有选择

时间复杂度: 
    9*8*7*6*...*1= 9! = 362880
空间复杂度：
    由于我copy啦递减的列表，所以空间复杂度为9+8+7+...+1 = 55

'''
import random
# import itertools
import time
# from termcolor import colored

#预设这组数字在10以内，可以根据需要调大
limit = 10


def main_process():
    nums = random.sample(range(1, limit), 9)
    # nums = [1,2,3,4,5,6,7,8,9]
    count = 0
    thesum = sum(nums)/3
    print(nums, thesum)
    if not thesum.is_integer():
        print('无解')
        return
    else:
        thesum = int(thesum)

    # nums = [1,2,3,4,5,6,7,8,9]
    flag = False
    for A in nums:
        a = nums.copy()
        a.remove(A)
        for B in a:
            b = a.copy()
            b.remove(B)
            for C in b:
                c = b.copy()
                c.remove(C)
                for D in c:
                    d = c.copy()
                    d.remove(D)
                    for E in d:
                        e = d.copy()
                        e.remove(E)
                        for F in e:
                            f = e.copy()
                            f.remove(F)
                            for G in f:
                                g = f.copy()
                                g.remove(G)
                                for H in g:
                                    h = g.copy()
                                    h.remove(H)
                                    for I in h:
                                        if((A+B+C == D+E+F == G+H+I
                                                  == A+D+G == B+E+H
                                                  == C+F+I == A+E+I
                                                  == C+E+G == thesum)):
                                            print('''
                                           | {0} | {1} | {2} |\n
                                           | {3} | {4} | {5} |\n
                                           | {6} | {7} | {8} |\n
                                            '''.format(A, B, C, D, E,
                                                       F, G, H, I))
                                            flag = True
                                            return
    if flag == False:
        print('无解')


if __name__ == "__main__":
    tic = time.process_time()

    main_process()

    toc = time.process_time()
    print("time=", toc - tic)
