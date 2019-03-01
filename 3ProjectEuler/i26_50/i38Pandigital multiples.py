# Pandigital multiples
# Problem 38
# Take the number 192 and multiply it by each of 1, 2, and 3:

# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?


import time
import math
def  find():
    # 918273645 is not the result ,show show start with 9, 9x is not, 9xx is not ,9xxx is possible
    theresult = 0
    for i in range(9000,10000):
        istr = str(i) + str(i*2)
        if "0" not in istr:
            if len(set(istr)) == 9:
                print(istr)
                if int(istr) > theresult:
                    theresult = int(istr)
    print('result', theresult)


if __name__ == "__main__":
    tic = time.clock()
    find()

    toc = time.clock()
    print("time=",toc - tic)