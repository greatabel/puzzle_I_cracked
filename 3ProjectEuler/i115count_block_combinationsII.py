'''
NOTE: This is a more difficult version of Problem 114.

A row measuring n units in length has red blocks with a minimum length of m units placed on it,
 such that any two red blocks (which are allowed to be different lengths) 
 are separated by at least one black square.

Let the fill-count function, F(m, n), represent the number of ways that a row can be filled.

For example, F(3, 29) = 673135 and F(3, 30) = 1089155.

That is, for m = 3, it can be seen that n = 30 is the smallest value for which the 
fill-count function first exceeds one million.

In the same way, for m = 10, it can be verified that F(10, 56) = 880711 and F(10, 57) = 1148904, 
so n = 57 is the least value for which the fill-count function first exceeds one million.

For m = 50, find the least value of n for which the fill-count function first exceeds one million.
'''

'''
基本上 我们可以照搬 i114的解法
'''
import time
from termcolor import colored


len_count_dic = dict()
def f(x, y):

    #添加缓存逻辑
    if x in len_count_dic and len_count_dic[x]!= 0:
        return len_count_dic[x]


    # 一行有x个单元， 我们用y个连续红色单元填充到里面， x >= y
    # 第一种就是没有用红色划分，全黑的情况
    ways_count = 1

    # 当红色单元以及超过需要填充的行单元数，应该终止程序
    if x < y:
        return ways_count

    for start_index in range(0, x-y+1):
        # print(colored("开始的index=", "red"), start_index)
        for red_len in range(y, x-start_index+1):
            # print(' 红单元长度=', red_len, '总长度=', x)
            # print('#' * start_index, colored('#', 'red') * red_len, '#' * (x - start_index - red_len))

            # ways_count += 1 这种粗暴的方法miss了情况：就是其中不止一个连续红色单元的情况
            # print(' x-start_index-red_len=', x-start_index-red_len)
            ways_count += f(x-start_index-red_len-1, y)

    # 添加缓存
    len_count_dic[x] = ways_count
    return ways_count


def main_process():
    limit = 10 ** 6
    y = 50
    # 测试用小数据
    # x = 7
    # 直接先不停测试上限，先试验了100不行，再200就可以了
    for x in range(50, 200):
        mycount = f(x, y)
        if mycount >= limit:
            print(colored('mycount=', 'red'), mycount, 'x=', x)
            break
    # mycount= 1053389 x= 168

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)