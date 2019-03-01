# Spiral primes
# Problem 58
# Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

# 37 36 35 34 33 32 31
# 38 17 16 15 14 13 30
# 39 18  5  4  3 12 29
# 40 19  6  1  2 11 28
# 41 20  7  8  9 10 27
# 42 21 22 23 24 25 26
# 43 44 45 46 47 48 49

# It is interesting to note that the odd squares lie along the bottom right diagonal,
# but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

# If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed.

#  If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?

import time
from termcolor import colored
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

def main_process():
    all_corners = [1]
    prime_count = 0
    avg = 1
    for i in range(1,10):
        square = (2*i+1)*(2*i+1)
        turn = [square - 6*i, square - 4*i, square - 2*i, square]
        if (square - 6*i) not in all_corners:
            all_corners.append(square - 6*i)
            if isPrime(square - 6*i):
                prime_count += 1
        if (square - 4*i) not in all_corners:
            all_corners.append(square - 4*i)
            if isPrime(square - 4*i):
                prime_count += 1
        if (square - 2*i) not in all_corners:
            all_corners.append(square - 2*i)
            if isPrime(square - 2*i):
                prime_count += 1
        if (square ) not in all_corners:
            all_corners.append(square )
            if isPrime(square):
                prime_count += 1
        print(turn)
        avg = prime_count/len(all_corners)
        print(prime_count,len(all_corners),'avg=',avg,(2*i + 1))
        if avg < 0.1:
            print('find',2*i + 1)
            break

    # print(colored('mycount=', 'red'), all_corners)

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)