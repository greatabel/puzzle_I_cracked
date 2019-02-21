'''
By replacing each of the letters in the word CARE with 1, 2, 9, 
and 6 respectively, we form a square number: 1296 = 362. 
What is remarkable is that, by using the same digital substitutions, 
the anagram, RACE, also forms a square number: 9216 = 962. 
We shall call CARE (and RACE) a square anagram word pair and specify further
 that leading zeroes are not permitted, neither may a different letter 
 have the same digital value as another letter.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
 containing nearly two-thousand common English words, find all the square anagram word pairs
  (a palindromic word is NOT considered to be an anagram of itself).

What is the largest square number formed by any member of such a pair?

NOTE: All anagrams formed must be contained in the given text file.
'''

import time
from termcolor import colored
import itertools




def main_process():
    # file_url = "https://projecteuler.net/project/resources/p098_words.txt"
    def sq(n):
        x = int(''.join(y[letter_set[i]] for i in n))
        return x if int(x**0.5)**2 == x else False
    
    words = [(w[1:-1], sorted(w[1:-1])) 
        for w in open('i98words.txt').read().split(',') if len(w)>6]

    word_pairs = []
    while words:
        w = words.pop()
        word_pairs+= ((w[0], a[0]) for a in words if w[1] == a[1])

    max_sq = 0
    for w, a in word_pairs:
        letter_set = {x:y for y, x in enumerate(set(w))}
        for y in itertools.permutations('123456789', len(letter_set)):
            if sq(w) and sq(a): max_sq = max(sq(w), sq(a), max_sq)

    print(colored('mycount=', 'red'), max_sq)

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)