'''
加法链：https://en.wikipedia.org/wiki/Addition_chain

在数学中，用于计算正整数n的加法链可以由自然数V的序列和索引对w的序列给出，
使得v中的每个项是两个先前项的和，这些项的索引被指定 由w：
V =(V0,...,Vs), with V0 = 1 and Vs = n
for each 0< i ≤ s holds: Vi = Vj + Vk, with wi=(j,k) and 0 ≤ j,k ≤ i − 1


加法链阶乘: https://en.wikipedia.org/wiki/Addition-chain_exponentiation

'''


import time
from termcolor import colored


def addtion_chain_demo(V):
    dic = {}
    
    for vi in V:
        for a in V:
            for b in V:
                if (vi not in dic) and vi == a + b:
                    print(vi, ' = ', a, '+', b)
                    dic[vi] = (a, b)
    return dic

def addition_chain_exponentiation(base, exp_num, d):
    for key, value in d.items():
        print('5^' , key, '=', '5^', value[0], ' X ', '5^', value[1])

def main_process():
    V = (1,2,3,6,12,24,30,31) 
    addition_dic = addtion_chain_demo(V)
    addition_chain_exponentiation(5, 31, addition_dic)
    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)