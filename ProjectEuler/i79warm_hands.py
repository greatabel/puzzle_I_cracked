import time
from termcolor import colored


def main_process():
    adjacent_points = {}
    inputs = ['319', '680', '180']
    for item in inputs:
        for index,ch in enumerate(item):
            print(index, ch, item[index+1:])
        print('\n')


    print(colored('mycount=', 'red'))

if __name__ == "__main__":
    main_process()