import sys

in_m, in_n = map(int, input().split())
map_mn = [list(map(int, sys.stdin.readline().split())) for _ in range(in_m)]
table_dp = [[-1 for _ in range(in_n)] for _ in range(in_m)]


def search_in_dfs(para_x, para_y):
    if para_x == in_m - 1 and para_y == in_n - 1:
        return 1

    if table_dp[para_x][para_y] != -1:
        return table_dp[para_x][para_y]
    else:
        table_dp[para_x][para_y] = 0
        for d in range(4):
            next_x = para_x + dx[d]
            next_y = para_y + dy[d]

            if 0 <= next_x < in_m and 0 <= next_y < in_n:
                if map_mn[next_x][next_y] < map_mn[para_x][para_y]:
                    table_dp[para_x][para_y] += search_in_dfs(next_x, next_y)
        # table_dp[para_x][para_y] = temp
        return table_dp[para_x][para_y]


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

print(search_in_dfs(0, 0))
