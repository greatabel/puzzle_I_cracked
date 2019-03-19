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
        for i in arr:
            print('\ni=', i)
            for j in i:
                print(colored(' j=', 'green', attrs=['reverse', 'blink', 'bold']), j)
                p = i[:]
                print(' p=', p, 'i[-1]=', i[-1], 'i[-1]+j =', i[-1]+j)
                p.append(i[-1]+j)
                print(colored('#','red'),'     p=', p, 'p[-1]=', p[-1], 'x=', x)
                if p[-1] == x:
                    print('中奖了', 'res=',res, '添加', p)
                    res.append(p)
                elif p[-1] < x:
                    print(' p[-1]=', p[-1], '<  x=', x,' temp', temp)
                    temp.append(p)
                    print(' p=',p, 'temp=', temp)
        arr = temp[:]
        print('设置 arr = temp[:] ==>', arr, temp[:])

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

    t = all_chains(4)
    print(t)

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)