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


def all_chains(x):
    if x <= 0:
        return [[]]
    if x == 1:
        return [[1]]
    if x == 2:
        return [[1, 2]]

    res = []
    arr = [[1, 2]]
    while (1):
        temp = []
        if arr == []:
            return res
        print('arr=', arr)
        for i in arr:
            print('i=', i)
            for j in i:
                print(colored(' 路径中其中一项的j=', 'green', attrs=['reverse', 'blink', 'bold']), j)
                p = i[:]
                print(' p=', p, 'i[最后一项]=', i[-1], 'i[最后一项]+路径中其中一项的j =', i[-1]+j)
                p.append(i[-1]+j)
                print(colored('新的路径p=','red'), p, 'p[最后一项]=', p[-1], '目标x=', x)
                if p[-1] == x:
                    print('中奖了', '一条达到目标的路径集合res=',res, ' 添加路径 ', p)
                    res.append(p)
                elif p[-1] < x:
                    print(' 新的路径p[最后一项]=', p[-1], '小于目标x=', x,'临时路径temp:', temp, '添加新路径p:', p)
                    temp.append(p)
                    print('之后的temp:', temp)
        arr = temp[:]
        print(colored('设置 arr 替换为 temp[:] arr变成=>', 'blue'), arr, '\n\n')

# def addtion_chain_demo(V):
#     dic = {}
    
#     for vi in V:
#         for a in V:
#             for b in V:
#                 if (vi not in dic) and vi == a + b:
#                     print(vi, ' = ', a, '+', b)
#                     dic[vi] = (a, b)
#     return dic

# def addition_chain_exponentiation(base, exp_num, d):
#     for key, value in d.items():
#         print('5^' , key, '=', '5^', value[0], ' X ', '5^', value[1])

def main_process():
    # V = (1,2,3,6,12,24,30,31) 
    # addition_dic = addtion_chain_demo(V)
    # addition_chain_exponentiation(5, 31, addition_dic)
    print(colored('mycount=', 'red'), 'results')

    t = all_chains(5)
    print(t)

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)