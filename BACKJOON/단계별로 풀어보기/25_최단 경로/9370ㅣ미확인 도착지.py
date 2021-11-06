import sys
import heapq


INF = sys.maxsize


def dijkstra(para_start):
    table_dp = [INF] * (in_n + 1)
    table_dp[para_start] = 0

    heap_n = []
    heapq.heappush(heap_n, (0, para_start))
    while heap_n:
        temp_cost, temp_node = heapq.heappop(heap_n)
        for cost, next_node in graph_n[temp_node]:
            next_cost = cost + temp_cost
            if next_cost < table_dp[next_node]:
                table_dp[next_node] = next_cost
                heapq.heappush(heap_n, (next_cost, next_node))

    return table_dp


in_tc = int(sys.stdin.readline())
for _ in range(in_tc):
    in_n, in_m, in_t = map(int, sys.stdin.readline().split())
    in_s, in_g, in_h = map(int, sys.stdin.readline().split())

    graph_n = [[] for _ in range(in_n + 1)]
    for _ in range(in_m):
        start_m, end_m, cost_m = map(int, sys.stdin.readline().split())
        graph_n[start_m].append((cost_m, end_m))
        graph_n[end_m].append((cost_m, start_m))

    answer = []
    for _ in range(in_t):
        goal = int(sys.stdin.readline())
        dp_s = dijkstra(in_s)
        dp_g = dijkstra(in_g)
        dp_h = dijkstra(in_h)

        if dp_s[goal] >= min(dp_s[in_g] + dp_g[in_h] + dp_h[goal], dp_s[in_h] + dp_h[in_g] + dp_g[goal]):
            answer.append(goal)

    answer.sort()
    print(*answer)

# 함수 한번 호출하는 방식의 풀이
# 참조 : https://ca.ramel.be/89