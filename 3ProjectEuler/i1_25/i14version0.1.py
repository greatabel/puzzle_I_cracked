# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

import math

cache = {1: 1}
def find_sequence_length(n):
    if n not in cache:
        if n % 2 == 0:
            cache[n] = 1 + find_sequence_length(n / 2)
        else:
            cache[n] = 1 + find_sequence_length(3 * n + 1)
    return cache[n]
        



if __name__ == "__main__":
    MAX = 0
    item = 0
    for i in range(1,int(1e6)+1):
        if i % 10000 == 0:
            print(i)
        result = find_sequence_length(i)
        if  result > MAX:
            MAX = result
            item = i
    print(MAX, item)
