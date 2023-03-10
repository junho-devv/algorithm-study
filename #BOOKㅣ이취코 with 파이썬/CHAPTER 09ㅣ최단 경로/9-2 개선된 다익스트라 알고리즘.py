import heapq
import sys


INF = int(1e9)

in_n, in_m = map(int, sys.stdin.readline().split())
in_s = int(sys.stdin.readline())

graph = [[] for _ in range(in_n + 1)]
distance = [INF] * (in_n + 1)

for _ in range(in_m):
    in_n1, in_n2, in_c = map(int, sys.stdin.readline().split())
    graph[in_n1].append((in_n2, in_c))


def dijkstra(start_node):

    que = list()
    heapq.heappush(que, (0, start_node))
    distance[start_node] = 0

    while que:

        min_d, now_node = heapq.heappop(que)

        if distance[now_node] < min_d:
            continue

        for node, cost in graph[now_node]:
            cost += min_d
            if cost < distance[node]:
                distance[node] = cost
                heapq.heappush(que, (cost, node))


dijkstra(in_s)

for n in range(1, in_n + 1):
    if distance[n] == INF:
        print("INFINITY")
    else:
        print(distance[n])
