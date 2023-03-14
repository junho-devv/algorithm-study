import heapq

INF = int(1e9)

# 첫째 줄 입력값 : 도시의 개수(c_num), 통로의 개수(p_num), 메시지를 보내고자 하는 도시(c_start)
c_num, p_num, c_start = map(int, input().split())

graph = [[] for _ in range(c_num + 1)]

distance = [INF] * (c_num + 1)

for _ in range(1, p_num + 1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])


def improved_dijkstra(start_node):

    que = []
    heapq.heappush(que, (0, start_node))
    distance[start_node] = 0

    while que:
        now_dist, now_node = heapq.heappop(que)

        if now_dist > distance[now_node]:
            continue

        for i in graph[now_node]:

            cost = now_dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(que, (cost, i[0]))


improved_dijkstra(c_start)

c_count = 0
t_count = 0

for o in range(c_num + 1):

    if distance[o] != INF and o != c_start:
        c_count += 1
        if t_count < distance[o]:
            t_count = distance[o]

print(c_count, t_count)
