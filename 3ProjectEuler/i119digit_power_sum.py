'''
The number 512 is interesting because it is equal to the sum of its digits 
raised to some power: 5 + 1 + 2 = 8, and 8^3 = 512. 

Another example of a number with this property is 614656 = 28^4.

We shall define an to be the nth term of this sequence and 

insist that a number must contain at least two digits to have a sum.

You are given that a2 = 512 and a10 = 614656.

Find a30.
'''

'''
欧拉工程119
我先试验了正常思路：遍历方法，到12个数开始就非常的慢，所以放弃。

可以考虑到我们要找的30数 肯定是非常大的数，所以我们不能遍历数，而应该考虑遍历次方。

'''

import math
import time
from termcolor import colored


def digit_sum(n):
    num_str = str(n)
    isum = 0
    for i in range(0, len(num_str)):
        isum += int(num_str[i])
    return isum


# def interesting(n):
#     x = digit_sum(n)
#     if x < 2:
#         return False
#     y = math.log(n, x)
#     decimal_y = y % 1
#     # python log bug
#     # print(' ', n, 'decimal_y=', decimal_y)
#     if decimal_y < 0.0000001 or decimal_y > 0.9999999:
#         return True
    

def main_process():

    # mycount = 0
    # i = 50
    # while mycount < 30:
    #     i += 1
    #     if interesting(i):
    #         mycount += 1
    #         print('mycount:',mycount, i)



    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)