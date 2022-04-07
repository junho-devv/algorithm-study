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
    in_n = int(sys.stdin.readline())
    in_m = int(sys.stdin.readline())

    parent_node = [n for n in range(in_n)]
    for i in range(in_n):
        city_map = list(map(int, sys.stdin.readline().split()))
        for j in range(in_n):
            if city_map[j] == 1:
                union(i, j)

    city_travel = list(map(int, sys.stdin.readline().split()))

    out_travel = set([find(i - 1) for i in city_travel])
    if len(out_travel) == 1:
        print("YES")
    else:
        print("NO")

