# Self powers
# Problem 48
# The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

# Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.

import time
from termcolor import colored


def main_process():
    isum = 0
    for i in range(1,1001):
        isum += i ** i 
    print(isum)
    print(colored('mycount=', 'red'), isum)

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)