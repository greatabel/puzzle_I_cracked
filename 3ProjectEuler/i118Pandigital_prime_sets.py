'''
Using all of the digits 1 through 9 and concatenating them freely to form decimal integers, 
different sets can be formed. Interestingly with the set {2,5,47,89,631}, 
all of the elements belonging to it are prime.

How many distinct sets containing each of the digits one through nine exactly once contain only prime elements?

翻译：
用1～9个连续数字自由连接组成数字，
可以组成不同的集合。
有趣的是像 {2,5,47,89,631} 这样的集合，每一个元素都是质数

有多少个这样刚好9个数字 组成的元素集合中每一个都是质数？
'''

import time
from termcolor import colored


def main_process():
    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)