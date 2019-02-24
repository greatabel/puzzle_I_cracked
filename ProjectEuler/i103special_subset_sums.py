'''
Let S(A) represent the sum of elements in set A of size n. 
We shall call it a special sum set if for any two non-empty disjoint subsets, 
B and C, the following properties are true:

S(B) ≠ S(C); that is, sums of subsets cannot be equal.
If B contains more elements than C then S(B) > S(C).
If S(A) is minimised for a given n, we shall call it an optimum special sum set. 
The first five optimum special sum sets are given below.

n = 1: {1}
n = 2: {1, 2}
n = 3: {2, 3, 4}
n = 4: {3, 5, 6, 7}
n = 5: {6, 9, 11, 12, 13}

It seems that for a given optimum set, A = {a1, a2, ... , an}, the next optimum set 
is of the form B = {b, a1+b, a2+b, ... ,an+b}, where b is the "middle" element on the previous row.

By applying this "rule" we would expect the optimum set for n = 6 to be A = {11, 17, 20, 22, 23, 24},
 with S(A) = 117. However, this is not the optimum set, as we have merely applied an algorithm to 
 provide a near optimum set. The optimum set for n = 6 is A = {11, 18, 19, 20, 22, 25}, with S(A) = 115 
 and corresponding set string: 111819202225.

Given that A is an optimum special sum set for n = 7, find its set string.

NOTE: This problem is related to Problem 105 and Problem 106.
'''

import time
from termcolor import colored
from random import randint


def powerset(s):
    d = dict(zip(
            (1<<i for i in range(len(s))),
            (set([e]) for e in s)
            ))

    subset = set()
    yield subset
    for i in range(1, 1<<len(s)):
        subset = subset ^ d[i & -i]
        yield subset


def main_process():
    nos1 = [19, 30, 37, 38, 39, 41, 44]
    nos2 = [20, 31, 38, 39, 40, 42, 45] # This is the answer!

    while True:
        test = [a + randint(-3, 3) for a in nos1]
        
        subsets = [list(A) for A in list(powerset(test))]
        subset_sums = [sum(a) for a in subsets]

        #print sorted(subset_sums)
        #print sorted(zip(subset_sums, subsets))

        #print ''.join([str(a) for a in test]), sum(test)

        #print len(set(subset_sums)), len(subset_sums), 

        three_sets = [a for a in subsets if len(a) == 3]
        four_sets = [a for a in subsets if len(a) == 4]
        three_set_sums = [sum(a) for a in three_sets]
        four_set_sums = [sum(a) for a in four_sets]

        #print min(four_set_sums), max(three_set_sums), 
        if len(set(subset_sums)) == len(subset_sums) and min(four_set_sums) > max(three_set_sums):
            print(colored('mycount=', 'red'), test, sum(test))
            break
    

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)