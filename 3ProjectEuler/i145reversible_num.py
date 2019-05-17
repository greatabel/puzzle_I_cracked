'''
How many reversible numbers are there below one-billion?

Some positive integers n have the property that the sum [ n + reverse(n) ] 

consists entirely of odd (decimal) digits. For instance, 

36 + 63 = 99 and 409 + 904 = 1313. We will call such numbers reversible; 

so 36, 63, 409, and 904 are reversible. Leading zeroes are not allowed in either n or reverse(n).

There are 120 reversible numbers below one-thousand.

How many reversible numbers are there below one-billion (109)?

#----------------------------#

有多少小于十亿的可逆数？

有些正整数n满足这样一种性质，将它的数字逆序排列后和本身相加所得到的和[ n + reverse(n) ]

的十进制表示只包含有奇数数字。例如，36 + 63 = 99 以及409 + 904 = 1313。

我们称这样的数是可逆的；因此36，63，409和904都是可逆的。无论是n还是reverse(n)都不允许出现前导0。

在小于一千的数中，一共有120个可逆数。

在小于十亿（109）的数中，一共有多少个可逆数？



'''



import time
from termcolor import colored


limit = 10 ** 3
limit = 10 ** 9
def main_process():
    numbers = []
    for i in range(12, limit):
        if i >= 10 **8 and i <= 10**9:
            continue

        if i % 10 ** 6 ==  0:
            print(i * 100 // limit)

        rev_i = str(i)[::-1]

        if rev_i[0] not in ['1', '3', '5', '7', '9'] and\
            rev_i[-1] not in ['1', '3', '5', '7', '9']:
            continue
        if rev_i[0] != '0':
            mysum = i + int(rev_i)
            flag = True
            for digit in str(mysum):
                if digit not in  ['1', '3', '5', '7', '9']:
                    flag = False
            if flag:
                # print(mysum)
                numbers.append(i)
    # print(numbers)
    print(colored('mycount=', 'red'), len(numbers))
    # mycount= 608720
    # time= 260.459537

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)



