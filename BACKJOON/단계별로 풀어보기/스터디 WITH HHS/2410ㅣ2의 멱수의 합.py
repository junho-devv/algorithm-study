import sys


in_n = int(sys.stdin.readline())

table_dp = [0] * (int(1e6) + 1)
table_dp[0] = 1

for i in range(in_n):
    if 2 ** i <= in_n:
        for j in range(2 ** i, in_n + 1):
            table_dp[j] += table_dp[j - 2 ** i]

    print(table_dp[:10])
