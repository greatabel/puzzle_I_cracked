# Square root convergents
# Problem 57
# It is possible to show that the square root of two can be expressed as an infinite continued fraction.

# √ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

# By expanding this for the first four iterations, we get:

# 1 + 1/2 = 3/2 = 1.5
# 1 + 1/(2 + 1/2) = 7/5 = 1.4
# 1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
# 1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

# The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, 
# is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

# In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?

import time
from termcolor import colored

# # We have \frac{3}{2},\frac{7}{5},\frac{17}{12},\frac{41}{29},\frac{99}{70},\frac{239}{169}…
#  n_{k+1} = n_k +  2d_k

#  d_{k+1} = n_k  + d_k

# n_{k +1} = n_k  +  2d_k
# d_{k +1} = n_{k 1} - d_k



def main_process(bound):
    count = 0
    ni = 3
    di = 2
    for i in range(0,bound):
        ni = ni + 2 * di
        di = ni - di
        print(ni,"/", di)
        if len(str(ni)) > len(str(di)):
            print("longer:",ni,"/", di)
            count += 1

    print(colored('mycount=', 'red'), count)

if __name__ == "__main__":
    tic = time.clock()
    
    main_process(1000)

    toc = time.clock()
    print("time=",toc - tic)