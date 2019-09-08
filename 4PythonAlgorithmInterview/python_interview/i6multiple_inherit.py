'''



#----------------------------#



'''

import time
from termcolor import colored


class Color:
    pass

class Fruit:
    pass

class Orange(Color, Fruit):
    pass

def main_process():
    r = issubclass(Orange, Color) and issubclass(Orange, Fruit)
    print(colored('--------------------', 'green'), r)

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





