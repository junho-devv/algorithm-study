import sys
import heapq


def trace(para_dp):
    answer = [in_d]

    temp_node = in_d
    while para_dp[temp_node] != 0:
        answer.append(para_dp[temp_node])
        temp_node = para_dp[temp_node]

    answer.reverse()

    return answer


def dijkstra(para_start):
    dp_city = [INF] * MAX
    dp_city[para_start] = 0

    dp_prev = [INF] * MAX
    dp_prev[para_start] = 0

    heap_n = []
    heapq.heappush(heap_n, (0, para_start))

    while heap_n:
        temp_cost, temp_node = heapq.heappop(heap_n)
        if dp_city[temp_node] < temp_cost:
            continue

        for cost, next_node in graph_bus[temp_node]:
            next_cost = cost + temp_cost
            if next_cost < dp_city[next_node]:
                dp_city[next_node] = next_cost
                dp_prev[next_node] = temp_node
                heapq.heappush(heap_n, (next_cost, next_node))

    return dp_city, dp_prev


if __name__ == '__main__':
    INF = int(1e9)
    MAX = int(1e3) + 1

    in_n = int(sys.stdin.readline())
    in_m = int(sys.stdin.readline())

    graph_bus = [[] for _ in range(int(MAX))]
    for _ in range(in_m):
        in_a, in_b, in_c = map(int, sys.stdin.readline().split())
        graph_bus[in_a].append((in_c, in_b))

    in_s, in_d = map(int, sys.stdin.readline().split())

    dp_s, dp_p = dijkstra(in_s)
    out_1 = dp_s[in_d]
    out_2 = trace(dp_p)
    print(out_1)
    print(len(out_2))
    print(*out_2)
