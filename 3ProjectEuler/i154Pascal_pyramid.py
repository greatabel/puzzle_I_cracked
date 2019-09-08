'''

Then, we calculate the number of paths leading from the apex to each position:

A path starts at the apex and progresses downwards to any of the three spheres directly below the current position.

Consequently, the number of paths to reach a certain position is the sum of the numbers immediately above it (depending on the position, there are up to three numbers above it).

The result is Pascal's pyramid and the numbers at each level n are the coefficients of the trinomial expansion (x + y + z)n.

How many coefficients in the expansion of (x + y + z)200000 are multiples of 1012?

#----------------------------#



'''




import time
from termcolor import colored



M = 200000
L = 12

def mypool(n, p):
    pool = [0] * (n + 1)
    for i in range(1, n + 1):
        ii = i // p
        pool[i] = ii + pool[ii]
    return pool

def main(M, L):
    P2 = mypool(M, 2)
    P5 = mypool(M, 5)
    M2 = P2[M] - L
    M5 = P5[M] - L
    count = 0
    # V = [0, 1, 3, 6]

    for a in range(M, (M - 1) // 3, -1): #(M + 2) // 3, M + 1):
        if a % 2000 == 0: print(a, count)
        a5 = M5 - P5[a]
        a2 = M2 - P2[a]
        for b in range((M - a + 1) // 2, min(a, M - a) + 1):
            c = M - a - b
            if P5[b] + P5[c] <= a5 and P2[b] + P2[c] <= a2:
                count += 6 if a != b != c else 3

    return count


def main_process():
    count = main(M, L)
    print(colored('mycount=', 'red'), count)
# mycount= 479742450
# time= 672.5573850000001


if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





