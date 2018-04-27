# Pandigital products
# Problem 32
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

import time
import math

def isPandigital(string):
    thelen = len(string)
    # print(string,'thelen=', thelen)
    for i in range(1, thelen+1):
        # print('str(i)=', str(i))
        if str(i) not in string:
            return False
    if thelen > 9:
        return False
    return True

# 数A*数B=数C,共计9位， 
# 只可能是 1位*4位=4位， 2位*3位=4位 
def find_allmatches(numbers):
    results = []

    for i in range(1, 10):
        for j in range(int(math.pow(10, 3)) , int(math.pow(10,4))):
            combine = str(i) + str(j) + str(i * j)
            if isPandigital(combine):
                
                if i * j not in results:
                    results.append(i * j)
                    print(str(i) , str(j) ,str(i * j))

    for i in range(10, 100):
        for j in range(100,1000):
            combine = str(i) + str(j) + str(i * j)
            if isPandigital(combine):
                
                if i * j not in results:
                    results.append(i * j)
                    print(str(i) , str(j) ,str(i * j))
    return sum(results)



if __name__ == "__main__":
    tic = time.clock()
    # for i in range(0,20):
    #     print(i,fib(i),len(str(fib(i))))
    # find_allpowers(5,5)
    # find_allpowers(10000,4)
    results = find_allmatches(list(range(1,10)))
    print('#', results)

    toc = time.clock()
    print("time=",toc - tic)