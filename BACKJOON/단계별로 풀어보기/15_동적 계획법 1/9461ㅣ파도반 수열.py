num_tc = int(input())

for _ in range(num_tc):

    input_n = int(input())

    table_dp = [0] * (int(1e2) + 1)

    for i in range(1, 4):
        table_dp[i] = 1

    for i in range(4, input_n + 1):
        table_dp[i] = table_dp[i - 2] + table_dp[i - 3]

    print(table_dp[input_n])
