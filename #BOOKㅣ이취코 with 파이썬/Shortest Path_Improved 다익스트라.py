import heapq
import sys

INF = int(1e9)

node, line = map(int, sys.stdin.readline().split())

start_node = int(sys.stdin.readline())

graph = [[] for _ in range(node+1)]

distance = [INF] * (node+1)

for _ in range(line):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])


def improved_dijkstra(start):
    que = []
    heapq.heappush(que, (0, start))
    distance[start] = 0

    while que:
        node_dist, now = heapq.heappop(que)

        if distance[now] < node_dist:
            continue

        for x in graph[now]:
            cost = node_dist + x[1]

            if cost < distance[x[0]]:
                distance[x[0]] = cost
                heapq.heappush(que, (cost, x[0]))


improved_dijkstra(start_node)

for x in range(node+1):

    if distance[x] == INF:
        print("무한")
    else:
        print(distance[x])
