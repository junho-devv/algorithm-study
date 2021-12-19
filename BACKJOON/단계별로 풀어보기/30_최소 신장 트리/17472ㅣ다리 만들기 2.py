from collections import deque
import sys


def group(para_row, para_col, para_isl):
    que_rc = deque([[para_row, para_col]])
    while que_rc:
        temp_r, temp_c = que_rc.popleft()
        isl_nm[temp_r][temp_c] = para_isl

        for way in way_4:
            next_r, next_c = temp_r + way[0], temp_c + way[1]
            if 0 <= next_r < in_n and 0 <= next_c < in_m:
                if map_nm[next_r][next_c] == 1 and isl_nm[next_r][next_c] == 0:
                    que_rc.append([next_r, next_c])


if __name__ == '__main__':
    in_n, in_m = map(int, sys.stdin.readline().split())
    map_nm = [list(map(int, sys.stdin.readline().split())) for _ in range(in_n)]
    isl_nm = [[0] * in_m for _ in range(in_n)]

    way_4 = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    num_isl = 0

    for _r in range(in_n):
        for _c in range(in_m):
            if map_nm[_r][_c] == 1 and isl_nm[_r][_c] == 0:
                num_isl += 1
                group(_r, _c, num_isl)

    for _r in isl_nm:
        print(_r)
