import time
from termcolor import colored
from collections import defaultdict, deque


def create_adjacent():
    adjacent_points = defaultdict(set)
    inputs = ['319', '680', '180', '690']
    for item in inputs:
        for index,ch in enumerate(item):
            adjacents = [int(i) for i in item[index+1:]]
            if adjacents != []:
                if int(ch) not in adjacent_points:
                    adjacent_points[int(ch)] = set(adjacents)
                else:
                    adjacent_points[int(ch)] = adjacent_points[int(ch)].union(set(adjacents))
                    # adjacent_points[int(ch)] = adjacent_points[int(ch)] + \
                    #     list(set(adjacents) - set(adjacent_points[int(ch)]))
            # print('index=', index, 'ch=', ch, 'adjacents=', adjacents)
    print(adjacent_points)
    return adjacent_points    


def main_process():
    create_adjacent()
    print(colored('mycount=', 'red'))

if __name__ == "__main__":
    main_process()