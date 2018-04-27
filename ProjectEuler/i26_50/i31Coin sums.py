# Coin sums
# Problem 31
# In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:

# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?

import time

def find_allways(total, sizes):
    if len(sizes) == 0:
        return 1
    else:
        mycount = 0
        size = sizes[0]
        num = total // size  
        num += 1
        for i in range(0, num):
            mycount += find_allways(  total - size * i, sizes[1:])
       
        return mycount


if __name__ == "__main__":
    tic = time.clock()
    # for i in range(0,20):
    #     print(i,fib(i),len(str(fib(i))))
    # find_allpowers(5,5)
    # find_allpowers(10000,4)
    results = find_allways(200,[200, 100, 50, 20, 10, 5, 2])
    print('#', results)

    toc = time.clock()
    print("time=",toc - tic)