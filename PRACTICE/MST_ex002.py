def find_center_city(graph, x_house):

    if graph[x_house] != x_house:
        graph[x_house] = find_center_city(graph, graph[x_house])

    return graph[x_house]


def connect_two_houses(graph, x_house, y_house):

    x = find_center_city(graph, x_house)
    y = find_center_city(graph, y_house)

    if x < y:
        graph[y] = x
    else:
        graph[x] = y


h_num, r_num = map(int, input().split())

city_map = [0] * (h_num + 1)

for i in range(1, h_num + 1):
    city_map[i] = i

city_road = []

for _ in range(r_num):
    a_house, b_house, m_cost = map(int, input().split())
    city_road.append([m_cost, a_house, b_house])

city_road.sort()

min_cost = []

# for i in range(r_num):
#     print(city_road[i][0], "+", city_road[i][1], "+", city_road[i][2])

for i in range(r_num):

    a_house = find_center_city(city_map, city_road[i][1])
    b_house = find_center_city(city_map, city_road[i][2])

    if a_house != b_house:
        connect_two_houses(city_map, city_road[i][1], city_road[i][2])
        # min_cost += city_road[i][0]
        min_cost.append(city_road[i][0])

# for edge in city_road:
#     cost, a, b = edge
#
#     if find_center_city(city_map, a) != find_center_city(city_map, b):
#         connect_two_houses(city_map, a, b)
#         min_cost += cost

max_cost = max(min_cost)

print(city_map)

print(sum(min_cost) - max_cost)




