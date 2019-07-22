'''

For any N, let f(N) be the last five digits before the trailing zeroes in N!.
For example,

9! = 362880 so f(9)=36288
10! = 3628800 so f(10)=36288
20! = 2432902008176640000 so f(20)=17664

Find f(1,000,000,000,000)

#----------------------------#

欧拉工程160 阶乘的尾数

对于任意N，记f(N)为N!除去末尾零后的最后五位数字。
例如，

9! = 362880，所以f(9)=36288
10! = 3628800，所以f(10)=36288
20! = 2432902008176640000，所以f(20)=17664

求f(1,000,000,000,000)

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





