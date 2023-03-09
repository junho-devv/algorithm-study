import sys


INF = int(1e9)

in_n, in_m = map(int, sys.stdin.readline().split())
in_s = int(sys.stdin.readline())

graph = [[] for _ in range(in_n + 1)]
visited = [False] * (in_n + 1)
distance = [INF] * (in_n + 1)

for _ in range(in_m):
    in_n1, in_n2, in_c = map(int, sys.stdin.readline().split())
    graph[in_n1].append((in_n2, in_c))


def get_smallest_node():
    min_value = INF
    idx = 0

    for n in range(1, in_n + 1):
        if distance[n] < min_value and not visited[n]:
            min_value = distance[n]
            idx = n

    return idx


def dijkstra(start_node):
    visited[start_node] = True
    distance[start_node] = 0

    for node, cost in graph[start_node]:
        distance[node] = cost

    for n in range(in_n - 1):

        now_node = get_smallest_node()
        visited[now_node] = True

        for node, cost in graph[now_node]:
            cost += distance[now_node]

            if cost < distance[node]:
                distance[node] = cost


dijkstra(in_s)

for n in range(1, in_n + 1):
    if distance[n] == INF:
        print("INFINITY")
    else:
        print(distance[n])
