import sys


def find(para_node):
    if parent_node[para_node] != para_node:
        parent_node[para_node] = find(parent_node[para_node])

    return parent_node[para_node]


def union(para_n1, para_n2):
    root_n1, root_n2 = find(para_n1), find(para_n2)
    if root_n1 > root_n2:
        root_n1, root_n2 = root_n2, root_n1

    parent_node[root_n2] = root_n1


if __name__ == '__main__':
    # 크루스칼(Kruskal) 알고리즘을 이용한 풀이
    in_v, in_e = map(int, sys.stdin.readline().split())

    edge_e = []
    for _ in range(in_e):
        in_a, in_b, in_c = map(int, sys.stdin.readline().split())
        edge_e.append([in_a, in_b, in_c])
    edge_e.sort(key=lambda e: e[2])

    parent_node = [n for n in range(in_v + 1)]
    out_min = 0
    for a, b, c in edge_e:
        root_a, root_b = find(a), find(b)
        if root_a != root_b:
            union(a, b)
            out_min += c

    print(out_min)
