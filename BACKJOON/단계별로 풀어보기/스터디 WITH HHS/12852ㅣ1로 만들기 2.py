import sys


in_n = int(sys.stdin.readline())

table_dp = [int(1e9)] * (int(1e6) + 1)
table_dp[0], table_dp[1] = 0, 0
stack_dp = [[1] for _ in range(int(1e6) + 1)]
for n in range(1, in_n + 1):
    op_1, op_2, op_3 = n * 3, n * 2, n + 1

    if op_1 < int(1e6) + 1 and table_dp[op_1] > table_dp[n] + 1:
        table_dp[op_1] = table_dp[n] + 1
        stack_dp[op_1] = stack_dp[n].copy()
        stack_dp[op_1].append(op_1)
    if op_2 < int(1e6) + 1 and table_dp[op_2] > table_dp[n] + 1:
        table_dp[op_2] = table_dp[n] + 1
        stack_dp[op_2] = stack_dp[n].copy()
        stack_dp[op_2].append(op_2)
    if op_3 < int(1e6) + 1 and table_dp[op_3] > table_dp[n] + 1:
        table_dp[op_3] = table_dp[n] + 1
        stack_dp[op_3] = stack_dp[n].copy()
        stack_dp[op_3].append(op_3)

print(table_dp[in_n])
for n in reversed(stack_dp[in_n]):
    print(n, end=' ')

