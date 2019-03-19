import time
from termcolor import colored


def main_process():
    a = list(range(1, 5))
    b = a[:]
    c = a
    print('a=', a,'a[:]=', b, c)
    a.append(60)
    print('a=', a,'a[:]=', b, c)
    b[0] = 1000
    print('a=', a,'a[:]=', b, c)
    c[1] = 20000
    print('a=', a,'a[:]=', b, c)

    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)