num_n = int(input())
list_n = [0] * 501

max_n = 0
for n in range(num_n):
    a, b = map(int, input().split())

    if b > max_n:
        max_n = b

    list_n[a] = b

table_dp = [0] * 501
for x in range(1, max_n + 1):
    for y in range(1, x):
        if list_n[x] >= list_n[y] > 0 and table_dp[x] <= table_dp[y]:
            table_dp[x] = table_dp[y]
    table_dp[x] += 1

print(num_n - max(table_dp))
