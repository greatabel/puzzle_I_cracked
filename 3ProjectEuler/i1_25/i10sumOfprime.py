# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.
import math


def isPrime(num):
    # print('num=',num)
    flag = True
    for i in range(2, round(math.sqrt(num))+1):
        if num % i == 0:
            flag = False
    # print('flag=',flag)
    return flag

# 太慢了，200 0000 需要更有效率的实现
# def find_prime(bound):
#     primeUnderSqrtN = []
#     for i in range(2,round(math.sqrt(bound))+1):
#         if isPrime(i):
#             primeUnderSqrtN.append(i)
#     print("primeUnderSqrtN=",primeUnderSqrtN)
#     mylist = list(range(1,bound))
#     # print("mylist=",mylist)
#     for i in primeUnderSqrtN:
#         print("i in primeUnderSqrtN:",i)
#         # print("i=",i,"range(i*2,len(mylist),i)=",list(range(i*2,len(mylist),i)))
#         for j in range(i*2,len(mylist)+1,i):
#             # print("i=",i,"j=",j,"len(mylist)=",len(mylist))
#             if j in mylist:
#                 mylist[mylist.index(j)] = 0

#     print(mylist,"#",sum(mylist)-1)

def find_prime(bound):
    primeUnderSqrtN = []
    for i in range(2,round(math.sqrt(bound))+1):
        if isPrime(i):
            primeUnderSqrtN.append(i)
    print("primeUnderSqrtN=",primeUnderSqrtN)
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
        print("i=",i)
    print(mylist,"# sum=",sum(mylist)+2-1)


if __name__ == "__main__":
    # find_prime(10)
    find_prime(2000000)
