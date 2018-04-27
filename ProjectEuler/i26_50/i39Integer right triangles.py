# Integer right triangles
# Problem 39
# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

# {20,48,52}, {24,45,51}, {30,40,50}

# For which value of p ≤ 1000, is the number of solutions maximised?

import time
import math
def  find(bound):
    # 918273645 is not the result ,show show start with 9, 9x is not, 9xx is not ,9xxx is possible
    pdict = {}
    for p in range(1,bound):
        pdict[p] = 0
        for a in range(1, bound//2 + 1):
            for b in range(1, p - a - 1):
                if a**2 + b**2 == (p - a - b) ** 2:
                    print(a,b,p-a-b)
                    pdict[p] += 1

        print('p=',p,'count=',pdict[p])
    print('pdict=',pdict)
    
    # http://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
    print(max(pdict, key=pdict.get), '#',pdict[max(pdict, key=pdict.get)])

if __name__ == "__main__":
    tic = time.clock()
    find(1000)

    toc = time.clock()
    print("time=",toc - tic)