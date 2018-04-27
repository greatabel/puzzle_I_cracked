# Coded triangle numbers
# Problem 42
# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

# Using words.txt (right click and 'Save Link/Target As...'), 
# a 16K text file containing nearly two-thousand common English words, how many are triangle words?

import time
from termcolor import colored
# import copy

def getData(path):
    with open(path) as text_file:
        contents = text_file.read()
        mylist = [line.replace('"','') for line in contents.split(',')]
        mylist.sort()
        # thesum = 0
        # for idex, val in enumerate(mylist):
        #     print(val)
        #     val = val.replace('"','')
        return mylist

def ciculatevalue(i):
    isum = 0
    for ch in i:
        code = ord(ch) - ord('A') + 1
        isum += code
    return isum

def triangle_numbers(bound):
    return [int(i*(i+1)/2) for i in range(1,bound)]

def main_process(rows):
    triangles = triangle_numbers(21)
    print('triangle_numbers=',triangles)
    # imax = 0
    # maxvalue = ''
    mycount = 0
    for row in rows:
        value = ciculatevalue(row)
        if value in triangles:
            print(value)
            mycount += 1
    print(colored('mycount=', 'red'), mycount)
        # if value > imax:
        #     imax = value
        #     maxvalue = row

    # print(imax,maxvalue)
    # 192 RESPONSIBILITY

if __name__ == "__main__":
    tic = time.clock()
    rows = getData('i42_words.txt')
    print(len(rows))
    main_process(rows)

    toc = time.clock()
    print("time=",toc - tic)