import sys


def search(para_node, para_cnt):
    visit_n[para_node] = True
    for node in tree_n[para_node]:
        if not visit_n[node]:
            para_cnt = search(node, para_cnt + 1)

    return para_cnt


if __name__ == '__main__':
    in_tc = int(sys.stdin.readline())
    for _ in range(in_tc):
        in_n, in_m = map(int, sys.stdin.readline().split())

        tree_n = [[] for _ in range(in_n + 1)]
        for _ in range(in_m):
            in_a, in_b = map(int, sys.stdin.readline().split())
            tree_n[in_a].append(in_b)
            tree_n[in_b].append(in_a)

        visit_n = [False] * (in_n + 1)
        out_min = search(1, 0)
        print(out_min)
