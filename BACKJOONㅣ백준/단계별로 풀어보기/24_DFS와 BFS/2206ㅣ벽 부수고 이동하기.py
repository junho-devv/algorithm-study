import sys
from collections import deque


in_n, in_m = map(int, sys.stdin.readline().split())
map_nm = [list(sys.stdin.readline().rstrip()) for _ in range(in_n)]

min_dist = [[[0 for _ in range(2)] for _ in range(in_m)] for _ in range(in_n)]
min_dist[0][0][1] = 1

way_4 = [(1, 0), (-1, 0), (0, 1), (0, -1)]

que_nm = deque([(0, 0, 1)])
while que_nm:
    temp_x, temp_y, temp_break = que_nm.popleft()
    if temp_x == in_n - 1 and temp_y == in_m - 1:
        print(min_dist[temp_x][temp_y][temp_break])
        break

    for way in way_4:
        next_x, next_y = temp_x + way[0], temp_y + way[1]
        if 0 <= next_x < in_n and 0 <= next_y < in_m:
            if map_nm[next_x][next_y] == '0' and min_dist[next_x][next_y][temp_break] == 0:
                min_dist[next_x][next_y][temp_break] = min_dist[temp_x][temp_y][temp_break] + 1
                que_nm.append((next_x, next_y, temp_break))
            elif map_nm[next_x][next_y] == '1' and temp_break == 1:
                min_dist[next_x][next_y][0] = min_dist[temp_x][temp_y][temp_break] + 1
                que_nm.append((next_x, next_y, 0))
else:
    print(-1)
