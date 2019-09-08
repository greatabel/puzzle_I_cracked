'''



#----------------------------#



'''

import time
from termcolor import colored


def main_process():
    q = '解释一下Python中的三元运算子'
    ans = 'python中没有其他语言中的三元表达式，不过有类似的实现方法:表达式1 if 条件 else 表达式2'
    x , y = 6, 8
    z = x if x > y else y
    print('z = x if x > y else y 于是：', z)
    print(colored(q, 'red'), ans)

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





