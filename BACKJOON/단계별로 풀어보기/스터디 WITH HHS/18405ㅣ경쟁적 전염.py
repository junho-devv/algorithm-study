from collections import deque
import sys


def spread():
    list_virus = []
    for row in range(in_n):
        for col in range(in_n):
            if examiner_n[row][col] != 0:
                list_virus.append([examiner_n[row][col], row, col, 0])
    list_virus.sort(key=lambda x: x[0])

    que_virus = deque(list_virus)
    while que_virus:
        temp_type, temp_x, temp_y, temp_time = que_virus.popleft()

        if temp_time == in_s:
            break

        for move in move_4:
            next_x, next_y = temp_x + move[0], temp_y + move[1]
            if 0 <= next_x < in_n and 0 <= next_y < in_n:
                if examiner_n[next_x][next_y] == 0:
                    examiner_n[next_x][next_y] = temp_type
                    que_virus.append([temp_type, next_x, next_y, temp_time + 1])

    return examiner_n[in_x - 1][in_y - 1]


if __name__ == '__main__':
    in_n, in_k = map(int, sys.stdin.readline().split())

    examiner_n = []
    for _ in range(in_n):
        examiner_n.append(list(map(int, sys.stdin.readline().split())))

    in_s, in_x, in_y = map(int, sys.stdin.readline().split())

    move_4 = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    out_type = spread()
    print(out_type)
