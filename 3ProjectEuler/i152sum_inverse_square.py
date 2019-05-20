'''

There are several ways to write the number 1/2 as a sum of inverse squares using distinct integers.

For instance, the numbers {2,3,4,5,7,12,15,20,28,35} can be used:

12=122+132+142+152+172+1122+1152+1202+1282+1352
In fact, only using integers between 2 and 45 inclusive, there are exactly three ways to do it, 

the remaining two being: {2,3,4,6,7,9,10,20,28,35,36,45} and {2,3,4,6,7,9,12,15,28,30,35,36,45}.

How many ways are there to write the number 1/2 as a sum of inverse squares using distinct integers 

between 2 and 80 inclusive?

#----------------------------#

欧拉工程152: 将1/2写成平方数的倒数和

有许多种方式将1/2写成一系列不同整数的平方的倒数和。

例如，可以用这些数{2,3,4,5,7,12,15,20,28,35}：


事实上，只用2至45之间的数的方式一共有三种，另两种分别是：{2,3,4,6,7,9,10,20,28,35,36,45}和

{2,3,4,6,7,9,12,15,28,30,35,36,45}。

如果只用2至80之间的数，将1/2写成不同整数的平方的倒数和共有多少种方式？

#----------------------------#
跳过，使用其他人方案
'''



import time
from termcolor import colored


set_of_numbers = [2,3,4,5,6, 7,8,9,10,12, 14,15,16,18,20, 21,24,25,27,28, 
                30,32,35,36,40, 42,45,48,49,50, 54,56,60,63,64, 70,72,75,80]
##set_of_numbers = [2,3,4,5,6, 7,9,10,12, 15,20, 28, 30,35,36,40, 45] ##,48,49,50, 54,56,60,63,64, 70,72,75,80]
lcm = 4480842240000
inverses = [ lcm/(x*x) for x in set_of_numbers ]
half = lcm/2

residuals = [ sum(inverses[i: -1]) for i in range(len(inverses)) ]

def searchNextInverse (startIndex, remainder) :
    for k in range(startIndex, len(inverses)) :
        if remainder >= inverses[k] :
            return k
    else :
        return -1
    
def real_numbers(x) :
    return [ set_of_numbers[j] for j in x ]

def find(remainder, start_index, factors) :
    if remainder == 0 :
        yield factors
    else :
        ##print real_numbers(factors), set_of_numbers[start_index], remainder
        ##start_index = max(j for j in range(start_index, len(inverses)) if remainder >= inverses[j] )
        for j in range(start_index, len(inverses)) :
            ##print set_of_numbers[j]
            new_remainder = remainder - inverses[j]
            if (new_remainder >= 0) :
                new_factors = factors + [j]
                
                for factors_found in find(new_remainder, j+1, new_factors) :
                    yield factors_found
            elif (remainder > residuals[j]) :
                ##print set_of_numbers[j], remainder, residuals[j], inverses[j]
                break
    return

def main_process() :
    tic = time.process_time()
    for i, x in enumerate(find(half, 0, [])) :
        
        print(i, real_numbers(x), time.process_time() - tic)
        # reuslt is 301

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)



