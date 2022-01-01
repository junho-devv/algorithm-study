import sys


def count(para_root):
    list_cnt[para_root] = 1
    for p_node in tree_n[para_root]:

        if list_cnt[p_node] == 0:
            count(p_node)
            list_cnt[para_root] += list_cnt[p_node]


if __name__ == '__main__':
    sys.setrecursionlimit(10 ** 9)

    in_n, in_r, in_q = map(int, sys.stdin.readline().split())
    tree_n = [[] for _ in range(in_n + 1)]
    list_cnt = [0] * (in_n + 1)

    for _ in range(in_n - 1):
        in_a, in_b = map(int, sys.stdin.readline().split())
        tree_n[in_a].append(in_b)
        tree_n[in_b].append(in_a)

    count(in_r)

    for _ in range(in_q):
        in_u = int(sys.stdin.readline())
        print(list_cnt[in_u])
