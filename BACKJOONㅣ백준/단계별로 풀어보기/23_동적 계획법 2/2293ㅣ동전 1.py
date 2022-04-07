import sys


in_n, in_k = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(in_n)]

table_dp = [0] * 10001
table_dp[0] = 1

for coin in coins:
    for k in range(coin, in_k + 1):
        table_dp[k] += table_dp[k - coin]

print(table_dp[in_k])
