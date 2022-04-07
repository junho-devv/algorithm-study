import sys


num_tc = int(sys.stdin.readline())
for _ in range(num_tc):
    in_n = int(sys.stdin.readline())

    table_dp = [0] * (int(1e4) + 1)
    table_dp[0] = 1

    nums = [1, 2, 3]
    for num in nums:
        for i in range(num, in_n + 1):
            table_dp[i] += table_dp[i - num]

    print(table_dp[in_n])
