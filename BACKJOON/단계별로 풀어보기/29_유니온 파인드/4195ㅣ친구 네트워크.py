import sys


def find(para_node):
    if parent[para_node] != para_node:
        parent[para_node] = find(parent[para_node])

    return parent[para_node]


def union(para_a, para_b):
    root_a, root_b = find(para_a), find(para_b)
    if root_a != root_b:
        parent[root_b] = root_a
        friend[root_a] += friend[root_b]


if __name__ == '__main__':
    in_tc = int(sys.stdin.readline())
    for _ in range(in_tc):
        in_f = int(sys.stdin.readline())

        parent = dict()
        friend = dict()
        for _ in range(in_f):
            in_a, in_b = map(str, sys.stdin.readline().split())
            if in_a not in parent:
                parent[in_a] = in_a
                friend[in_a] = 1
            if in_b not in parent:
                parent[in_b] = in_b
                friend[in_b] = 1

            union(in_a, in_b)

            out_friends = friend[find(in_a)]
            print(out_friends)
