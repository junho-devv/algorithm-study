import sys


def find(para_node):
    if parent[para_node] == para_node:
        parent[para_node] = find(parent[para_node])

    return parent[para_node]


def union(para_a, para_b):

    return


if __name__ == '__main__':
    in_tc = int(sys.stdin.readline())
    for _ in range(in_tc):
        in_f = int(sys.stdin.readline())
        for _ in range(in_f):
            in_a, in_b = map(int, sys.stdin.readline().split())
            if