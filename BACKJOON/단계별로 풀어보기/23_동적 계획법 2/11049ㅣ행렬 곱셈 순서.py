import sys


in_n = int(sys.stdin.readline())
list_matrix = [0] + [list(map(int, sys.stdin.readline().split())) for _ in range(in_n)]

table_dp = [[0 for _ in range(in_n + 1)] for _ in range(in_n + 1)]

for l in range(2, in_n + 1):
    for i in range(1, in_n + 1):
        table_dp[i][i + l - 1] = 2 ** 32

        for k in range(i, i + l - 1):
            table_dp[i][i + l - 1] = min(table_dp[i][i + l - 1], table_dp[i][k] + table_dp[k + 1][i + l - 1] +
                                         list_matrix[i][0] * list_matrix[k][1] * )