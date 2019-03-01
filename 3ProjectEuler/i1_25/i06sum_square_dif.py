# coding: utf-8
# The sum of the squares of the first ten natural numbers is,

# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
import math
def sum_square(n):
    result = math.pow(n, 2)*math.pow(n+1, 2)/4
    return result

def square_sum(n):
    result = n*(2*n+1)*(n+1)/6
    return result

if __name__ == "__main__":
    input = 100
    print(sum_square(input) - square_sum(input))