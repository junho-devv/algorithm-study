# 블록 이동하기
from collections import deque

b_size = 5
board = [
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 1],
    [1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0]
]

a_robot = {(0, 0), (1, 0)}

robot_left = (0, 0)
robot_right = (1, 0)


def get_next_pos(pos, temp_board):

    next_pos = []
    pos = list(pos)
    left_x, left_y, right_x, right_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]

    x_direction = [1, 0, -1, 0]
    y_direction = [0, 1, 0, -1]

    for d in range(4):
        left_nx, left_ny = left_x + x_direction[d], left_y + y_direction[d]
        right_nx, right_ny = right_x + x_direction[d], right_y + y_direction[d]

        if temp_board[left_nx][left_ny] == 0 and temp_board[right_nx][right_ny] == 0:
            next_pos.append({(left_nx, left_ny), (right_nx, right_ny)})

    if left_x == right_x:
        for i in [-1, 1]:
            if temp_board[left_x + i][left_y] == 0 and temp_board[right_x + i][left_y] == 0:
                next_pos.append({(left_x, left_y), (left_x + i, left_y)})
                next_pos.append({(right_x, right_y), (right_x + i, right_y)})

    if left_y == right_y:
        for i in [-1, 1]:
            if temp_board[left_x][left_y + i] == 0 and temp_board[right_x][right_y + i] == 0:
                next_pos.append({(left_x, left_y), (left_x, left_y + i)})
                next_pos.append({(right_x, right_y), (right_x, right_y + i)})

    return next_pos


def solution():

    answer = 0

    temp_board = [[1] * (b_size + 2) for _ in range(b_size + 2)]
    for x in range(b_size):
        for y in range(b_size):
            temp_board[x + 1][y + 1] = board[x][y]

    start_pos = {(1, 1), (1, 2)}

    a_que = deque()
    a_que.append((start_pos, answer))

    visited_list = [a_robot]

    while a_que:
        a_pos, answer = a_que.popleft()

        if (b_size, b_size) in a_pos:
            return answer

        for next_pos in get_next_pos(a_pos, temp_board):

            if next_pos not in visited_list:
                a_que.append((next_pos, answer + 1))
                visited_list.append(next_pos)

    return answer


print(solution())
