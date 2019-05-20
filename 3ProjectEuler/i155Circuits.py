'''



#----------------------------#



'''




import time
from termcolor import colored

import math



    
def main_process():
    SIZE = 18
    # possible[i] holds all the possible capacitance values of a series/parallel
    # capacitor network that uses exactly i capacitors of 60 uF each
    possible = []
    all = set()  # Union of every possible[i]
    # Note: Each fraction is represented as a pair (num, den), where den > 0 and gcd(num, den) = 1.

    possible.append(set())
    possible.append({(60, 1)})
    all.update(possible[1])
    for i in range(2, SIZE + 1):
        poss = set()
        for j in range(1, i // 2 + 1):
            for (n0, d0) in possible[j]:
                for (n1, d1) in possible[i - j]:
                    pseudosum = n0 * d1 + n1 * d0
                    numerprod = n0 * n1
                    denomprod = d0 * d1
                    npgcd = math.gcd(pseudosum, numerprod)
                    dpgcd = math.gcd(pseudosum, denomprod)
                    poss.add((pseudosum // dpgcd, denomprod // dpgcd))  # Parallel
                    poss.add((numerprod // npgcd, pseudosum // npgcd))  # Series
        possible.append(poss)
        all.update(poss)

    print(colored('mycount=', 'red'), len(all))
#     mycount= 3857447
# time= 27.831167999999998

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





