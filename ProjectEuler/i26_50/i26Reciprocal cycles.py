# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

# 1/2 =   0.5
# 1/3 =   0.(3)
# 1/4 =   0.25
# 1/5 =   0.2
# 1/6 =   0.1(6)
# 1/7 =   0.(142857)
# 1/8 =   0.125
# 1/9 =   0.(1)
# 1/10    =   0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.


# http://guozi149.me/foundations/math/516

from decimal import Decimal

max_index = 0
maxlen = 0

def count_repeat(numerator,denominator):
    global max_index
    global maxlen
    # numerator *= 10
    reminder = (numerator  % denominator) * 10
    print(numerator,'  /  ',denominator,' reminder=', reminder)
    results = []
    while reminder not in results:
        results.append(reminder)
        reminder = (reminder % denominator) * 10

        # print('reminder=', reminder)
    if 0 not in results:
        print('results=', results,'len=',len(results),'denominator=',denominator)
        if len(results) > maxlen:
            maxlen = len(results)
            max_index = denominator


def find(n):
    for i in range(2,n+1):
        count_repeat(1, i)
        # print(i,Decimal(1/i))
    print('###index=',max_index,maxlen)


if __name__ == "__main__":

    find(1000)