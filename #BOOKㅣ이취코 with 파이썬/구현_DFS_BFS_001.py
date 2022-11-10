# 특정 거리의 도시 찾기
from collections import deque


def solution(city, roads, visited, distances):

    visited[city] = True

    print(city, end=' ')

    for next_city in roads[city]:
        if not visited[next_city]:
            temp = distances[next_city] + distances[city] + 1
            distances[next_city] = min(distances)
            solution(next_city, roads, visited, distances)

    return 0


c_num, r_num, s_path, c_start = map(int, input().split())

road_list = [[] for _ in range(c_num + 1)]

for _ in range(r_num):
    x, y = map(int, input().split())
    road_list[x].append(y)

road_distance = [-1] * (c_num + 1)
road_distance[c_start] = 0

que = deque([c_start])

while que:
    now = que.popleft()

    for road in road_list[now]:

        if road_distance[road] == -1:

            road_distance[road] = road_distance[now] + 1
            que.append(road)

check = False
for i in range(1, c_num + 1):
    if road_distance[i] == s_path:
        print(i)
        check = True

if not check:
    print(-1)

