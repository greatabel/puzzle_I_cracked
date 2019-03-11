'''
Using a combination of grey square tiles and oblong tiles chosen from: 
red tiles (measuring two units), green tiles (measuring three units), 
and blue tiles (measuring four units), it is possible to tile a row measuring 
five units in length in exactly fifteen different ways.

png117.png
How many ways can a row measuring fifty units in length be tiled?
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