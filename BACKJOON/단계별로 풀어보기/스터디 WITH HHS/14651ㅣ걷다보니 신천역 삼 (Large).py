import sys


in_n = int(sys.stdin.readline())

dp = [[0 for _ in range(3)] for _ in range(33333 + 1)]
dp[0][0] = dp[1][0] = dp[1][1] = dp[1][2] = 1

given_mod = int(1e9) + 9

for n in range(2, in_n + 1):
    for num in [0, 1, 2]:
        dp[n][num] = (dp[n - 1][0] + dp[n - 1][1] + dp[n - 1][2]) % given_mod

answer = (dp[in_n][0] - dp[in_n - 1][0]) % given_mod
print(answer)
