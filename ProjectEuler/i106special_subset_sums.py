'''
Let S(A) represent the sum of elements in set A of size n. 
We shall call it a special sum set if for any two non-empty disjoint subsets,
 B and C, the following properties are true:

S(B) ≠ S(C); that is, sums of subsets cannot be equal.
If B contains more elements than C then S(B) > S(C).
For this problem we shall assume that a given set contains n strictly increasing elements 
and it already satisfies the second rule.

Surprisingly, out of the 25 possible subset pairs that can be obtained from a set for which n = 4, 
only 1 of these pairs need to be tested for equality (first rule). Similarly, when n = 7, only 70 
out of the 966 subset pairs need to be tested.

For n = 12, how many of the 261625 subset pairs that can be obtained need to be tested for equality?

NOTE: This problem is related to Problem 103 and Problem 105.

'''

import time
from termcolor import colored

# skip this problem by using solution https://github.com/hughdbrown/Project-Euler/blob/master/euler-106.py

def pairwiseCompare(x, y) :
    return sum((1 if x1 > y1 else 0) for x1, y1 in zip(x,y))

def choose(s, i) :
    if not i :
        yield []
    else :
        for j in range(int(len(s)) - i + 1) :
            a, rest = [s[j]], s[j+1: ]
            for ss in choose(rest, i-1) :
                yield a + ss

def main_process(hi) :
    total = 0
    s = range(1, hi + 1)
    ss = set(s)
    for i in range(2, 1 + int(hi/2)) :
        for x in choose(s, i) :
            diff = ss - set(x)
            diff -= set(a for a in diff if a < x[0])
            for y in choose(sorted(diff), i) :
                total += (1 if pairwiseCompare(x, y) not in [0, i] else 0)
    print(hi, total)


if __name__ == "__main__":
    tic = time.clock()
    
    main_process(12)

    toc = time.clock()
    print("time=",toc - tic)