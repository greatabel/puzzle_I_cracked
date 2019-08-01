'''

Problem 162 Hexadecimal numbers

In the hexadecimal number system numbers are represented using 16 different digits:

0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F
The hexadecimal number AF when written in the decimal number system equals 10x16+15=175.

In the 3-digit hexadecimal numbers 10A, 1A0, A10, and A01 the digits 0,1 and A are all present.
Like numbers written in base ten we write hexadecimal numbers without leading zeroes.

How many hexadecimal numbers containing at most sixteen hexadecimal digits exist with all of the digits 0,1, 

and A present at least once?
Give your answer as a hexadecimal number.

(A,B,C,D,E and F in upper case, without any leading or trailing code 

that marks the number as hexadecimal and without leading zeroes , 

e.g. 1A3F and not: 1a3f and not 0x1a3f and not $1A3F and not #1A3F and not 0000001A3F)

#----------------------------#

欧拉项目162: 十六进制数

十六进制数系统使用16个不同的数字：

0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F
十六进制数AF在十进制下等于10x16+15=175。

三位十六进制数10A，1A0，A10和A01都包含数字0，1和A。
和十进制下一样，在十六进制中没有前导零。

有多少至多十六位的十六进制数同时包含0，1和A？
用十六进制数表示你的答案。

（A,B,C,D,E和F均为大写字母，没有前导零或末尾标识符来表明该数字为十六进制，

例如，1A3F不能写成:1a3f或0x1a3f或$1A3F或#1A3F或0000001A3F）

#----------------------------#


'''


from itertools import permutations
import time
from termcolor import colored

def observe_pattern():
    perms = [''.join(p) for p in permutations('0123456789ABCDEF', 3)]
    print(len(perms), '###', perms[:50])

def main_process():
    observe_pattern()
    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





