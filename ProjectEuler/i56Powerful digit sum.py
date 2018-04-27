# Powerful digit sum
# Problem 56
# A googol (10100) is a massive number: one followed by one-hundred zeros; 
# 100100 is almost unimaginably large: one followed by two-hundred zeros. 
# Despite their size, the sum of the digits in each number is only 1.

# Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?



import time
from termcolor import colored

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

def main_process(bounda,boundb):
    imax = 0
    for a in range(2,bounda):
        print('a=',a)
        tempa = a 
        for b in range(2,boundb):
            tempa *= a
            dsum = sum_digits(tempa)
            imax = max(imax, dsum)

    print(colored('mycount=', 'red'), imax)

if __name__ == "__main__":
    tic = time.clock()
    
    main_process(100,100)

    toc = time.clock()
    print("time=",toc - tic)