'''
For a number written in Roman numerals to be considered valid there are basic rules which must be followed. 
Even though the rules allow some numbers to be expressed in more than one way there is always a 
"best" way of writing a particular number.

For example, it would appear that there are at least six ways of writing the number sixteen:

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

However, according to the rules only XIIIIII and XVI are valid, and the last example is considered to be 
the most efficient, as it uses the least number of numerals.

The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one thousand numbers written 
in valid, but not necessarily minimal, Roman numerals; see About... Roman Numerals for the definitive rules 
for this problem.

Find the number of characters saved by writing each of these in their minimal form.

Note: You can assume that all the Roman numerals in the file contain no more than four consecutive identical units.
'''


import time
from termcolor import colored

def subtractive(roman):
    result = roman
    replacements = [
        ("VIIII", "IX"), 
        ("IIII", "IV"), 
        ("LXXXX", "XC"), 
        ("XXXX", "XL"),
        ("DCCCC", "CM"), 
        ("CCCC", "CD"),
    ]
    for old, new in replacements:
        result = result.replace(old, new)
    return result

def main_process():
    current = 0
    improved = 0
    myfile = open('i89_roman.txt').read()
    for line in myfile.split('\n'):
        if line and line != '':
            roman = line.strip()
            current += len(roman)
            improved += len(subtractive(roman))
    print(colored('mycount=', 'red'), current - improved)

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)