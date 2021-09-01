length_n = int(input())

table_dp = [[0] * 10 for _ in range(101)]
for i in range(1, 10):
    table_dp[1][i] = 1

for i in range(2, length_n + 1):
    for j in range(10):

        if j == 0:
            table_dp[i][j] = table_dp[i - 1][1]
        elif j == 9:
            table_dp[i][j] = table_dp[i - 1][8]
        else:
            table_dp[i][j] = table_dp[i - 1][j - 1] + table_dp[i - 1][j + 1]

print(sum(table_dp[length_n]) % int(1e9))
