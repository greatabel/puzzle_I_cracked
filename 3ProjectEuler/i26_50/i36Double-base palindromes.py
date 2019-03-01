# Double-base palindromes
# Problem 36
# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

# (Please note that the palindromic number, in either base, may not include leading zeros.)

import time
# from i1_25 import i04find_palindrome

def is_palindrome(string):
    for i,char in enumerate(string):
        if char != string[-i-1]:
            return False
    return True



if __name__ == "__main__":
    tic = time.clock()
    # isCircular(971)
    # limit = find_circular_below(1000)
    isum = 0
    for i in range(1,10**6):
        # if i04find_palindrome.palindromic(i):
        if is_palindrome(str(i)) and is_palindrome(str(bin(i))[2:]):
            print(str(i),str(bin(i))[2:])
            isum += i 
    print('#=',isum)

    toc = time.clock()
    print("time=",toc - tic)