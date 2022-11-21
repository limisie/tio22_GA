import numpy as np


def dimacs_to_adjacent_matrix(file):
    f = open(file, "r")
    nodes = 0
    am = None
    k = 0

    for line in f:
        line_temp = line.split(' ')

        if line_temp[0] == 'p':
            nodes = int(line_temp[2])
            am = np.zeros((nodes, nodes), dtype=np.int8)
            k = int(line_temp[5])
        if line_temp[0] == 'e':
            node1, node2 = int(line_temp[1]) - 1, int(line_temp[2]) - 1
            am[node1, node2] = 1
            am[node2, node1] = 1

    return nodes, am, k
