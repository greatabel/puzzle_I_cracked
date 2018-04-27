# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

import math

def find_prime_factors(num):
    results = []
    i = 2
    while i <= num:

        while num >= i:
            if num % i == 0 :
                results.append(i)
                num = round(num/i)
                print("num= ",num, "i= ", i)
            else:
                break
        i = i+1
    print(results)

if __name__ == "__main__":

    import timeit
    tic=timeit.default_timer()
    # find_prime_factors(13195)
    find_prime_factors(600851475143)
    toc=timeit.default_timer() 
    print(toc - tic, " seconds")
