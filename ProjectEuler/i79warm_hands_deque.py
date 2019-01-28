from collections import deque
from i79warm_hands import create_adjacent



    
# https://docs.python.org/3/library/collections.html#collections.deque
def main_process():
    d = deque('abcdefghi')
    for elem in d:
        print(elem)
    print('d=', d)
    d.append('j')
    d.append('k')
    print('d=', d)

    pop = d.pop()
    print('pop=', pop)
    popleft = d.popleft()
    print('popleft=', popleft)
    print('d=', d)
    print(list(reversed(d)))
    graph = create_adjacent()
    find_shortest_path(1, graph)


if __name__ == "__main__":
    main_process()