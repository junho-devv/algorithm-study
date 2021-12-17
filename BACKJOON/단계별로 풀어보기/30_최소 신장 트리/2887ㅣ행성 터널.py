import sys


def find(para_node):
    if list_parent[para_node] != para_node:
        list_parent[para_node] = find(list_parent[para_node])

    return list_parent[para_node]


def union(para_node_1, para_node_2):
    root_1, root_2 = find(para_node_1), find(para_node_2)
    if root_1 > root_2:
        root_1, root_2 = root_2, root_1

    list_parent[root_2] = root_1


if __name__ == '__main__':
    in_n = int(sys.stdin.readline())

    list_planet = [list(map(int, sys.stdin.readline().split())) + [_] for _ in range(in_n)]

    list_tunnel = []
    for _1 in range(3):
        list_planet.sort(key=lambda _: _[_1])
        for _2 in range(1, in_n):
            temp_dist = abs(list_planet[_2][_1] - list_planet[_2 - 1][_1])
            now_idx = list_planet[_2][3]
            prev_idx = list_planet[_2 - 1][3]

            list_tunnel.append([temp_dist, now_idx, prev_idx])
    list_tunnel.sort(key=lambda _: _[0])

    list_parent = [_ for _ in range(in_n)]
    out_min = 0
    for cost, planet_1, planet_2 in list_tunnel:
        if find(planet_1) != find(planet_2):
            union(planet_1, planet_2)
            out_min += cost

    print(out_min)
