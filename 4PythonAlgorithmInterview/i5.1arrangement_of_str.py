'''

设计一个程序，当输入一个字符串，输出所有排列
例如abc，输出：a,b,c所有的pailie:abc,acb,bac,bca,cba,cab

#----------------------------#

参考：https://stackoverflow.com/questions/8306654/finding-all-possible-permutations-of-a-given-string-in-python


'''

import time
from termcolor import colored
from itertools import permutations


def default_way(str):
    permlist = permutations(str)
    for p in list(permlist):
        print(''.join(p))

def permutations(string):
    """Create all permutations of a string with non-repeating characters
    """
    permutation_list = []
    if len(string) == 1:
        return [string]
    else:
        for char in string:
            [permutation_list.append(char + a) for a in permutations(string.replace(char, ""))]
    return permutation_list

def main_process():
    str = 'abc'
    default_way(str)
    ps = permutations(str)
    print(ps)
    print(colored('mycount=', 'red'), 'results')


if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





