'''



#----------------------------#



'''

import time
from termcolor import colored


def main_process():
    t = '''
    q: Python中的字典是什么？
    Python 中的字典是Python中一个键值映射的数据结构
    '''
    print(colored('mycount=', 'red'), t)


    dic = {'a':1, 'b':2}
    for k,v in dic.items():
        print(k, v)

    dic['a'] = 10
    for k,v in dic.items():
        print(k, v)

    arg = 1
    data = {
    0: "zero",
    1: "one",
    2: "two",
    }
    r = data.get(arg, "nothing")
    print(r)

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





