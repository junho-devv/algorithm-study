import sys


INF = int(1e9)

in_n = int(sys.stdin.readline())
in_m = int(sys.stdin.readline())

graph = [[INF] * (in_n + 1) for _ in range(in_n + 1)]

for n in range(1, in_n + 1):
    graph[n][n] = 0

for _ in range(in_m):
    in_n1, in_n2, in_c = map(int, sys.stdin.readline().split())
    graph[in_n1][in_n2] = in_c

for k in range(1, in_n + 1):
    for n1 in range(1, in_n + 1):
        for n2 in range(1, in_n + 1):
            graph[n1][n2] = min(graph[n1][n2], graph[n1][k] + graph[k][n2])

for n1 in range(1, in_n + 1):
    for n2 in range(1, in_n + 1):
        if graph[n1][n2] == INF:
            print("INFINITY", end=' ')
        else:
            print(graph[n1][n2], end=' ')
    print()
