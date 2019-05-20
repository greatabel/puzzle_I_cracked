'''

In a triangular array of positive and negative integers, we wish to find a sub-triangle 

such that the sum of the numbers it contains is the smallest possible.

In the example below, it can be easily verified that the marked triangle satisfies 

this condition having a sum of −42.


We wish to make such a triangular array with one thousand rows, 

so we generate 500500 pseudo-random numbers sk in the range ±219, 

using a type of random number generator (known as a Linear Congruential Generator) as follows:

t := 0 
for k = 1 up to k = 500500: 
    t := (615949*t + 797807) modulo 220
    sk := t−219

Thus: s1 = 273519, s2 = −153582, s3 = 450905 etc

Our triangular array is then formed using the pseudo-random numbers thus:

s1
s2  s3
s4  s5  s6  
s7  s8  s9  s10
...
Sub-triangles can start at any element of the array and extend down as far 

as we like (taking-in the two elements directly below it from the next row, 

the three elements directly below from the row after that, and so on). 
The "sum of a sub-triangle" is defined as the sum of all the elements it contains. 
Find the smallest possible sub-triangle sum.



#----------------------------#

#----------------------------#

不想解决此题，跳过：使用 nayuki的方案

'''



import time
from termcolor import colored


def compute_plain(triangle):
    # Calculate cumulative sums for each row
    rowsums = []
    for row in triangle:
        rowsum = [0]
        for j in range(len(row)):
            rowsum.append(rowsum[j] + row[j])
        rowsums.append(rowsum)
    
    # Calculate minimum subtriangle sum for each apex position
    result = 0
    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            # Apex element selected at triangle[i][j]
            cursum = 0
            for k in range(i, len(triangle)):  # Ending row (inclusive)
                cursum += rowsums[k][k - i + 1 + j] - rowsums[k][j]
                result = min(cursum, result)
    return result


def compute_numpy(triangle):
    # Calculate cumulative sums for each row
    import numpy
    ROWS = len(triangle)
    rowsums = numpy.zeros([ROWS, ROWS + 2], dtype=numpy.int64)
    for (i, row) in enumerate(triangle):
        rowsums[i, : i + 2] = numpy.cumsum([0] + row, dtype=numpy.int64)
    
    # Calculate minimum subtriangle sum for each apex position
    result = 0
    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            # Apex element selected at triangle[i][j]
            ks = numpy.arange(i, ROWS, dtype=numpy.uint32)
            terms = rowsums[ks, ks - i + 1 + j] - rowsums[ks, j]
            sums = numpy.cumsum(terms, dtype=numpy.int64)
            result = min(numpy.min(sums), result)
    return result


def lcg_random():
    state = 0
    while True:
        state = (615949 * state + 797807) & ((1 << 20) - 1)
        yield state - (1 << 19)

def main_process():
    ROWS = 1000
    rand = lcg_random()
    triangle = [[next(rand) for j in range(i + 1)] for i in range(ROWS)]
    try:
        ans = compute_numpy(triangle)
    except ImportError:
        ans = compute_plain(triangle)
    print(colored('mycount=', 'red'), ans)

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)
