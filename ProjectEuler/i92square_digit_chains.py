'''
A number chain is created by continuously adding the square of the digits 
in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in 
an endless loop. What is most amazing is that EVERY starting number 
will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?

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