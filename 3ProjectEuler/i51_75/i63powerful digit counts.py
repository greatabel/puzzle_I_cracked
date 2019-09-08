# Powerful digit counts
# Problem 63
# The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.

# How many n-digit positive integers exist which are also an nth power?





import time
from termcolor import colored
from math import pow

def main_process():
    count = 0
    for i in range(1,100):
        for j in range(1,50):
            test = int(pow(i,j))
            if len(str(test)) == j:
                print(test,j)
                count += 1
            if len(str(test)) > j:
                break
        # print("i:",i)


    print(colored('mycount=', 'red'), count)

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)