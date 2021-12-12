import sys


def find(para_node):
    if parent_node[para_node] != para_node:
        parent_node[para_node] = find(parent_node[para_node])

    return parent_node[para_node]


def union(para_a, para_b):
    root_a, root_b = find(para_a), find(para_b)
    if root_a > root_b:
        root_a, root_b = root_b, root_a

    parent_node[root_b] = root_a


if __name__ == '__main__':
    in_n, in_m = map(int, sys.stdin.readline().split())

    parent_node = [n for n in range(in_n)]
    out_turn = []
    for m in range(in_m):
        in_a, in_b = map(int, sys.stdin.readline().split())

        if find(in_a) == find(in_b):
            out_turn.append(m + 1)

        union(in_a, in_b)

    if not out_turn:
        print(0)
    else:
        print(out_turn[0])
