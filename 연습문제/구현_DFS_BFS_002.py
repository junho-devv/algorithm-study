# 연구소 14502

n, m = 7, 7

r_map = [
    [2, 0, 0, 0, 1, 1, 0],
    [0, 0, 1, 0, 1, 2, 0],
    [0, 1, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0]
]

temp_map = [[0] * m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0


def spread_virus(x, y):

    for direction in range(4):

        nx = x + dx[direction]
        ny = y + dy[direction]
        # 상, 하, 좌, 우 중에서 바이러스가 퍼질 수 있는 경우
        if 0 <= nx < n and 0 <= ny < m:
            if temp_map[nx][ny] == 0:
                # 해당 위치에 바이러스 배치하고, 다시 재귀적으로 수행
                temp_map[nx][ny] = 2
                spread_virus(nx, ny)


def get_score():

    score = 0

    for x in range(n):
        for y in range(m):
            if temp_map[x][y] == 0:
                score += 1

    return score


def search_in_depth_first(count):

    global result

    if count == 3:
        for x in range(n):
            for y in range(m):
                temp_map[x][y] = r_map[x][y]
        # 각 바이러스의 위치에서 전파 진행
        for x in range(n):
            for y in range(m):
                if temp_map[x][y] == 2:
                    spread_virus(x, y)
        # 안전 영역의 최댓값 계산
        result = max(result, get_score())
        return

    # 빈 공간에 울타리 설치
    for x in range(n):
        for y in range(m):
            if r_map[x][y] == 0:
                r_map[x][y] = 1
                count += 1
                search_in_depth_first(count)
                count -= 1
                r_map[x][y] = 0


search_in_depth_first(0)
print(r_map)
