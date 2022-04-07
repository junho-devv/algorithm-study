import sys


in_n = int(sys.stdin.readline())

table_dp = [0] * 50001
table_dp[0], table_dp[1] = 0, 1

roots = []
for n in range(1, in_n + 1):

    if n ** 0.5 == int(n ** 0.5):
        roots.append(n)

    temp_min = int(1e9)
    for root in roots:
        temp_min = min(temp_min, table_dp[n - root])
    table_dp[n] = temp_min + 1

print(table_dp[in_n])
