# Euler discovered the remarkable quadratic formula:

# n² + n + 41

# It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39.
 # However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

# The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. 
# The product of the coefficients, −79 and 1601, is −126479.

# Considering quadratics of the form:

# n² + an + b, where |a| < 1000 and |b| < 1000

# where |n| is the modulus/absolute value of n
# e.g. |11| = 11 and |−4| = 4
# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, 
# starting with n = 0.


# n=0 show b should be prime,
# n=1 show 1 + a + b is prime, show a is odd  1 + a + b > 0  a > - (1 + b)
# n² + an + b >0  => an > - (b + n**2)   
import math

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

def print_Qua(n):
    global the_count
    global theA
    global theB
    blist = []
    for i in range(0,n):
        if isPrime(i):
            blist.append(i)


    for bi in blist:
        for ai in range(-n+1, n,2):
            tempcount = 0

            for i in range(0,n):                
                if  ai > -(1 + bi):
                    f = i*i + ai * i + bi
                    if f > 0 and isPrime(f):
                        print('f(',i,')','= n² + ',ai ,'n + ',bi, '=' ,f)
                        tempcount += 1
                    else:
                        print('\n',tempcount)
                        if the_count < tempcount:
                            the_count = tempcount
                            theA = ai
                            theB = bi
                        break



the_count = 0
theA = 0
theB = 0
if __name__ == "__main__":
    print_Qua(1000)
    print('###',the_count, 'a=',theA, 'b=',theB, theA * theB)