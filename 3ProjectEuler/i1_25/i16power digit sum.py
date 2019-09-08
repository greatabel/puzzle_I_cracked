# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2^1000?

# python 默认支持大数，不知道难点在哪儿，哈哈
import math
if __name__ == "__main__":
    n = int(math.pow(2, 1000))
    print("n=",str(n))
    result = 0
    while n != 0:
        result += int(n % 10)
        n = n // 10
        print( "n%10=",n % 10, "n=",n)
    print(result)