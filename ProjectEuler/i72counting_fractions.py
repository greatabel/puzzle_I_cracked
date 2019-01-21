'''
Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, 
it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000?
'''

import time
from termcolor import colored

# https://www.mathblog.dk/project-euler-72-reduced-proper-fractions/
def main_process():
    limit = 10 ** 6
    phi_list = list(range(0,limit + 1))
    sum_phi = 0
    # print(phi_list)
    for i in range(2, limit + 1 ):
        # print('i=', i, 'here', phi_list[i])
        if phi_list[i] == i:

            for j in range(i, limit + 1, i):
                phi_list[j] *= (i - 1)/ i
        sum_phi += phi_list[i]
    # print(phi_list)
    print(colored('mycount=', 'red'), sum_phi)

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)