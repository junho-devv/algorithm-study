import sys


in_n = int(sys.stdin.readline())

table_dp = [0] * (int(1e6) + 1)
table_dp[0] = 1

bin_n = list(bin(in_n))[2:]
for i in range(len(bin_n)):
    i = 2 ** i
    for j in range(i, in_n + 1):
        table_dp[j] = (table_dp[j] + table_dp[j - i]) % int(1e9)


print(table_dp[in_n] % int(1e9))

# table_dp[n] = table_dp[n] + table_dp[n - 2 ** i]
# DP 테이블에 자기자신과 자기자신에서 2 ** i를 뺀 위치의 DP 테이블 값을 합친다
# 오름차순
# 3의 경우에
# 기존 1+1+1과 1에 2추가 한경우를 합하여 2