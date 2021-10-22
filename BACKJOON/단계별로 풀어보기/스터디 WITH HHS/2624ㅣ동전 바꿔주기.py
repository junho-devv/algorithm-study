import sys


in_t = int(sys.stdin.readline())
in_k = int(sys.stdin.readline())
list_k = [list(map(int, sys.stdin.readline().split())) for _ in range(in_k)]

table_dp = [0 for _ in range(in_t + 1)]

for k in range(in_k):

    for num in range(1, list_k[k][1] + 1):
        if num - list_k[k][0] >= 0:
            table_dp[num] += table_dp[num - list_k[k][0]]