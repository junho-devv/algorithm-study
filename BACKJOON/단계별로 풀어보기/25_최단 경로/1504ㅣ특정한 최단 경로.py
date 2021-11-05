import sys
import heapq


INF = sys.maxsize

in_n, in_e = map(int, sys.stdin.readline().split())
graph_n = [[] for _ in range(in_n + 1)]
for _ in range(in_e):
    start_e, end_e, cost_e = map(int, sys.stdin.readline().split())
    graph_n[start_e].append((cost_e, end_e))
    graph_n[end_e].append((cost_e, start_e))
in_v1, in_v2 = map(int, sys.stdin.readline().split())


def dijkstra(para_start):
    table_dp = [INF] * (in_n + 1)
    table_dp[para_start] = 0

    heap_n = []
    heapq.heappush(heap_n, (0, para_start))

    while heap_n:
        temp_cost, temp_node = heapq.heappop(heap_n)
        if table_dp[temp_node] < temp_cost:
            continue

        for cost, next_node in graph_n[temp_node]:
            next_cost = cost + temp_cost
            if next_cost < table_dp[next_node]:
                table_dp[next_node] = next_cost
                heapq.heappush(heap_n, (next_cost, next_node))

    return table_dp


dp_start = dijkstra(1)
dp_v1 = dijkstra(in_v1)
dp_v2 = dijkstra(in_v2)

answer = min(dp_start[in_v1] + dp_v1[in_v2] + dp_v2[in_n], dp_start[in_v2] + dp_v2[in_v1] + dp_v1[in_n])
print(answer if answer < INF else -1)
