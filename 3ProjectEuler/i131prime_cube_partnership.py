'''
There are some prime values, p, for which there exists a positive integer, n, 
such that the expression n3 + n2p is a perfect cube.

For example, when p = 19, 8^3 + 8^2×19 = 12^3.

What is perhaps most surprising is that for each prime with this property the value of n is unique, 
and there are only four such primes below one-hundred.

How many primes below one million have this remarkable property?

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