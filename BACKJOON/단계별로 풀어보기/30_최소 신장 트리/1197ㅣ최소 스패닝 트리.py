import sys


if __name__ == '__main__':
    in_v, in_e = map(int, sys.stdin.readline().split())

    tree_n = [[] for _ in range(in_v + 1)]
    for _ in range(in_e):
        in_a, in_b, in_c = map(int, sys.stdin.readline().split())
        tree_n.append()