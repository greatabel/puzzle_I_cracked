# Truncatable primes
# Problem 37
# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

import time
import math
# from i1_25 import i07find_Nth_prime

def isPrime(num):
    # print('num=',num)
    flag = True
    if num == 1:
        flag = False
    for i in range(2, round(math.sqrt(num))+1):
        if num % i == 0:
            # print(num ,'%',i )
            flag = False
    return flag

def isTruncatablePirme(prime):
    prime = str(prime)
    flag = False
    for i in range(1,len(prime)):
        # print('i=',i,prime[i:],'#',prime[:i])
        if isPrime(int(prime[i:])) and isPrime(int(prime[:i])):
            flag = True
        else:
            flag = False
            break
    return flag
    

if __name__ == "__main__":
    isum = 0 
    icount = 0
    tic = time.clock()
    for i in range(1,int(math.pow(10,6))):
        # print(i)
        if isPrime(i):
            if i > 10 and isTruncatablePirme(i):
                print(i)
                isum += i
                icount += 1
        if icount == 11:
            break
                    
    print('isum=',isum,icount)

    toc = time.clock()
    print("time=",toc - tic)