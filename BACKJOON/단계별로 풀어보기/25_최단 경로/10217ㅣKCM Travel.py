import sys


INF = sys.maxsize


def dijkstra(para_start):
    table_dp[para_start][0] = 0

    for temp_cost in range(in_m + 1):
        for temp_node in range(1, in_n + 1):
            temp_time = table_dp[temp_node][temp_cost]
            if temp_time == INF:
                continue
            for next_node, cost, time in graph_n[temp_node]:
                next_cost = temp_cost + cost
                if next_cost > in_m:
                    continue

                table_dp[next_node][next_cost] = min(table_dp[next_node][next_cost], temp_time + time)

    return


in_tc = int(sys.stdin.readline())
for _ in range(in_tc):
    in_n, in_m, in_k = map(int, sys.stdin.readline().split())
    graph_n = [[] for _ in range(in_n + 1)]
    for _ in range(in_k):
        in_u, in_v, in_c, in_d = map(int, sys.stdin.readline().split())
        graph_n[in_u].append((in_v, in_c, in_d))

    table_dp = [[INF for _ in range(in_m + 1)] for _ in range(in_n + 1)]

    dijkstra(1)

    if min(table_dp[in_n]) == INF:
        print("Poor KCM")
    else:
        print(min(table_dp[in_n]))
