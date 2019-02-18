'''By using each of the digits from the set, {1, 2, 3, 4}, 
exactly once, and making use of the four arithmetic operations (+, −, *, /) 
and brackets/parentheses, it is possible to form different positive integer targets.

For example,

8 = (4 * (1 + 3)) / 2
14 = 4 * (3 + 1 / 2)
19 = 4 * (2 + 3) − 1
36 = 3 * 4 * (2 + 1)

Note that concatenations of the digits, like 12 + 34, are not allowed.

Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one different 
target numbers of which 36 is the maximum, and each of the numbers 1 to 28 can 
be obtained before encountering the first non-expressible number.

Find the set of four distinct digits, a < b < c < d, for which the longest set of 
consecutive positive integers, 1 to n, can be obtained, giving your answer as a string: abcd.
'''

import time
from termcolor import colored
import itertools


def operate(a, b, operator):
    if operator == 0:
        return a + b
    elif operator == 1:
        return a -b 
    elif operator == 2:
        return a * b
    elif operator == 3:
        if b == 0:
            return None
        else:
            return a / b
    else:
        return None

def mytry(a, b, c, d):
    operators = {0, 1, 2, 3}
    for i in range(0, 4):
        for op in operators:
            result = operate(a, b, op)
            print(result)

    "Helloh"

def main_process():
    for op in itertools.product([0, 1, 2, 3], repeat=3):
        print(op)
    # count = 0
    # for terms in itertools.combinations(range(1, 10), 4):
    #     # count += 1
    #     print('terms=', terms)
    #     for n in itertools.permutations(terms):
    #         print(n)
    # print('count=', count)
    # mytry(1, 2, 3, 4)
    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)