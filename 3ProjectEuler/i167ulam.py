'''

Investigating Ulam sequences

Problem 167
For two positive integers a and b, the Ulam sequence U(a,b) is defined by U(a,b)1 = a,

 U(a,b)2 = b and for k > 2, U(a,b)k is the smallest integer greater than U(a,b)(k-1) 

 which can be written in exactly one way as the sum of two distinct previous members of U(a,b).

For example, the sequence U(1,2) begins with
1, 2, 3 = 1 + 2, 4 = 1 + 3, 6 = 2 + 4, 8 = 2 + 6, 11 = 3 + 8;
5 does not belong to it because 5 = 1 + 4 = 2 + 3 has two representations as the sum of two previous members, 

likewise 7 = 1 + 6 = 3 + 4.

Find ∑U(2,2n+1)k for 2 ≤ n ≤10, where k = 1011.

#----------------------------#

乌拉姆序列研究

任取两个正整数a和b，乌拉姆序列U(a,b)按如下方式定义：U(a,b)1 = a，U(a,b)2 = b，

对于k > 2，U(a,b)k是比U(a,b)(k-1)更大，且存在用U(a,b)之前的这些项中的不同两项之和唯一表示的最小整数。

例如，序列U(1,2)的开头部分如下所示
1, 2, 3 = 1 + 2, 4 = 1 + 3, 6 = 2 + 4, 8 = 2 + 6, 11 = 3 + 8;
5不在这个序列是，因为5 = 1 + 4 = 2 + 3，有两种表示方法，同样地7也是如此因为7 = 1 + 6 = 3 + 4。

对于2 ≤ n ≤10，求∑U(2,2n+1)k，其中k = 1011.

#----------------------------#

use solution from :

http://dreslan.blogspot.com/2014/05/project-euler-problem-167.html 

'''




import time
from termcolor import colored

def answer():
    sum = getUlam(5,10**11)
    i = 7
    while i <=21:
        sum += getUlam(i, 10**11)
        i+=2
    return sum

def getUlam(y,k):
    #ulam = (period, constant difference, ([seqbeginning], [repeated sequece]))
    ulam = getUlam2(y)
    if k <= len(ulam[2][0]):
        return ulam[2][0][k-1]
    shift = k - len(ulam[2][0])
    remainder = shift % ulam[0]
    #doesn't work for some reason when remainder = 0
    if remainder == 0:
        remainder = len(ulam[2][1])
    return ulam[2][1][remainder-1] + (shift - remainder)*ulam[1]/ulam[0]

def getUlam2(y):
    p, seq = get_Period_First_Difference(2,y)
    repeatedSeq = get_Repeated_Sequence(p, seq)
    firstDifference = get_First_Difference(p, seq)
    return p, firstDifference, repeatedSeq

def get_Repeated_Sequence(period, seq):
    evenIndex = find_even(seq, 2)
    return seq[:evenIndex+1], seq[evenIndex+1:evenIndex + period + 1]

def get_First_Difference(period, seq):
    evenIndex = find_even(seq, 2)
    return seq[evenIndex+1+period] - seq[evenIndex+1]

def get_Period_First_Difference(x,y):
    if x != 2 or y < 5:
        return ["No period exists."], seq
    
    n = 100
    p = 0
    evenIndex = 0
    
    while True:
        seq = ulam2(y,n)
        evenIndex = find_even(seq, 2)
        seqDiff = format_sequence(seq)[evenIndex+1:]
        p = period(seqDiff)
        if p:
            return p, seq
        n*=10
        #play with the line below to change time out length
        if n >= 100000000:
            break
    return ["No period found. Try increasing timeout."], seq

def ulam2(y,length):
    #sequence, candidates, even index, index - 1 of largest term so far
    seq, cand, evenIndex, n = nextEven([2,y,2+y])
    while n < length:
        cand.append(seq[0]+seq[n-1])
        cand.append(seq[evenIndex]+seq[n-1])
        cand.sort()
        #since list is sorted, only need beginning of list
        while cand[0] in cand[1:2]:
            temp = cand[0]
            cand.pop(0)
            cand.pop(0)
            if cand[0] == temp and cand[0] != cand[1]:
                cand.pop(0)
        seq.append(cand[0])
        cand.pop(0)
        n+=1
    return seq

def nextEven(seq):
    cand = []
    n = len(seq)
    #want to generate 1 beyond the 2nd even, thus n-2
    while seq[n-2] % 2 or n-2 == 0:
        i = 0
        for e in seq[:n-1]:
            cand.append(e+seq[n-1])
        cand.sort()
        #since list is sorted, only need to check first 2 terms
        while cand[0] in cand[1:2]:
            temp = cand[0]
            cand.pop(0)
            cand.pop(0)
            if cand[0] == temp and cand[0] != cand[1]:
                cand.pop(0)
        seq.append(cand[0])
        cand.pop(0)
        n+=1
    #now we get rid of even candidates
    i = 0
    while i < len(cand):
        if cand[i] % 2 == 0:
            cand.pop(i)
        else: i+=1
    return seq, cand, n-2,n

def format_sequence(sequence):
    formatted_sequence = []
    previous = sequence[0]
    for e in sequence[1:]:
        formatted_sequence.append(e-previous)
        #current e becomes previous e next iteration
        previous = e
    return formatted_sequence

def period(seq):
    unique = []
    last = 0
    for index, e in enumerate(seq):
        if e not in unique:
            unique.append(e)
            last = index
    #this is the smallest sequence that captures all unique values
    minPattern = seq[:last]
    
    #is the sequence long enough to test for a repeat?
    if len(seq) < 2*len(minPattern):
        return []
    
    minPattern = seq[:last]
    for index, e in enumerate(seq[last:]):
        if e == minPattern[0] and seq[last+index:last+index+len(minPattern)] == minPattern:
            return len(seq[:last+index])
    return []

#returns the index of the nth even number
def find_even(seq, n):
    for index, e in enumerate(seq):
        if e % 2 == 0 and e != 0:
            n-=1
            if n == 0:
                return index
    return []

def main_process():
    results = answer()
    print(colored('mycount=', 'red'), int(results))
    # 3916160068885

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





