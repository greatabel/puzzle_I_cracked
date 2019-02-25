'''
Let S(A) represent the sum of elements in set A of size n. We shall call it a special sum
 set if for any two non-empty disjoint subsets, B and C, the following properties are true:

S(B) ≠ S(C); that is, sums of subsets cannot be equal.
If B contains more elements than C then S(B) > S(C).
For example, {81, 88, 75, 42, 87, 84, 86, 65} is not a special sum set because 65 + 87 + 88 = 75 + 81 + 84, 
whereas {157, 150, 164, 119, 79, 159, 161, 139, 158} satisfies both rules for all possible subset 
pair combinations and S(A) = 1286.

Using sets.txt (right click and "Save Link/Target As..."), a 4K text file with one-hundred sets 
containing seven to twelve elements (the two examples given above are the first two sets in the file), 
identify all the special sum sets, A1, A2, ..., Ak, and find the value of S(A1) + S(A2) + ... + S(Ak).

NOTE: This problem is related to Problem 103 and Problem 106.
'''

# use https://github.com/hughdbrown/Project-Euler/blob/master/euler-105.py
# not intrested in this problem , skip it by using  hughdbrown solution

import time
from termcolor import colored


def powerset(s) :
    length = len(s)
    for i in range(1, 1 << length) :
        yield [c for j, c in enumerate(s) if (1 << j) & i]
    return


def isSpecialSet(s) :
    for i in range(1,1+int(len(s)/2) ):
        left, right = s[:i+1], s[-i:]
        if len(left) <= len(right) :
            break
        if sum(left) <= sum(right) :
            print(left, right)
            return False
    sset = set(s)
    for a in powerset(s) :
        diff = sset - set(a)
        suma = sum(a)
        for b in powerset(diff) :
            if suma == sum(b) :
                print(suma, sorted(a), sorted(b))
                return False    
    return True


def main_process():
    total = 0
    with open("i105sets.txt") as f :
        for line in f :

            a = sorted(int(d) for d in line.strip().split(","))
            if isSpecialSet(a) :
                #print "Special: ", a
                total += sum(a)
            else :
                print("Not special: ", a)
    print('#'*10, total)



if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)