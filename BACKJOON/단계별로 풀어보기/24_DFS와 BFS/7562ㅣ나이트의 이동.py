import sys
from collections import deque


move_8 = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]


def search():
    que_xy = deque([(curr_x, curr_y)])
    while que_xy:
        temp_x, temp_y = que_xy.popleft()
        if temp_x == goal_x and temp_y == goal_y:
            return

        for move in move_8:
            next_x, next_y = temp_x + move[0], temp_y + move[1]
            if 0 <= next_x < in_i and 0 <= next_y < in_i:
                if chessboard[next_x][next_y] == 0:
                    chessboard[next_x][next_y] = chessboard[temp_x][temp_y] + 1
                    que_xy.append((next_x, next_y))


in_tc = int(sys.stdin.readline())
for _ in range(in_tc):
    in_i = int(sys.stdin.readline())
    curr_x, curr_y = map(int, sys.stdin.readline().split())
    goal_x, goal_y = map(int, sys.stdin.readline().split())

    chessboard = [[0 for _ in range(in_i)] for _ in range(in_i)]
    chessboard[curr_x][curr_y] = 1

    search()

    print(chessboard[goal_x][goal_y] - 1)
