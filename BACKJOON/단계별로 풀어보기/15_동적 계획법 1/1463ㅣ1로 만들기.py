int_n = int(input())

table_dp = [0] * (int(1e6) + 1)

for i in range(2, int_n + 1):

    count_n = 0
    result_n = int(1e9)

    if i % 2 == 0:
        result_n = min(result_n, table_dp[i // 2] + 1)

    if i % 3 == 0:
        result_n = min(result_n, table_dp[i // 3] + 1)

    result_n = min(result_n, table_dp[i - 1] + 1)

    table_dp[i] = result_n

print(table_dp[int_n])
