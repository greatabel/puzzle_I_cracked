'''
A number consisting entirely of ones is called a repunit. 

We shall define R(k) to be a repunit of length k; 

for example, R(6) = 111111.

Let us consider repunits of the form R(10n).

Although R(10), R(100), or R(1000) are not divisible by 17, 
R(10000) is divisible by 17. Yet there is no value of n for which R(10n) will divide by 19. 
In fact, it is remarkable that 11, 17, 41, and 73 are the only four primes below one-hundred 
that can be a factor of R(10n).

Find the sum of all the primes below one-hundred thousand that will never be a factor of R(10n).


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