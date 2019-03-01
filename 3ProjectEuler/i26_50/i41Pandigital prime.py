# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
 # For example, 2143 is a 4-digit pandigital and is also prime.

# What is the largest n-digit pandigital prime that exists?

import time
import math

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

# 9+8+7+6+5+4+3+2+1+0 = 45 ,divide by 3
# 9+8+7+6+5+4+3+2+1 = 45, so
#   1+2+3+4+5+6+7+8 = 36    ,so     
def  find(bound):
    primes = find_prime(bound)
    print('primes len=', len(primes))
    for p in reversed(primes):
        p = str(p)
        
        if isPandigital(p):
            print(p,len(p))

    # primesI = copy.deepcopy(primes)


if __name__ == "__main__":
    tic = time.clock()
    find(10**7)

    toc = time.clock()
    print("time=",toc - tic)