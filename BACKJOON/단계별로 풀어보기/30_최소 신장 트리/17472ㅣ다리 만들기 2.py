from collections import deque
import sys


def group(para_row, para_col, para_isl):
    isl_nm[para_row][para_col] = para_isl
    que_rc = deque([[para_row, para_col]])
    while que_rc:
        temp_r, temp_c = que_rc.popleft()
        for way in way_4:
            next_r, next_c = temp_r + way[0], temp_c + way[1]
            if 0 <= next_r < in_n and 0 <= next_c < in_m:
                if map_nm[next_r][next_c] == 1 and isl_nm[next_r][next_c] == 0:
                    isl_nm[next_r][next_c] = para_isl
                    que_rc.append([next_r, next_c])
                    list_isl.append((next_r, next_c, para_isl))


def search():
    for p_c, p_r, p_isl in list_isl:
        que_rc = deque()
        table_nm = [[0] * in_m for _ in range(in_n)]
        for way in way_4:
            que_rc.append((p_c, p_r))
            while que_rc:
                temp_r, temp_c = que_rc.popleft()
                next_r, next_c = temp_r + way[0], temp_c + way[1]
                if 0 <= next_r < in_n and 0 <= next_c < in_m:
                    if isl_nm[next_r][next_c] == 0:
                        table_nm[next_r][next_c] = table_nm[temp_r][temp_c] + 1
                        que_rc.append((next_r, next_c))
                    elif isl_nm[next_r][next_c] != p_isl and table_nm[next_r][next_c] >= 2:
                        list_edge.append(table_nm[next_r][next_c], p_isl, isl_nm[next_r][next_c])


# def find(para_node):
#
#     if list_parent[para_node] != para_node:
#         list_parent[para_node] = find(list_parent[para_node])
#
#     return list_parent[para_node]
#
#
# def union(para_node_1, para_node_2):
#     root_1, root_2 = find(para_node_1), find(para_node_2)
#     if root_1 > root_2:
#         root_1, root_2 = root_2, root_1
#
#     list_parent[root_2] = root_1


if __name__ == '__main__':
    in_n, in_m = map(int, sys.stdin.readline().split())
    map_nm = [list(map(int, sys.stdin.readline().split())) for _ in range(in_n)]
    isl_nm = [[0] * in_m for _ in range(in_n)]

    way_4 = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    list_isl, num_isl = [], 0
    list_isl = []
    for _r in range(in_n):
        for _c in range(in_m):
            if map_nm[_r][_c] == 1 and isl_nm[_r][_c] == 0:
                num_isl += 1
                group(_r, _c, num_isl)

    list_edge = []
    search()

    for _r in isl_nm:
        print(_r)

    print(list_edge)

    # len_isl = len(list_isl)
    # dict_dist = dict()
    # set_dist = set()
    # for _1 in range(len_isl - 1):
    #     for _2 in range(_1 + 1, len_isl):
    #         if list_isl[_1][2] != list_isl[_2][2]:
    #             if list_isl[_1][0] == list_isl[_2][0] or list_isl[_1][1] == list_isl[_2][1]:
    #                 temp_dist = abs(list_isl[_1][0] - list_isl[_2][0]) + abs(list_isl[_1][1] - list_isl[_2][1]) - 1
    #                 set_dist.add((list_isl[_1][2], list_isl[_2][2], temp_dist))
    #
    #                 # if (list_isl[_1][2], list_isl[_2][2]) not in dict_dist:
    #                 #     dict_dist[list_isl[_1][2], list_isl[_2][2]] = [list_isl[_1][2], list_isl[_2][2], temp_dist]
    #                 # else:
    #                 #     temp_min = min(dict_dist[list_isl[_1][2], list_isl[_2][2]][2], temp_dist)
    #                 #     dict_dist[list_isl[_1][2], list_isl[_2][2]] = [list_isl[_1][2], list_isl[_2][2], temp_min]
    #
    # # print(dict_dist)
    # # dict_dist = sorted(dict_dist.items(), key=lambda _: _[1][2])
    # # print(dict_dist)

    # list_dist = list(set_dist)
    # list_dist.sort(key=lambda _: _[2])
    # print(list_dist)
    #
    # list_parent = [_ for _ in range(len_isl + 1)]
    # out_min = 0
    # for _ in list_dist:
    #     if _[2] >= 2:
    #         if find(_[0]) != find(_[1]) and (_[0], _[1]) not in dict_dist:
    #             union(_[0], _[1])
    #             out_min += _[2]
    #             dict_dist[_[0], _[1]] = 1
    #
    # print(out_min)