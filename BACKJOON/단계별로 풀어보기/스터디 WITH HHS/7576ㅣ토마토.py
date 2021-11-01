import sys
from collections import deque


in_m, in_n = map(int, sys.stdin.readline().split())
box_nm = [list(map(int, sys.stdin.readline().split())) for _ in range(in_n)]
day_nm = [[int(1e9) for _ in range(in_m)] for _ in range(in_n)]

ripen_tomato = []
for n in range(in_n):
    for m in range(in_m):
        if box_nm[n][m] == 1:
            ripen_tomato.append((n, m))
        elif box_nm[n][m] == -1:
            day_nm[n][m] = -1

way_4 = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def ripe(para_x, para_y):
    que_tomato = deque([[para_x, para_y]])
    while que_tomato:
        temp_x, temp_y = que_tomato.popleft()

        for way in way_4:
            way_x, way_y = way
            next_x, next_y = temp_x + way_x, temp_y + way_y

            if 0 <= next_x < in_n and 0 <= next_y < in_m:
                if box_nm[next_x][next_y] == 0 and day_nm[next_x][next_y] > box_nm[temp_x][temp_y] + 1:
                    box_nm[next_x][next_y] = box_nm[temp_x][temp_y] + 1
                    que_tomato.append([next_x, next_y])

    return


for tomato in ripen_tomato:
    tomato_x, tomato_y = tomato
    day_nm[tomato_x][tomato_y] = 0
    ripe(tomato_x, tomato_y)

answer = 0
for n in range(in_n):
    for m in range(in_m):
        if box_nm[n][m] == 0:
            print(-1)
