'''

Problem 142
Perfect Square Collection

Find the smallest x + y + z with integers x > y > z > 0 

such that x + y, x - y, x + z, x - z, y + z, y - z are all perfect squares.

#----------------------------#



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
