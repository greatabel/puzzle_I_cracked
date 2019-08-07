'''

A 4x4 grid is filled with digits d, 0 ≤ d ≤ 9.

It can be seen that in the grid

6 3 3 0
5 0 4 3
0 7 1 4
1 2 4 5

the sum of each row and each column has the value 12. Moreover the sum of each diagonal is also 12.

In how many ways can you fill a 4x4 grid with the digits d, 0 ≤ d ≤ 9 so that each row, 

each column, and both diagonals have the same sum?

#----------------------------#



'''




import time
from termcolor import colored

def compute():
    ans = 0
    digits = tuple(range(10))
    for b in digits:
        for c in digits:
            for d in digits:
                for e in digits:
                    for i in digits:
                        m = b + c + d - e - i
                        if m < 0 or m > 9: continue
                        for k in digits:
                            f = b + c + d*2 - e - i - k
                            if f < 0 or f > 9: continue
                            for a in digits:
                                for g in digits:
                                    o = a + b + d - g - k
                                    if o < 0 or o > 9: continue
                                    j = a + b + c - g - m
                                    if j < 0 or j > 9: continue
                                    l = a + b + c + d - i - j - k
                                    if l < 0 or l > 9: continue
                                    h = a + b + c + d - e - f - g
                                    if h < 0 or h > 9: continue
                                    n = a + c + d - f - j
                                    if n < 0 or n > 9: continue
                                    p = a + b + c - h - l
                                    if p < 0 or p > 9: continue
                                    ans += 1
    return ans

def main_process():
    results = compute()
    print(colored('mycount=', 'red'), results)
    # mycount= 7130034

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





