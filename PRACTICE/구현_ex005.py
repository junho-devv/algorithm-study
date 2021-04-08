from collections import deque

board_size = int(input())
apple_num = int(input())

board = [[0] * (board_size + 1) for _ in range(board_size + 1)]

x_direction = [1, 0, -1, 0]
y_direction = [0, 1, 0, -1]
direction = 0

for _ in range(apple_num):

    a_row, a_col = map(int, input().split())
    board[a_row][a_col] += 1

change_num = int(input())

s_que = deque()

for _ in range(change_num):

    a_sec, a_dir = map(str, input().split())
    s_que.append([a_sec, a_dir])

print(s_que)

a_que = deque()
a_que.append([1, 1])

answer = 0

x, y = 1, 1

crashed = True

while crashed:

    if s_que:
        crashed = True
    else:
        s_que.append(["999999", "L"])
        continue

    x_temp, y_temp = s_que.popleft()

    move_time = int(x_temp) - answer

    for _ in range(move_time):

        answer += 1

        a_temp = x + x_direction[direction]
        b_temp = y + y_direction[direction]
        print(x, y)
        if a_temp < 1 or b_temp < 1 or a_temp > board_size or b_temp > board_size:
            crashed = False
            break

        for val in a_que:
            if a_temp == val[0] and b_temp == val[1]:
                crashed = False
                break

        a_que.append([a_temp, b_temp])

        if board[b_temp][a_temp] == 0:
            a_que.popleft()

        x, y = a_temp, b_temp

    if y_temp == "L":
        direction -= 1
    if y_temp == "D":
        direction += 1

print(a_que)
print(answer)
