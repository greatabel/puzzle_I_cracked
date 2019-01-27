from collections import deque

def find_shortest_path(start, graph):
    ""
    
# https://docs.python.org/3/library/collections.html#collections.deque
def main_process():
    d = deque('ghi')
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


if __name__ == "__main__":
    main_process()