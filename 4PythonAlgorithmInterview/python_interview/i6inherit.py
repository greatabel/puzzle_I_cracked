'''



#----------------------------#



'''

import time
from termcolor import colored


x = 0
class fruit:
    def __init__(self):
        global x
        x += 1
        print("I'm a fruit")

class citrus(fruit):
    def __init__(self):
        super().__init__()
        global x
        x += 10
        print('I am citrus')

def main_process():
    t = '解释一下Python中的继承?\
        承能让我们重新使用代码，也能更容易的创建和维护应用。Python支持如下种类的继承：\
        \n单继承：一个类继承自单个基类\
        \n多继承：一个类继承自多个基类\
        \n多级继承：一个类继承自单个基类，后者则继承自另一个基类\
        \n分层继承：多个类继承自单个基类\
        \n混合继承：两种或多种类型继承的混合'
    print(colored('mycount=', 'red'), t)
    lime = citrus()
    print('x=', x)

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





