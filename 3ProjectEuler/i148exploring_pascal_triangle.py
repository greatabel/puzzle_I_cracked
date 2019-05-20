'''

148 Exploring Pascal's triangle

We can easily verify that none of the entries in the first seven rows of Pascal's triangle are divisible by 7:

                         1
                     1       1
                 1       2       1
             1       3       3       1
         1       4       6       4       1
     1       5      10      10       5       1
1        6      15      20      15       6       1
However, if we check the first one hundred rows, we will find that only 2361 of the 5050

 entries are not divisible by 7.

Find the number of entries which are not divisible by 7 in the first one billion (109) rows of Pascal's triangle.

#----------------------------#
欧拉工程148： 探索帕斯卡三角

可以验证，帕斯卡三角的前7行是，没有一个整数能够被7整除：

                                    

                         1
                     1       1
                 1       2       1
             1       3       3       1
         1       4       6       4       1
     1       5      10      10       5       1
1        6      15      20      15       6       1

然而，如果我们检查前一百行就会发现，在这5050个数上，

只有2361个不能被7整除。

找出帕斯卡三角前十亿（10^9）行中不能被7整除的数的数目。

#----------------------------#
思路分析：暴力破解肯定是没戏

带7   的总数是28
带7^2 的总数是28^2

'''




import time
from termcolor import colored


def row(row_num):
    if row_num < 7:
        return int(row_num+1)
    else:
        r =  (int(row_num % 7) + 1) * row(row_num/7)
        return r

limit = 10 ** 9
# limit = 10 ** 2
def main_process():
    results = 0
    for i in range(0, limit):
        if i % 10**6 == 0:
            print(i * 100 / limit, ' percentage')
        results += row(i)
    print(colored('mycount=', 'red'), results)

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)




