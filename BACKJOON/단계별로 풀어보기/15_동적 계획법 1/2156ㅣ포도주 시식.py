num_n = int(input())

amount_n = [0] * (int(1e4) + 1)
table_dp = [0] * (int(1e4) + 1)

for i in range(1, num_n + 1):
    amount_n[i] = int(input())

table_dp[1] = amount_n[1]
table_dp[2] = amount_n[1] + amount_n[2]

for i in range(3, num_n + 1):

    table_dp[i] = max(table_dp[i - 3] + amount_n[i - 1] + amount_n[i], table_dp[i - 2] + amount_n[i], table_dp[i - 1])

print(table_dp[num_n])
