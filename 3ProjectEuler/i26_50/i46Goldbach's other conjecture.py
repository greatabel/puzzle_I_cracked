# Goldbach's other conjecture
# Problem 46
# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

# 9 = 7 + 2×12
# 15 = 7 + 2×22
# 21 = 3 + 2×32
# 25 = 7 + 2×32
# 27 = 19 + 2×22
# 33 = 31 + 2×12

# It turns out that the conjecture was false.

# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?


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



def checkconjecture(n,primes):
    flag = False
    for p in primes:
        if n > p:
            r = math.sqrt( (n - p) / 2 )
            if int(r) == r:
                print(n,"=",p,"+2* ",r,"^2")
                flag = True
    return flag
        


def main_process():
    bound = 10000
    primes = find_prime(bound)
    for i in range(1,bound):
        if i % 2 == 1 and i > 1 and i not in primes:
            if not checkconjecture(i,primes):
                print(i,checkconjecture(i,primes))
                break

    print(colored('mycount=', 'red'), 'results')



if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)