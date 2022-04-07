import heapq

INF = int(1e9)


def explore_the_space(a_size, a_list):

    x_direction = [1, 0, -1, 0]
    y_direction = [0, 1, 0, -1]

    table_cost = [[INF] * a_size for _ in range(a_size)]

    que_e = [(a_list[0][0], 0, 0)]
    table_cost[0][0] = a_list[0][0]

    while que_e:
        cost, x, y = heapq.heappop(que_e)

        if table_cost[x][y] < cost:
            continue

        for i in range(4):
            next_x = x + x_direction[i]
            next_y = y + y_direction[i]

            # if next_x < 0 or next_x >= a_size or next_y < 0 or next_y >= a_size:
            #     continue
            #
            # cost += a_list[next_x][next_y]
            # if cost < table_cost[next_x][next_y]:
            #     table_cost[next_x][next_y] = cost
            #     heapq.heappush(que_e, (cost, next_x, next_y))
            if 0 <= next_x < size_e and 0 <= next_y < size_e:
                next_cost = cost + list_e[next_x][next_y]
                if next_cost < table_cost[next_x][next_y]:
                    table_cost[next_x][next_y] = next_cost
                    heapq.heappush(que_e, (next_cost, next_x, next_y))

    answer = table_cost[size_e - 1][size_e - 1]

    return answer


# 테스트 케이스 개수 입력하기
num_t = int(input())

for t in range(num_t):
    # 탐사 공간의 크기 입력하기
    size_e = int(input())
    # 탐사 공간 속 각 칸의 에너지 소모량
    list_e = []
    for _ in range(size_e):
        list_e.append(list(map(int, input().split())))

    print(explore_the_space(size_e, list_e))

# 3
# 3
# 5 5 4
# 3 9 1
# 3 2 7
# 5
# 3 7 2 0 1
# 2 8 0 9 1
# 1 2 1 9 1
# 9 8 9 2 0
# 3 6 5 1 5
# 7
# 9 0 5 1 1 5 3
# 4 1 2 1 6 5 3
# 0 7 6 1 6 8 5
# 1 1 7 8 3 2 3
# 9 4 0 7 6 4 1
# 5 8 3 2 4 8 3
# 7 4 8 4 8 3 4
