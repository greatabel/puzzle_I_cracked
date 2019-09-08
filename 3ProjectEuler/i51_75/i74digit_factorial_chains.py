'''
The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169;
 it turns out that there are only three such loops that exist:

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, 
but the longest non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
'''
import time
from termcolor import colored
import math


def sum_factorial_digits(n):
    digits = []
    while n > 0:
        s = n % 10
        digits.append(s)
        n = n // 10

    mysum = 0
    for digit in digits:
        mysum += math.factorial(digit)
    # print('n=', n, ' sum=', mysum)
    return mysum

def main_process():
    # for i in (145, 169, 871, 872):
    #     sum_factorial_digits(i)
    limit = 10 ** 6
    count = 0
    for i in range(1, limit+1):
        seq = []
        while (i not in seq):
            seq.append(i)
            i = sum_factorial_digits(i)
        if len(seq) == 60:
            count += 1
            print('count=', count)

    print(colored('mycount=', 'red'), count)

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)