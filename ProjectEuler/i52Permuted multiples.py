# Permuted multiples
# Problem 52
# It can be seen that the number, 125874, and its double, 251748, 

# contain exactly the same digits, but in a different order.

# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.




import time
from termcolor import colored

def get_digital(number):
    results = []
    if number == 0:
        results = [0]
    while number > 0:
        result = number % 10
        number = number // 10
        results.append(result)
    # print('results=', results)
    return results

def condition(number):
    L  = []
    for i in range(1,7):
        tmp = get_digital(number * i)
        tmp.sort()
        L.append(tmp)
        print('tmp=',tmp)
    if all(x == L[0] for x in L):
        print(L)
        return True




def main_process():
    flag = True
    i = 1
    while flag:
        if condition(i):
            flag = False
        else:
            flag = True
        i += 1
        print('i=',i)

    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)