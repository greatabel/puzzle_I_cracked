# Prime digit replacements
# Problem 51
# By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

# By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

# Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.


import time
import math
from termcolor import colored

def get_digital(number):
    results = []
    if number == 0:
        results = [0]
    while number > 0:
        result = number % 10
        number = number // 10
        results.append(result)
    # print('results=', results)
    return results

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

def replace(s1, n):
    """Replace repeating digits"""
    L1 = []
    for i in range(1, 10):
        y = str(i)
        x = s1.replace(n, y)
        L1.append(x)
    return L1

def allPrime(x,count):
    L2 = []
    for number in x:
        if isPrime(int(number)):
            L2.append(int(number))
        else:
            continue
    if len(L2) == count:
        print("result = ", L2)
        return True

def step(s, key):
    for digit in s:
        if digit == key:
            x = replace(s, key)
            if allPrime(x,8):
                return True

def find_group(prime):
    s = ''
    s1 = str(prime)
    s = s1[0:-1]
    # print("s=",s,"s1=",s1)
    d = {}
    for i in s:
        d[i] = s.count(i)
    # print("d=",d)
    for k,v in d.items():
        # print("k,v ",k,v)
        if step(s1, k):
            return True
            break
        else:
            continue



def main_process():
    primes = find_prime(1000000)
    print("finished primes")
    for p in primes:
        # print('p=',p, get_digital(p))
        if find_group(p):
            print('end')
            break
        else:
            continue

    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)