import sys
import heapq


INF = sys.maxsize

in_v, in_e = map(int, sys.stdin.readline().split())
in_start = int(sys.stdin.readline())
graph_v = [[] for _ in range(in_v + 1)]
for _ in range(in_e):
    start_v, end_v, cost_v = map(int, sys.stdin.readline().split())
    graph_v[start_v].append((cost_v, end_v))

table_dp = [INF] * (in_v + 1)
heap_v = []


def dijkstra(para_start):
    table_dp[para_start] = 0
    heapq.heappush(heap_v, (0, para_start))

    while heap_v:
        temp_cost, temp_node = heapq.heappop(heap_v)
        if table_dp[temp_node] < temp_cost:
            continue

        for cost, next_node in graph_v[temp_node]:
            next_cost = cost + temp_cost
            if next_cost < table_dp[next_node]:
                table_dp[next_node] = next_cost
                heapq.heappush(heap_v, (next_cost, next_node))


dijkstra(in_start)

for v in range(1, in_v + 1):
    print("INF" if table_dp[v] == INF else table_dp[v])
