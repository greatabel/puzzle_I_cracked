'''
The most naive way of computing ^15 requires fourteen multiplications:

n × n × ... × n = n^15

But using a "binary" method you can compute it in six multiplications:

n × n = n^2
n2 × n2 = n^4
n4 × n4 = n^8
n8 × n4 = n^12
n12 × n2 = n^14
n14 × n = n^15

However it is yet possible to compute it in only five multiplications:

n × n = n^2
n2 × n = n^3
n3 × n3 = n^6
n6 × n6 = n^12
n12 × n3 = n^15

We shall define m(k) to be the minimum number of multiplications to compute nk; for example m(15) = 5.

For 1 ≤ k ≤ 200, find ∑ m(k).
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