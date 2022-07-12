import sys

INF = int(1e9)

node, line = map(int, input().split())

start_node = int(input())
graph = [[] for i in range(node+1)]

visited = [False] * (node+1)
distance = [INF] * (node+1)

for _ in range(line):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])


def get_smallest_node():
    min_value = INF
    index = 0

    for x in range(1, node+1):
        if distance[x] < min_value and not visited[x]:
            min_value = distance[x]
            index = x

    return index


def dijkstra(start):

    distance[start] = 0
    visited[start] = True

    for x in graph[start]:
        distance[x[0]] = x[1]

    for x in range(node - 1):

        now = get_smallest_node()
        visited[now] = True

        for y in graph[now]:

            cost = distance[now] + y[1]

            if distance[y[0]] > cost:
                distance[y[0]] = cost


dijkstra(start_node)

for x in range(1, node+1):

    if distance[x] == INF:
        print("무한")
    else:
        print(distance[x])



