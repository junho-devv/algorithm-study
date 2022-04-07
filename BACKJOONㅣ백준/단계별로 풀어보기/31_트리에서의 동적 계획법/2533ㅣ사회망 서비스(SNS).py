import sys


def search(para_node): # depth first search
    list_visit[para_node] = True
    table_dp[para_node][0] = 1

    for f_ in graph_n[para_node]:
        if not list_visit[f_]:
            search(f_)
            table_dp[para_node][0] += min(table_dp[f_][0], table_dp[f_][1])
            table_dp[para_node][1] += table_dp[f_][0]


if __name__ == '__main__':
    sys.setrecursionlimit(10 ** 7)
    MAX = int(1e6) + 1

    in_n = int(sys.stdin.readline())

    graph_n = [[] for _ in range(MAX)]
    for _ in range(in_n - 1):
        in_e1, in_e2 = map(int, sys.stdin.readline().split())
        graph_n[in_e1].append(in_e2)
        graph_n[in_e2].append(in_e1)

    list_visit = [False] * (in_n + 1)
    table_dp = [[0, 0] for _ in range(in_n + 1)]
    search(1)

    out_1 = min(table_dp[1][0], table_dp[1][1])
    print(out_1)
