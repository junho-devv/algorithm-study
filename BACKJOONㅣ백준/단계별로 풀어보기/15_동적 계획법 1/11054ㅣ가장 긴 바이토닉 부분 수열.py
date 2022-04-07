num_n = int(input())
seq_n = list(map(int, input().split()))

table_dp1 = [0] * (int(1e3) + 1)
table_dp2 = [0] * (int(1e3) + 1)

for x in range(num_n):

    for y in range(x):
        if seq_n[x] > seq_n[y] and table_dp1[x] < table_dp1[y]:
            table_dp1[x] = table_dp1[y]
    table_dp1[x] += 1

for x in reversed(range(num_n)):
    for y in range(num_n - 1, x, -1):
        if seq_n[x] > seq_n[y] and table_dp2[x] < table_dp2[y]:
            table_dp2[x] = table_dp2[y]
    table_dp2[x] += 1

sum_dp = [0] * (int(1e3) + 1)
for i in range(num_n):

    sum_dp[i] = table_dp1[i] + table_dp2[i] - 1

print(max(sum_dp))
