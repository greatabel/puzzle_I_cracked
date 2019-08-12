'''

Number Rotations

Problem 168
Consider the number 142857. We can right-rotate this number by moving the last digit (7) to the front of it, 

giving us 714285.
It can be verified that 714285=5×142857.
This demonstrates an unusual property of 142857: it is a divisor of its right-rotation.

Find the last 5 digits of the sum of all integers n, 10 < n < 10100, that have this property.

#----------------------------#

欧拉工程168 数字轮换

考虑数142857，我们可以将它的数字右移一位并把最后一个数字7放到最前面，得到714285。
可以验证714285=5×142857。
这表明了142857的一个特殊性质：它右移一位并把末位数字移至最前得到的数是它的倍数。

找出所有10 < n < 10100范围内满足这一性质的整数n，求它们的和的最后五位数字。

'''




import time
from termcolor import colored


def main_process():
    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





