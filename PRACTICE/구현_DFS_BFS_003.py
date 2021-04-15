m_size, v_num = map(int, input().split())

v_map = []

temp_map = []
for i in range(m_size):
    for j in range(m_size):
        temp_map[i][j] = v_map[i][j]

for i in range(m_size):
    v_map.append(list(map(int, input().split())))

v_sec, v_x, v_y = map(int, input().split())

# 전염 방향 : 좌, 상, 우, 하
x_direction = [1, 0, -1, 0]
y_direction = [0, 1, 0, -1]


def spread_virus(x, y):

    for d in range(4):
        next_x = x + x_direction[d]
        next_y = y + y_direction[d]

        if 0 <= next_x < m_size and 0 <= next_y < m_size:
            if temp_map[next_x][next_y] == 0:
                temp_map[next_x][next_y] = temp_map[x][y]


def search_in_depth_first(sec):

    for t in range(1, v_num):
        for x in range(m_size):
            for y in range(m_size):

                if v_map[x][y] == t:
                    spread_virus(x, y)


search_in_depth_first(0)

for i in range(m_size):
    print(v_map[i])
