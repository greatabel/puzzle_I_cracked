'''



#----------------------------#

https://zhuanlan.zhihu.com/p/28738634

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

    print('推导式是个绝妙的东西，列表推导式一出，map、filter等函数黯然失色，\
        自 Python2.7以后的版本，此特性扩展到了字典和集合身上，构建字典对象无需调用 dict 方法')
    numbers = [1, 2, 3]
    d = {number: number * 10 for number in numbers}

    for k,v in d.items():
        print(k, v)

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





