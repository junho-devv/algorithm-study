INF = int(1e9)

c_num, p_num = map(int, input().split())

graph = [[INF] * (c_num + 1) for _ in range(c_num + 1)]

for a in range(1, c_num + 1):
    graph[a][a] = 0

for _ in range(p_num):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

pass_point, goal = map(int, input().split())

for k in range(1, c_num + 1):
    for a in range(1, c_num + 1):
        for b in range(1, c_num + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][pass_point] + graph[pass_point][goal]

if distance >= INF:
    print("-1")
else:
    print(distance)

