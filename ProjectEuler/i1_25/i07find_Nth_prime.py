# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

import math

def isPrime(num):
    # print('num=',num)
    flag = True
    for i in range(2, round(math.sqrt(num))+1):
        if num % i == 0:
            flag = False
    # print('flag=',flag)
    return flag

if __name__ == "__main__":
    results = []
    i = 1
    while len(results) < 10001:
        i += 1        
        if isPrime(i):
            results.append(i)
        print(len(results))
    print(results)