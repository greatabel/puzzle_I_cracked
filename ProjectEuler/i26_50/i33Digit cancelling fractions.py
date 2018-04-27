# Digit cancelling fractions
# Problem 33
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

import time

def get_digital(number):
    results = []
    while number > 0:
        result = number % 10
        number = number // 10
        results.append(result)
    return results



def find_allmatches(numbers):
    final_i = 1
    final_j = 1
    for i in numbers:
        for j in numbers:
            if j != 0:
                # print(i,"/", j)
                ii = get_digital(i)
                jj = get_digital(j)
                commons = list(set(ii).intersection(jj))
                if len(commons) != 0 and commons[0] != 0 and i < j:
                    # print(commons[0],ii,jj)
                    ii.remove(commons[0])
                    jj.remove(commons[0])
                    if len(ii) > 0 and len(jj) > 0:
                        # print("i2/j2=",ii[0],"/",jj[0])
                        if jj[0] != 0 and (ii[0] / jj[0] )==  ( i / j) :
                            print( ii[0],"/", jj[0],"=", i,"/",j)
                            final_i *= ii[0]
                            final_j *= jj[0]
    print("final=", final_i, final_j)
    from fractions import gcd
    print(final_j / gcd(final_i, final_j))

    
if __name__ == "__main__":
    tic = time.clock()
    # for i in range(0,20):
    #     print(i,fib(i),len(str(fib(i))))
    # find_allpowers(5,5)
    # find_allpowers(10000,4)
    results = find_allmatches(list(range(1,100)))
    print('#', results)

    toc = time.clock()
    print("time=",toc - tic)