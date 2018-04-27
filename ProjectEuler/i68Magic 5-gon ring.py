# Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and each line adding to nine.


# Working clockwise, and starting from the group of three with the numerically lowest external node (4,3,2 in this example), 
# each solution can be described uniquely. For example, the above solution can be described by the set: 4,3,2; 6,2,1; 5,1,3.

# It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are eight solutions in total.

# Total   Solution Set
# 9   4,2,3; 5,3,1; 6,1,2
# 9   4,3,2; 6,2,1; 5,1,3
# 10  2,3,5; 4,5,1; 6,1,3
# 10  2,5,3; 6,3,1; 4,1,5
# 11  1,4,6; 3,6,2; 5,2,4
# 11  1,6,4; 5,4,2; 3,2,6
# 12  1,5,6; 2,6,4; 3,4,5
# 12  1,6,5; 3,5,4; 2,4,6
# By concatenating each group it is possible to form 9-digit strings; the maximum string for a 3-gon ring is 432621513.

# Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings. 
# What is the maximum 16-digit string 
# for a "magic" 5-gon ring?

import time
from termcolor import colored

import itertools

def main_process(n):
    
    all_possilble = list(itertools.permutations(range(1,n+1), n))
    matches = []
    for l in all_possilble:
        test = is_gong10(l)
        if test is not None and test not in matches:
            matches.append(test)
    matches.sort()
    print(matches)
    print(colored('mycount=', 'red'), 'results')

def is_gong6(l):
    sum_I = l[0]+l[1]+l[2]
    sum_II = l[2]+l[3]+l[4]
    sum_III = l[1]+l[4]+l[5]
    if sum_I == sum_II and sum_II == sum_III:
        if l[0] < l[3] and l[0] < l[5]:
            # print(l[0],l[1],l[2],'#',l[3],l[2],l[4],'#',l[5],l[4],l[1])
            return int(str(l[0])+str(l[1])+str(l[2])+str(l[3])+\
                str(l[2])+str(l[4])+str(l[5])+str(l[4])+str(l[1]))
        if l[3] < l[0] and l[3] < l[5]:
            return int(str(l[3])+str(l[2])+str(l[4])+str(l[5])+\
                str(l[4])+str(l[1])+str(l[0])+str(l[1])+str(l[2]))
        if l[5] < l[0] and l[5] < l[3]:
            return int(str(l[5])+str(l[4])+str(l[1])+str(l[0])+\
                str(l[1])+str(l[2])+str(l[3])+str(l[2])+str(l[4]))             
    else:
        return None

def is_gong10(l):
    if is_right_10(l):
        return to10string(l)

def is_right_10(l):
    seed = l[9] + l[4] + l[0]
    for i in range(5, 9):
        if (l[i] + l[i-5] + l[i-4]) != seed:
            return False
    return True

def to10string(l):
    triples = [(l[i], l[i-5], l[i-4]) for i in range(5,9)] + [(l[9], l[4], l[0])]
    pivot = triples.index(min(triples))
    triples = triples[pivot:] + triples[:pivot]
    return ''.join(str(triple[i]) for triple in triples for i in range(len(triple)))

if __name__ == "__main__":
    tic = time.clock()
    
    main_process(10)

    toc = time.clock()
    print("time=",toc - tic)