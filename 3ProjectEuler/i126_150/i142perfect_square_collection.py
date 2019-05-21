'''

Problem 142
Perfect Square Collection

Find the smallest x + y + z with integers x > y > z > 0 

such that x + y, x - y, x + z, x - z, y + z, y - z are all perfect squares.

#----------------------------#

欧拉工程142: 完全平方数收集

找出最小的x + y + z的值，其中正整数x > y > z > 0

满足x + y, x - y, x + z, x - z, y + z, y - z 均为完全平方数。

'''






import time
from termcolor import colored


def main_process():
    bound_guess = 1000
    squares = set([n*n for n in range(1, bound_guess)])
    for a in range(1, bound_guess):
        a2 = a*a
        for b in range(1, a):
            b2 = b*b
            for c in range(1, b):
                c2 = c*c
                if b2 - c2 in squares and a2 - c2 in squares and a2 - b2 in squares:
                    if (a2 + b2 + c2) % 2 == 0 and a2 > b2 - c2 and b2 > a2 - c2 and c2 > a2 - b2:
                       print( (a2 + b2 + c2)/2)
                       # 1006193
        


if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)
