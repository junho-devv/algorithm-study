INF = int(1e9)

node = int(input())
line = int(input())

graph = [[INF] * (node+1) for _ in range(node+1)]

for a in range(1, node+1):
    graph[a][a] = 0

for _ in range(line):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for i in range(1, node + 1):
    for a in range(1, node + 1):
        for b in range(1, node + 1):
            graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])

for a in range(1, node + 1):
    for b in range(1, node + 1):

        if graph[a][b] == INF:
            print("무한", end=" ")

        else:
            print(graph[a][b], end=" ")
    print()
