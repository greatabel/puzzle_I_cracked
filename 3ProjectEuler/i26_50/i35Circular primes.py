# Circular primes
# Problem 35
# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

# How many circular primes are there below one million?

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

# def get_digital(number):
#     results = []
#     if number == 0:
#         results = [0]
#     while number > 0:
#         result = number % 10
#         number = number // 10
#         results.append(result)
#     # print('results=', results)
#     return results

# copy from i10
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

# def permutList(l):
#     if not l:
#             return [[]]
#     res = []
#     for e in l:
#             temp = l[:]
#             temp.remove(e)
#             res.extend([[e] + r for r in permutList(temp)])
#     return res
from itertools import permutations



def isCircular(prime):
    prime = str(prime)
    flag = False
    for i in range(len(prime)):
        if isPrime(int(prime[i:]+prime[:i])):
            flag = True
        else:
            flag = False
            break
    return flag

def get_permutation_numbers(l):
    results = []
    for digitals in l:
        num = 0
        place = 0
        for digit in reversed(digitals):
            num += digit * (10** place)
            place += 1
        if num not in results:
            results.append(num)
    # print('all:',results)
    return results

def find_circular_below(bound):
    primes = find_prime(bound)
    # primesI = copy.deepcopy(primes)
    print('primes len=', len(primes))
    circulars = []
    prime_i = 0
    for p in primes[:]:
        prime_i += 1
        # digitals = get_digital(p)
        # print('digitals=', digitals)        
        # numbers = get_permutation_numbers(permutList(digitals))
        # print("p=",p,"numbers=",numbers)
        # flag = True
        # for num in numbers:
        #     if num not in primes:
        #         flag = False                
        #         break
        # if flag:
        #     circulars.append(p)        
        #     print('len(circulars)=',len(circulars))
        if isCircular(p):
            circulars.append(p)
            print('len(circulars)=',len(circulars))
            
        if prime_i % 1000 == 0:
            print('prime_i = ' , prime_i,len(primes))

    print("circulars=", circulars, len(circulars))



if __name__ == "__main__":
    tic = time.clock()
    # isCircular(971)
    # limit = find_circular_below(1000)
    limit = find_circular_below(10**6)

    toc = time.clock()
    print("time=",toc - tic)