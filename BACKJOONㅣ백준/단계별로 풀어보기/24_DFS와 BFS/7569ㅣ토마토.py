import sys
from collections import deque


in_m, in_n, in_h = map(int, sys.stdin.readline().split())
box_hnm = [[list(map(int, sys.stdin.readline().split())) for _ in range(in_n)] for _ in range(in_h)]

ripen_tomato = deque()
for h in range(in_h):
    for n in range(in_n):
        for m in range(in_m):
            if box_hnm[h][n][m] == 1:
                ripen_tomato.append((h, n, m))

way_6 = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def ripe():
    while ripen_tomato:
        temp_z, temp_x, temp_y = ripen_tomato.popleft()
        for way in way_6:
            next_z, next_x, next_y = temp_z + way[0], temp_x + way[1], temp_y + way[2]
            if 0 <= next_z < in_h and 0 <= next_x < in_n and 0 <= next_y < in_m:
                if box_hnm[next_z][next_x][next_y] == 0:
                    box_hnm[next_z][next_x][next_y] = box_hnm[temp_z][temp_x][temp_y] + 1
                    ripen_tomato.append((next_z, next_x, next_y))

    return


ripe()

isRipen = True
answer = -1
for h in range(in_h):
    for n in range(in_n):
        for m in range(in_m):
            if box_hnm[h][n][m] == 0:
                isRipen = False

            answer = max(answer, box_hnm[h][n][m])


if not isRipen:
    print(-1)
elif answer == -1:
    print(0)
else:
    print(answer - 1)
