'''
The following undirected network consists of seven vertices and twelve edges with a total weight of 243.


The same network can be represented by the matrix below.

        A   B   C   D   E   F   G
A   -   16  12  21  -   -   -
B   16  -   -   17  20  -   -
C   12  -   -   28  -   31  -
D   21  17  28  -   18  19  23
E   -   20  -   18  -   -   11
F   -   -   31  19  -   -   27
G   -   -   -   23  11  27  -
However, it is possible to optimise the network by removing some edges and still ensure that 
all points on the network 
remain connected. The network which achieves the maximum saving is shown below. It has a weight of 93, 
representing a saving of 243 − 93 = 150 from the original network.


Using network.txt (right click and 'Save Link/Target As...'), a 6K text file containing a network 
with forty vertices, and given in matrix form, find the maximum saving which can be achieved by removing 
redundant edges whilst ensuring that the network remains connected.
'''

import time
from termcolor import colored

# use https://github.com/LaurentMazare/ProjectEuler/blob/master/e107.py solution, not intrested in this problem
def main_process():
    """Minimal network"""

    # Constants
    NETWORK_URL = 'i107network.txt'

    edges = []
    total_weight = 0
    num_vertices = 0
    for i, line in enumerate(open(NETWORK_URL)):
        num_vertices += 1
        for j, weight in enumerate(line.rstrip().split(',')):
            if weight == '-':
                continue
            if i >= j:
                continue
            total_weight += int(weight)
            edges.append([int(weight), i, j])
    edges = sorted(edges)

    graph = {}
    minimum_weight = 0
    for edge in edges:
        weight, node1, node2 = edge

        undiscovered = set(range(num_vertices))
        s = [node1]
        while len(s):
            v = s.pop()
            if v in undiscovered:
                undiscovered.remove(v)
                if v in graph:
                    try:
                        nodes = graph[v].iterkeys()
                    except AttributeError:
                        nodes = graph[v].keys()
                    s.extend(nodes)
        if node2 in undiscovered:
            if node1 not in graph:
                graph[node1] = {}
            graph[node1][node2] = weight
            if node2 not in graph:
                graph[node2] = {}
            graph[node2][node1] = weight
            minimum_weight += weight

    print(colored('mycount=', 'red'), total_weight - minimum_weight)

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)