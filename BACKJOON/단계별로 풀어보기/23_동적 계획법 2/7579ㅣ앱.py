import sys


in_n, in_m = map(int, sys.stdin.readline().split())
list_memory = [0] + list(map(int, sys.stdin.readline().split()))
list_cost = [0] + list(map(int, sys.stdin.readline().split()))

table_dp = [[0 for _ in range((sum(list_cost) + 1))] for _ in range(len(list_cost))]

min_cost = sum(list_cost)
for i in range(len(list_cost)):
    for cost in range(1, sum(list_cost) + 1):
        if list_cost[i] > cost:
            table_dp[i][cost] = table_dp[i - 1][cost]
        else:
            table_dp[i][cost] = max(table_dp[i - 1][cost - list_cost[i]] + list_memory[i], table_dp[i - 1][cost])

        if table_dp[i][cost] >= in_m:
            min_cost = min(min_cost, cost)

print(min_cost)
