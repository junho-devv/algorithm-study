# 인구 이동
from collections import deque

c_size, a_left, a_right = 2, 20, 50
p_map = [
    [50, 30],
    [20, 40]
]

x_direction = [1, 0, -1, 0]
y_direction = [0, 1, 0, -1]


def unite_countries(a, b, sector, a_union):

    a_united = [(a, b)]

    a_que = deque()
    a_que.append((a, b))

    a_union[a][b] = sector
    a_population = p_map[a][b]
    u_num = 1

    while a_que:
        x, y = a_que.popleft()

        # 4가지 방향을 확인
        for d in range(4):
            next_x = x + x_direction[d]
            next_y = y + y_direction[d]

            if 0 <= next_x < c_size and 0 <= next_y < c_size and a_union[next_x][next_y] == -1:
                a_diff = abs(p_map[next_x][next_y] - p_map[x][y])
                if a_left <= a_diff <= a_right:
                    a_que.append((next_x, next_y))
                    a_union[next_x][next_y] = sector
                    a_population += p_map[next_x][next_y]
                    u_num += 1
                    a_united.append((next_x, next_y))

    for x, y in a_united:
        p_map[x][y] = a_population // u_num

    return u_num


def solution():
    answer = 0

    while True:
        print("while")
        print(p_map)
        a_union = [[-1] * c_size for _ in range(c_size)]
        sector = 0

        for x in range(c_size):
            print("a for")
            for y in range(c_size):
                print("for num")
                if a_union[x][y] == -1:
                    unite_countries(x, y, sector, a_union)
                    print(a_union)
                    sector += 1

        if sector == c_size * c_size:
            print(sector)
            break

        answer += 1
    print(a_union)
    return answer


print(solution())
