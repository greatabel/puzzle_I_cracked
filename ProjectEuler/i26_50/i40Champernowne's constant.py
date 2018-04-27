# Champernowne's constant
# Problem 40
# An irrational decimal fraction is created by concatenating the positive integers:

# 0.123456789101112131415161718192021...

# It can be seen that the 12th digit of the fractional part is 1.

# If dn represents the nth digit of the fractional part, find the value of the following expression.

# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

import time
import math

# 1-9: 1-9
# 10-99: 10-189
# 100-999: 190-2.889
# 1.000-9.999:  2.890-38.889
# 10.000-99.999: 38.890 – 488.889
# 100.000-999.999: 488.890 – 5.888.889
# so possible 10** 6 is at index 500,000 near
def  find():
    myStr = ""
    for i in range(1, 500000):
        myStr += str(i)
    result = 1
    for i in range(0,7):
        print(myStr[10**i])
        result *= int(myStr[10**i - 1])
    print(result)

if __name__ == "__main__":
    tic = time.clock()
    find()

    toc = time.clock()
    print("time=",toc - tic)