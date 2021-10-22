import sys


in_t = int(sys.stdin.readline())
in_k = int(sys.stdin.readline())
list_k = [list(map(int, sys.stdin.readline().split())) for _ in range(in_k)]

table_dp = [0 for _ in range(in_t + 1)]
table_dp[0] = 1

for k in range(in_k):
    for t in reversed(range(1, in_t + 1)):
        for num in range(1, list_k[k][1] + 1):
            if 0 <= t - list_k[k][0] * num:
                table_dp[t] += table_dp[t - list_k[k][0] * num]

print(table_dp[in_t])
