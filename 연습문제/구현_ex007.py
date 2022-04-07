from itertools import combinations

n, m = map(int, input().split())

city_map = []

for i in range(n):
    city_map.append(list(map(int, input().split())))


def calculate_distance(city_list, chicken_list):

    answer = 0

    for city in city_list:

        result = int(1e9)

        for chicken in chicken_list:

            x_temp = abs(city[0] - chicken[0])
            y_temp = abs(city[1] - chicken[1])

            result = min(result, x_temp + y_temp)

        answer += result

    return answer


def solution():

    city_list = []
    chicken_list = []

    for x in range(n):
        for y in range(n):

            if city_map[x][y] == 1:
                city_list.append([x, y])

            if city_map[x][y] == 2:
                chicken_list.append([x, y])

    candidates = list(combinations(chicken_list, m))

    answer = int(1e9)

    for candidate in candidates:
        answer = min(answer, calculate_distance(city_list, candidate))

    return answer


print(solution())
