import sys


def find(para_node):
    if parent_node[para_node] != para_node:
        parent_node[para_node] = find(parent_node[para_node])

    return parent_node[para_node]


def union(para_node_1, para_node_2):
    root_1, root_2 = find(para_node_1), find(para_node_2)
    if root_1 > root_2:
        root_1, root_2 = root_2, root_1

    parent_node[root_2] = root_1


if __name__ == '__main__':
    in_n, in_m = map(int, sys.stdin.readline().split())

    god_n = []
    for _ in range(in_n):
        in_a, in_b = map(int, sys.stdin.readline().split())
        god_n.append((in_a, in_b))

    dist_n = []
    for _1 in range(in_n):
        for _2 in range(_1 + 1, in_n):
            if find(_1) != find(_2):
                dist_n

    parent_node = [_ for _ in range(in_n + 1)]
    for _ in range(in_m):
        in_a, in_b = map(int, sys.stdin.readline().split())
        union(in_a, in_b)