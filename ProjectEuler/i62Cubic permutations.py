# Cubic permutations
# Problem 62
# The cube, 41063625 (3453), can be permuted to produce two other cubes: 
# 56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

# Find the smallest cube for which exactly five permutations of its digits are cube.


import time
from termcolor import colored
from collections import defaultdict

def cube(x): 
    return x**3

def main_process():
    cubes = defaultdict(list)
    for i in range(1,9000):
        c = cube(i)
        digits = ''.join(sorted([d for d in str(c)]))
        cubes[digits].append(c)
    print(len(cubes))
    for k,v in list(cubes.items()):
        # print(k,v)
        if len(v) == 5:
            print(k,int(min(v))**(1./3.),'min=',min(v),'v=',v)
    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)