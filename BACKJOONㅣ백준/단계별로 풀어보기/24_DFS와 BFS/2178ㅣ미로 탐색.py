import sys
from collections import deque


in_n, in_m = map(int, sys.stdin.readline().split())
maze_nm = [list(sys.stdin.readline().rstrip()) for _ in range(in_n)]

min_nm = [[int(1e5) for _ in range(in_m)] for _ in range(in_n)]
way_4 = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def search(para_x, para_y):
    que_xy = deque([[para_x, para_y]])

    while que_xy:
        temp_x, temp_y = que_xy.popleft()

        for way in way_4:
            way_x, way_y = way
            next_x, next_y = temp_x + way_x, temp_y + way_y

            if 0 <= next_x < in_n and 0 <= next_y < in_m:
                if maze_nm[next_x][next_y] == '1':
                    que_xy.append([next_x, next_y])
                    maze_nm[next_x][next_y] = maze_nm[temp_x][temp_y] + 1


maze_nm[0][0] = 1
search(0, 0)

print(maze_nm[in_n - 1][in_m - 1])
