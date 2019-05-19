'''

Investigating a Prime Pattern

Problem 146
The smallest positive integer n for which the numbers 

n2+1, n2+3, n2+7, n2+9, n2+13, and n2+27 are consecutive primes is 10. 

The sum of all such integers n below one-million is 1242490.

What is the sum of all such integers n below 150 million?



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
