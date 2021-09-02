length_n = int(input())
seq_n = list(map(int, input().split()))

table_dp = [0] * (int(1e3) + 1)

for a in range(length_n):
    for b in range(a):
        if seq_n[a] > seq_n[b] and table_dp[a] < table_dp[b]:
            table_dp[a] = table_dp[b]

    table_dp[a] += 1

print(max(table_dp))
