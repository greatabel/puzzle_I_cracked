# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

import math

def palindromic(num):
    # print('num=', num)
    results = []
    while num > 0:
        results.append(num%10)
        num = round((num-num%10 )/10)
    # print("results=", results)
    flag = (results == list(reversed(results)))
    if flag:
        print("flag:",list(reversed(results)))

    return flag

def find_largestpalindromic_in_digit(digit):
    result = 0
    for i in range(round(math.pow(10, digit-1)), round(math.pow(10, digit))):
            for j in range(round(math.pow(10, digit-1)), round(math.pow(10, digit))):
                if palindromic(i*j) and i*j>result:
                    result = i*j
                    print(result)
                # print(i*i)
    return result

if __name__ == "__main__":
    print(find_largestpalindromic_in_digit(3))
