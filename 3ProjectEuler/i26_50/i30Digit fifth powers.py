# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

# 1634 = 14 + 64 + 34 + 44
# 8208 = 84 + 24 + 04 + 84
# 9474 = 94 + 44 + 74 + 44
# As 1 = 14 is not a sum it is not included.

# The sum of these numbers is 1634 + 8208 + 9474 = 19316.

# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

import time
import math

# 9   999,999,999 531,441 they need to have the same # of digits
# 8   99,999,999  472,392 nope, still too many
# 7   9,999,999   413,343 not quite there
# 6   999,999 354,294 a valid search limit

def circulate_digit_sum(n,pw):

    # print('n=',n)
    dsum = 0
    while n  > 0:
        reminder = n % 10
        n //= 10
        # print(reminder,n)
        dsum += powers[reminder]
    # print(dsum)
    return dsum

powers = {}

def find_allpowers(presume,pw):
    global powers
    for a in range(10):
         powers[a] = a ** pw
    print('powers=',powers)

    mysum = 0
    for i in range(2, presume):
        if i == circulate_digit_sum(i,pw):
            print(i)
            mysum += i
    print('mysum=',mysum)


    

if __name__ == "__main__":
    tic = time.clock()
    # for i in range(0,20):
    #     print(i,fib(i),len(str(fib(i))))
    # find_allpowers(5,5)
    # find_allpowers(10000,4)
    find_allpowers(1000000,5)

    toc = time.clock()
    print("time=",toc - tic)