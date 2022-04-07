import sys

# 팰린드롬(palindrome)이란 앞에서부터 읽으나 뒤에서부터 읽으나 같은 단어를 말한다.
in_n = int(sys.stdin.readline())
list_n = list(map(int, sys.stdin.readline().split()))

table_dp = [[0 for _ in range(in_n)] for _ in range(in_n)]
# 길이가 1일 때,
for n in range(in_n):
    table_dp[n][n] = 1
# 길이가 2일 때,
for n in range(in_n - 1):
    if list_n[n] == list_n[n + 1]:
        table_dp[n][n + 1] = 1
# 길이가 3이상일 때
for l in range(2, in_n):
    for n in range(in_n - l):
        if list_n[n] == list_n[n + l] and table_dp[n + 1][n + l - 1] == 1:
            table_dp[n][n + l] = 1

in_m = int(sys.stdin.readline())
for _ in range(in_m):
    m_s, m_e = map(int, sys.stdin.readline().split())
    print(table_dp[m_s - 1][m_e - 1])
