# Distinct primes factors
# Problem 47
# The first two consecutive numbers to have two distinct prime factors are:

# 14 = 2 × 7
# 15 = 3 × 5

# The first three consecutive numbers to have three distinct prime factors are:

# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.

# Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?

import time
from termcolor import colored

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

def find_prime(bound):
    primeUnderSqrtN = []
    for i in range(2,round(math.sqrt(bound))+1):
        if isPrime(i):
            primeUnderSqrtN.append(i)
    # print("primeUnderSqrtN=",primeUnderSqrtN)
    mylist = list(range(1,bound))
    
    i = 0
    count = 0
    while i!= len(primeUnderSqrtN):
        for j in range(i+1,len(mylist)):
            if mylist[j] % primeUnderSqrtN[i] == 0:
                mylist[j] = 0
                count += 1
        mylist.sort()
        mylist = mylist[count:]
        count = 0
        i += 1
        # print("i=",i)
    mylist.remove(1)
    mylist.append(2)
    mylist.sort()
    return mylist

def find_prime_factors(num):
    results = []
    i = 2
    while i <= num:

        while num >= i:
            if num % i == 0 :
                results.append(i)
                num = round(num/i)
                # print("num= ",num, "i= ", i)
            else:
                break
        i = i+1
    print(num,'factors:',results)
    return results

def main_process():
    start = 2 * 3 * 5 * 7
    count = 1
    while count != 4:
        start += 1
        if len(set(find_prime_factors(start)) )== 4:
            count += 1
            print(start,'count=',count)
        else:
            count = 0

    print(colored('mycount=', 'red'), start - 3)

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)