import sys


sys.setrecursionlimit(10000)
way_4 = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def move(para_x, para_y):
    visited_cabbage[para_x][para_y] = True

    for way in way_4:
        way_x, way_y = way
        next_x, next_y = para_x + way_x, para_y + way_y

        if 0 <= next_x < in_n and 0 <= next_y < in_m:
            if not visited_cabbage[next_x][next_y] and field_cabbage[next_x][next_y] == 1:
                move(next_x, next_y)


num_tc = int(sys.stdin.readline())
for _ in range(num_tc):
    in_m, in_n, in_k = map(int, sys.stdin.readline().split())
    field_cabbage = [[0 for _ in range(in_m)] for _ in range(in_n)]
    for _ in range(in_k):
        col_k, row_k = map(int, sys.stdin.readline().split())
        field_cabbage[row_k][col_k] = 1
    visited_cabbage = [[False for _ in range(in_m)] for _ in range(in_n)]

    num_worm = 0
    for row in range(in_n):
        for col in range(in_m):
            if not visited_cabbage[row][col] and field_cabbage[row][col] == 1:
                move(row, col)
                num_worm += 1

    print(num_worm)
