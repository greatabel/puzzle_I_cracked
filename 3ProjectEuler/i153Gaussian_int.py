'''

As we all know the equation x2=-1 has no solutions for real x. 
If we however introduce the imaginary number i this equation has two solutions: x=i and x=-i. 
If we go a step further the equation (x-3)2=-4 has two complex solutions: x=3+2i and x=3-2i. 
x=3+2i and x=3-2i are called each others' complex conjugate. 
Numbers of the form a+bi are called complex numbers. 
In general a+bi and a−bi are each other's complex conjugate.

A Gaussian Integer is a complex number a+bi such that both a and b are integers. 
The regular integers are also Gaussian integers (with b=0). 
To distinguish them from Gaussian integers with b ≠ 0 we call such integers "rational integers." 
A Gaussian integer is called a divisor of a rational integer n if the result is also a Gaussian integer. 
If for example we divide 5 by 1+2i we can simplify 51+2i in the following manner: 
Multiply numerator and denominator by the complex conjugate of 1+2i: 1−2i. 
The result is 51+2i=51+2i1−2i1−2i=5(1−2i)1−(2i)2=5(1−2i)1−(−4)=5(1−2i)5=1−2i. 
So 1+2i is a divisor of 5. 
Note that 1+i is not a divisor of 5 because 51+i=52−52i. 
Note also that if the Gaussian Integer (a+bi) is a divisor of a rational integer n, 

then its complex conjugate (a−bi) is also a divisor of n.

In fact, 5 has six divisors such that the real part is positive: {1, 1 + 2i, 1 − 2i, 2 + i, 2 − i, 5}. 
The following is a table of all of the divisors for the first five positive rational integers:

n   Gaussian integer divisors
with positive real part Sum s(n) of 
these divisors
1   1   1
2   1, 1+i, 1-i, 2  5
3   1, 3    4
4   1, 1+i, 1-i, 2, 2+2i, 2-2i,4    13
5   1, 1+2i, 1-2i, 2+i, 2-i, 5  12
For divisors with positive real parts, then, we have: ∑n=15s(n)=35.

For ∑n=1105s(n)=17924657155.

What is ∑n=1108s(n)?

#----------------------------#



'''



import math
import time
from termcolor import colored


n = 10 ** 8
# n = 10 ** 5


def main_process():
    #sum of rational integer divisors:
    result = sum(i*(n//i) for i in range(1, n+1))
    print(result)
    #Gaussian integers:
    for x in range(1, int(math.sqrt(n))+1):
        if x % 1000 == 0:
            print(x*100//n, ' percentage')
        for y in range(1, int(math.sqrt(n))+1):
            #We try each pair of divisors x + iy, x - iy. The sum of these
            #will be 2x. Then we check how many times this pair
            #appears + how often multiples appear using a clever summation.
            #This is why we only do this for gcd(x, y) = 1.
            if math.gcd(x, y) == 1:
                a = x**2+y**2
                result += 2*x*sum((n//(a*j))*j for j in range(1, (n//a) + 1))


    print(colored('mycount=', 'red'), result)
    # 17971254122360635

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)









