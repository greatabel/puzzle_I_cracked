'''



#----------------------------#



'''

import time
from termcolor import colored


def main_process():
    t = '''
    q:  Python中的标识符长度能有多长？

    在Python中，标识符可以是任意长度。此外，我们在命名标识符时还必须遵守以下规则：

    只能以下划线或者 A-Z/a-z 中的字母开头

    其余部分可以使用 A-Z/a-z/0-9

    区分大小写


    '''
    print(colored('mycount=', 'red'), t)

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





