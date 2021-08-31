import sys


num_n = int(sys.stdin.readline())

stair_n = []
for _ in range(num_n):
    stair_n.append(int(sys.stdin.readline()))

table_dp = [0] * 300
table_dp[0] = stair_n[0]
table_dp[1] = stair_n[0] + stair_n[1]
table_dp[2] = max(stair_n[1] + stair_n[2], stair_n[0] + stair_n[2])

for i in range(3, num_n):
    table_dp[i] = max(table_dp[i - 3] + stair_n[i - 1] + stair_n[i], table_dp[i - 2] + stair_n[i])

print(table_dp[num_n - 1])
