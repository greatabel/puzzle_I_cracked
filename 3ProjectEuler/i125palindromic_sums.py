'''
The palindromic number 595 is interesting because it can be written as the 
sum of consecutive squares: 6^2 + 7^2 + 8^2 + 9^2 + 10^2 + 11^2 + 12^2.
There are exactly eleven palindromes below one-thousand that can be written 
as consecutive square sums, and the sum of these palindromes is 4164. 
Note that 1 = 0^2 + 1^2 has not been included as this problem is 
concerned with the squares of positive integers.
Find the sum of all the numbers less than 10^8 that are both palindromic and 
can be written as the sum of consecutive squares.

#----------------------------#
翻译：回文和

回文数595很有趣，因为它可以写成连续平方数的和：
6^2 + 7^2 + 8^2 + 9^2 + 10^2 + 11^2 + 12^2
恰好有十一个小于一千的回文数可以写成连续平方数的和，这些回文数的和是4164。
注意 1 = 0^2 + 1^2并没有算在内，因为本题只考虑正整数的平方。

在小于10^8的数中，找出所有可以写成连续平方数的和的回文数，并求它们的和。

#----------------------------#


'''











import time
from termcolor import colored


# copy from i04
def palindromic(num):
    # print('num=', num)
    results = []
    while num > 0:
        results.append(num%10)
        num = round((num-num%10 )/10)
    # print("results=", results)
    flag = (results == list(reversed(results)))
    if flag:
        print("flag:",list(reversed(results)))

    return flag


def main_process():
    for i in range(100, 135):
        palindromic(i)
    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)


