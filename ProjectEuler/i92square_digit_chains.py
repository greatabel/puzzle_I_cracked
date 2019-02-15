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

def get_digits(n):
    b = str(n)
    c = []
    for digit in b:
        c.append(int(digit))
    return c

def get_digits_sum(start):
    digits = get_digits(start)
    isum = 0
    for digit in digits:
        isum += digit ** 2
    return isum


def main_process():
    start = 44
    mylist = []    
    mysum = get_digits_sum(44)
    print('#', mysum)
    while (mysum not in mylist):
        mylist.append(mysum)
        print(mysum)
        mysum = get_digits_sum(mysum)
    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)