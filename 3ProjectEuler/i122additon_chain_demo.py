'''
加法链：https://en.wikipedia.org/wiki/Addition_chain

在数学中，用于计算正整数n的加法链可以由自然数V的序列和索引对w的序列给出，
使得v中的每个项是两个先前项的和，这些项的索引被指定 由w：
V =(V0,...,Vs), with V0 = 1 and Vs = n
for each 0< i ≤ s holds: Vi = Vj + Vk, with wi=(j,k) and 0 ≤ j,k ≤ i − 1

'''


import time
from termcolor import colored


def main_process():

    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)