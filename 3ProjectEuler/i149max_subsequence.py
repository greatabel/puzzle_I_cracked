'''

Looking at the table below, it is easy to verify that the maximum possible sum of 

adjacent numbers in any direction (horizontal, vertical, diagonal or anti-diagonal) is 16 (= 8 + 7 + 1).

−2  5   3   2
9   −6  5   1
3   2   7   3
−1  8   −4    8
Now, let us repeat the search, but on a much larger scale:

First, generate four million pseudo-random numbers using a specific form of what 

is known as a "Lagged Fibonacci Generator":

For 1 ≤ k ≤ 55, sk = [100003 − 200003k + 300007k3] (modulo 1000000) − 500000.
For 56 ≤ k ≤ 4000000, sk = [sk−24 + sk−55 + 1000000] (modulo 1000000) − 500000.

Thus, s10 = −393027 and s100 = 86613.

The terms of s are then arranged in a 2000×2000 table, using the first 2000 numbers to

 fill the first row (sequentially), the next 2000 numbers to fill the second row, and so on.

Finally, find the greatest sum of (any number of) adjacent entries in any direction (horizontal, 

vertical, diagonal or anti-diagonal).

#----------------------------#

不想解决此题，跳过：使用 nayuki的方案：

'''


import time
from termcolor import colored


def getsum(x, y, dx, dy):
    global grid
    result = 0
    current = 0
    while 0 <= x < SIZE and 0 <= y < SIZE:
        current = max(current + grid[y][x], 0)  # Reset the running sum if it goes negative
        result = max(current, result)  # Keep track of the best seen running sum
        x += dx
        y += dy
    return result


SIZE = 2000
grid = []
def main_process():

    
    global grid
    # Generate the pseudorandom sequence according to the lagged Fibonacci generator
    randseq = []
    for i in range(SIZE**2):
        k = i + 1
        if k <= 55:
            randseq.append((100003 - 200003*k + 300007*k*k*k) % 1000000 - 500000)
        else:
            randseq.append((randseq[-24] + randseq[-55]) % 1000000 - 500000)
    
    # Reshape the sequence into into a 2D array
    grid = [randseq[i * SIZE : (i + 1) * SIZE] for i in range(SIZE)]
    
    # For the sequence of numbers in the grid at positions (x, y), (x+dx, y+dy), (x+2*dx, y+2*dy), ... until the
    # last in-bounds indices, this function returns the maximum sum among all possible substrings of this sequence.

    
    # Scan along all line directions and positions
    ans = max(
        max(getsum(0, i, +1,  0),  # Horizontal from left edge
            getsum(i, 0,  0, +1),  # Vertical from top edge
            getsum(0, i, +1, +1),  # Diagonal from left edge
            getsum(i, 0, +1, +1),  # Diagonal from top edge
            getsum(i, 0, -1, +1),  # Anti-diagonal from top edge
            getsum(SIZE - 1, i, -1, +1))  # Anti-diagonal from right edge
        for i in range(SIZE))
    # return str(ans)
    print(colored('mycount=', 'red'), ans)
    # mycount= 52852124

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)
