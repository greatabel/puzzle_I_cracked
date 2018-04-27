# Prime pair sets
# Problem 60
# The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime.
# For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, 
# represents the lowest sum for a set of four primes with this property.

# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.



import time
from termcolor import colored
import math
import itertools as iter

primes = []
def isPrime(num):
    # print('num=',num)
    flag = True
    if num == 1:
        flag = False
    for i in range(2, round(math.sqrt(num))+1):
        if num % i == 0:
            flag = False
    # print('flag=',flag)
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

def make_chain(chain):
    if len(chain) == set_size:
        return chain 
    for p in primes:
        if p > chain[-1] and all_prime(chain+[p]):
            new_chain = make_chain(chain+[p])
            if new_chain:
                return new_chain
    return False

def check(myarray):
    return all(isPrime(int(str(p[0]) + str(p[1]))) for p in iter.permutations(myarray, 2))
    # for p in iter.permutations(myarray, 2):
    #     # print('#=',p,'|',p[0],p[1],int(str(p[0])+str(p[1])))
    #     return all(isPrime( int(str(p[0])+str(p[1]))  ))

def main_process():
    p = find_prime(9000)
    # print('p=',p)
    for i in range(len(p)):
        for j in range(i+1, len(p)):
            if not check([p[i],p[j]]): continue
            for k in range(j+1, len(p)):
                if not check([p[i],p[j],p[k]]): continue
                for l in range(k+1, len(p)):
                    if not check([p[i],p[j],p[k],p[l]]): 
                        continue
                    else:
                        print('4:',p[i],p[j],p[k],p[l])
                        
                    for m in range(l+1, len(p)):
                        if not check([p[i],p[j],p[k],p[l],p[m]]): 
                            continue
                        else:
                            print(p[i],p[j],p[k],p[l],p[m],'sum=',(p[i] + p[j] + p[k] + p[l] + p[m]))
                            return
                        

    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)