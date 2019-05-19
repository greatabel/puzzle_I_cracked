'''

148 Exploring Pascal's triangle

We can easily verify that none of the entries in the first seven rows of Pascal's triangle are divisible by 7:

                         1
                     1       1
                 1       2       1
             1       3       3       1
         1       4       6       4       1
     1       5      10      10       5       1
1        6      15      20      15       6       1
However, if we check the first one hundred rows, we will find that only 2361 of the 5050

 entries are not divisible by 7.

Find the number of entries which are not divisible by 7 in the first one billion (109) rows of Pascal's triangle.

#----------------------------#



'''










import time
from termcolor import colored


def main_process():
    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)
