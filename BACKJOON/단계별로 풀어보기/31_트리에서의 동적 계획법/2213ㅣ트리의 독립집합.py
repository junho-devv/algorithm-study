import sys


if __name__ == '__main__':
    in_n = int(sys.stdin.readline())
    in_w = list(map(int, sys.stdin.readline().split()))

    tree_n = [[] for _ in range(in_n + 1)]
    for _ in range(in_n - 1):
        in_a, in_b = map(int, sys.stdin.readline().split())
        tree_n[in_a].append(in_b)
        tree_n[in_b].append(in_a)




