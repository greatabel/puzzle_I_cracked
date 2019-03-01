'''
It turns out that 12 cm is the smallest length of wire that can be bent to form 
an integer sided right angle triangle in exactly one way, but there are many more examples.

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer 
sided right angle triangle, and other lengths allow more than one solution to be found; 
for example, using 120 cm it is possible to form exactly three different integer sided right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, 
for how many values of L ≤ 1,500,000 can exactly one integer sided right angle triangle be formed?
'''
import time
from termcolor import colored
import math
from math import gcd

# 太慢了
# def gougu_triple(limit):
#     count = 0
#     for l in range(3, limit):
#         for a in range(1, int(l/2)):
#             for b in range(1, int((l - a)/2)):
#                 c = l - a  - b
#                 if a ** 2 + b ** 2 == c **2:
#                     count += 1
#                     if count % 100 == 0:
#                         print('c=', count, '%', l*100/limit)
#                     # print(a, b, c)
#     print(count)
def pythagorean_triple(max_length):
    numOfTriangles, rightTriangles = 0,  [0] * (max_length+1)
    for m in range(2, int(math.sqrt((max_length-4)//2))):
            for n in range (1, m):       # m > n
                # check whether (m − n) is odd and  m & n are co-prime
                if (m - n) % 2 == 1 and 1 == gcd(m, n):             
                    a, b, c = m*m-n*n, 2*m*n, m*m+n*n
                    p = a+b+c  # the perimeter of a right angle triangle
             
                    if p <= max_length and 1 == gcd(c, gcd(b, a)):
                        #for k in range (1, (max_length+1)//p+1):   ## working
                        #    rightTriangles[p*k] += 1
                        for s in range(p, max_length+1, p):            ## faster 
                            rightTriangles[s] += 1
    numOfTriangles = len([s for s in range(1, max_length+1) if 1 == rightTriangles[s]])
    print(numOfTriangles)






def main_process():
    # pythagorean_triple(100)
    pythagorean_triple(1500000)
    # print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)