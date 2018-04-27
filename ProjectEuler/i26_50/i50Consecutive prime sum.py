# Consecutive prime sum
# Problem 50
# The prime 41, can be written as the sum of six consecutive primes:

# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.

# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

# Which prime, below one-million, can be written as the sum of the most consecutive primes?

import time
import math
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

def main_process():
    bound = 1000000
    primes = find_prime(bound)
    sumprime = 0
    print(primes)
    sums = []
    for i in range(0,len(primes)):
        start = primes[i]
        if i == 0:
            sums.append(primes[0])
        else:
            if (sums[i-1] + primes[i] ) < bound:
                sums.append( sums[i-1] + primes[i] )
            else:
                break
    print(sums)
    print('-'*20)
    jumps = 0
    mysum = 0
    for i in range(len(sums)):
        if isPrime(sums[i]):
            print(i+1,'#',sums[i]," is prime")
            if i+1 > jumps:
                jumps = i + 1
                mysum = sums[i]
        for j in range(len(sums)-1, i+jumps, -1):

            # print("i:",i,"j:",j,"jumps:",jumps,"sums[j]=",sums[j],"sums[i]=",sums[i])
            n = sums[j] - sums[i]
            sub = j - i
            if  sub > jumps and isPrime(n):
                print("jump",jumps,"## i:",i,"j:",j,"n:",n)
                jumps = j - i
                mysum = n
                # break
    print(mysum,'#',jumps)


    


    

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)