'''
The proper divisors of a number are all the divisors excluding the number itself. 
For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. 
As the sum of these divisors is equal to 28, we call it a perfect number.

Interestingly the sum of the proper divisors of 220 is 284 
and the sum of the proper divisors of 284 is 220, forming a chain of two numbers. 
For this reason, 220 and 284 are called an amicable pair.

Perhaps less well known are longer chains. For example, starting with 12496, we form a chain of five numbers:

12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)

Since this chain returns to its starting point, it is called an amicable chain.

Find the smallest member of the longest amicable chain with no element exceeding one million.

'''
# https://blog.dreamshire.com/project-euler-95-solution/
import time
from termcolor import colored

limit = 10 ** 6
# test
# limit = 100

# def perfect_number(n):
#     isum = 0
#     for x in range(1, n):
        
#         if n % x == 0:
#             isum += x
#     return isum



def main_process():
    # for i in range(1, limit):
    #     if perfect_number(i) == i:
    #         print(i)
    d = [1] * limit
    # print('d=', d)
    for i in range(2, limit//2):
        for j in range(2*i, limit , i):
            d[j] += i

    max_cl = 0
    for i in range(2, limit):
        n, chain = i, []
        while d[n] < limit:
            d[n], n = limit+1, d[n]
            try: k = chain.index(n)
            except ValueError: 
                chain.append(n)
            else: 
                if len(chain[k:]) > max_cl:
                    max_cl, min_link = len(chain[k:]), min(chain[k:])


    print(colored('min_link=', 'red'), min_link)

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)


