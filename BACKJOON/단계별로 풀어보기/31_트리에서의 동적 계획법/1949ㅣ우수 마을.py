import sys


def search(para_node):  # DFS, 깊이 우선 탐색
    list_visit[para_node] = True
    table_dp[para_node][0] = list_population[para_node]

    for f_node in graph_n[para_node]:
        if not list_visit[f_node]:
            search(f_node)
            table_dp[para_node][0] += table_dp[f_node][1]
            table_dp[para_node][1] += max(table_dp[f_node][0], table_dp[f_node][1])


if __name__ == '__main__':
    MAX = int(1e4) + 1
    sys.setrecursionlimit(10 ** 5)

    in_n = int(sys.stdin.readline())
    list_population = [0] + list(map(int, sys.stdin.readline().split()))

    graph_n = [[] for _ in range(MAX)]
    for _ in range(in_n - 1):
        in_v1, in_v2 = map(int, sys.stdin.readline().split())
        graph_n[in_v1].append(in_v2)
        graph_n[in_v2].append(in_v1)

    list_visit = [False] * MAX
    table_dp = [[0, 0] for _ in range(MAX)]
    search(1)

    out_1 = max(table_dp[1][0], table_dp[1][1])
    print(out_1)
