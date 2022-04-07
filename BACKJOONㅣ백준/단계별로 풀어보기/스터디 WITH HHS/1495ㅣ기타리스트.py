import sys

input = sys.stdin.readline

in_n, in_s, in_m = map(int, input().split())
list_v = list(map(int, input().split()))

table_dp = [[False for _ in range(in_m + 1)] for _ in range(in_n + 1)]
table_dp[0][in_s] = True
for n in range(in_n):
    for m in range(in_m + 1):
        if table_dp[n][m]:
            if m + list_v[n] <= in_m:
                table_dp[n + 1][m + list_v[n]] = True
            if m - list_v[n] >= 0:
                table_dp[n + 1][m - list_v[n]] = True

for m in reversed(range(in_m + 1)):
    if table_dp[in_n][m]:
        print(m)
        break
else:
    print(-1)

