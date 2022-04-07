import sys
from collections import deque


in_m, in_n = map(int, sys.stdin.readline().split())
box_nm = [list(map(int, sys.stdin.readline().split())) for _ in range(in_n)]
day_nm = [[int(1e9) for _ in range(in_m)] for _ in range(in_n)]

ripen_tomato = deque()
for n in range(in_n):
    for m in range(in_m):
        if box_nm[n][m] == 1:
            ripen_tomato.append((n, m))

way_4 = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def ripe():
    while ripen_tomato:
        temp_x, temp_y = ripen_tomato.popleft()

        for way in way_4:
            way_x, way_y = way
            next_x, next_y = temp_x + way_x, temp_y + way_y

            if 0 <= next_x < in_n and 0 <= next_y < in_m:
                if box_nm[next_x][next_y] == 0:
                    box_nm[next_x][next_y] = box_nm[temp_x][temp_y] + 1
                    ripen_tomato.append((next_x, next_y))


ripe()

isRipen = True
answer = -1
for n in range(in_n):
    for m in range(in_m):
        if box_nm[n][m] == 0:
            isRipen = False

        answer = max(answer, box_nm[n][m])

if not isRipen:
    print(-1)
elif answer == -1:
    print(0)
else:
    print(answer - 1)
