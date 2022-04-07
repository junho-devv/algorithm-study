from collections import deque
import sys


def group(para_row, para_col, para_isl):
    isl_nm[para_row][para_col] = para_isl
    que_rc = deque([[para_row, para_col]])
    list_isl.append((para_row, para_col, para_isl))
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
        for way in way_4:
            que_rc = deque([[p_c, p_r]])
            temp_dist = 0
            while que_rc:
                temp_r, temp_c = que_rc.popleft()
                next_r, next_c = temp_r + way[0], temp_c + way[1]
                if 0 <= next_r < in_n and 0 <= next_c < in_m:
                    if isl_nm[next_r][next_c] == 0:
                        temp_dist += 1
                        que_rc.append([next_r, next_c])
                    elif isl_nm[next_r][next_c] != p_isl and temp_dist >= 2:
                        list_edge.append([temp_dist, p_isl, isl_nm[next_r][next_c]])


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
    in_n, in_m = map(int, sys.stdin.readline().split())
    map_nm = [list(map(int, sys.stdin.readline().split())) for _ in range(in_n)]
    isl_nm = [[0] * in_m for _ in range(in_n)]

    way_4 = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    # 각 섬에 번호 부여하기
    list_isl, num_isl = [], 0
    for _r in range(in_n):
        for _c in range(in_m):
            if map_nm[_r][_c] == 1 and isl_nm[_r][_c] == 0:
                num_isl += 1
                group(_r, _c, num_isl)

    list_edge = []
    search()
    list_edge.sort(key=lambda _: _[0])

    list_parent = [_ for _ in range(num_isl + 1)]
    out_min, cnt_edge = 0, 0
    for _dist, _1, _2 in list_edge:
        if find(_1) != find(_2):
            union(_1, _2)
            out_min += _dist

            cnt_edge += 1

    if cnt_edge == num_isl - 1:
        print(out_min)
    else:
        print(-1)
