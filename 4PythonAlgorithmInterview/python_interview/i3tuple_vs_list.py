'''

列表和元组之间的区别是？

#----------------------------#



'''

import time
from termcolor import colored


def main_process():
    q = '列表和元组之间的区别是？'
    ans = ['1. 二者的主要区别是列表是可变的，而元组是不可变的']
    ans.append('2. 元组通常由不同的数据，而列表是相同类型的数据队列。元组表示的是结构，而列表表示的是顺序')
    ans.append('3. 你不能将列表当作字典的key， 而元组可以')
    print(colored(q, 'red'), ans)

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





