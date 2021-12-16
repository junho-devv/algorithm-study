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
            temp_1, temp_2 = god_n[_1], god_n[_2]
            if find(_1 + 1) != find(_2 + 1):
                temp_dist = ((temp_1[0] - temp_2[0]) ** 2 + (temp_1[1] - temp_2[1]) ** 2) ** 0.5
                dist_n.append([temp_1, temp_2, temp_dist])
    dist_n.sort(key=lambda _: _[2])

    parent_node = [_ for _ in range(in_n + 1)]
    for _ in range(in_m):
        in_a, in_b = map(int, sys.stdin.readline().split())
        union(in_a, in_b)

