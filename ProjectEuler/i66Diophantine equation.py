# Consider quadratic Diophantine equations of the form:

# x2 – Dy2 = 1

# For example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1.

# It can be assumed that there are no solutions in positive integers when D is square.

# By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

# 32 – 2×22 = 1
# 22 – 3×12 = 1
# 92 – 5×42 = 1
# 52 – 6×22 = 1
# 82 – 7×32 = 1

# Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.
# Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.


import time
from termcolor import colored

import math
def main_process():
    maxn=1
    maxD=2
    for D in range(2,1001):
        tmp=math.sqrt(D)
        tmp=int(tmp)
        if tmp*tmp==D:
            continue

        m=0
        d=1
        a=tmp
        #print(a)
        n1=1
        d1=0
        num=a
        den=1

        while num*num-D*den*den!=1:
            m=int(a*d-m)
            d=int((D-m*m)/d)
            a=int((tmp+m)/d)

            n2=n1
            n1=num
            d2=d1
            d1=den

            num=int(a*n1+n2)
            den=int(a*d1+d2)
            #print('num = ',num)
            #print('den = ',den)
            #print ('result = ',num*num-D*den*den)
        if num >maxn:
            maxn=num
            maxD=D
    print(maxD)

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)