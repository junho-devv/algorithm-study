num_n = int(input())
seq_n = list(map(int, input().split()))

table_dp = [0] * (int(1e5) + 1)

for n in range(num_n):

    if table_dp[n] < 0:
        table_dp[n + 1] = seq_n[n]
    else:
        table_dp[n + 1] = table_dp[n] + seq_n[n]

print(max(table_dp[1:num_n + 1]))
