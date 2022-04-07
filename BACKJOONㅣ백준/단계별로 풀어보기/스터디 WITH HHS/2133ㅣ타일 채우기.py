import sys


in_n = int(sys.stdin.readline())

table_dp = [0 for _ in range(31)]
table_dp[2] = 3

for n in range(4, in_n + 1, 2):
    table_dp[n] = table_dp[2] * table_dp[n - 2] + 2 + sum(table_dp[:n - 2]) * 2

print(table_dp[in_n])
