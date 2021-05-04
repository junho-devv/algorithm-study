import heapq
# 임의의 큰 수(INF) 설정하기
INF = int(1e9)

num_b, num_p = map(int, input().split())

list_path = [[] for _ in range(num_b + 1)]
for _ in range(num_p):
    start, end = map(int, input().split())
    list_path[start].append([1, end])
    list_path[end].append([1, start])

list_dist = [INF] * (num_b + 1)
list_dist[0] = 0
list_dist[1] = 0

que_x = []
heapq.heappush(que_x, (0, 1))

while que_x:
    dist, now = heapq.heappop(que_x)

    if list_dist[now] < dist:
        continue

    for des in list_path[now]:
        cost = dist + des[0]

        if cost < list_dist[des[1]]:
            list_dist[des[1]] = cost
            heapq.heappush(que_x, (cost, des[1]))

one, two, three = 0, 0, 0

two = max(list_dist)

for i in range(1, num_b + 1):
    if list_dist[i] == two:
        one = i
        break

for i in range(1, num_b + 1):
    if list_dist[i] == two:
        three += 1

print(one, two, three)


