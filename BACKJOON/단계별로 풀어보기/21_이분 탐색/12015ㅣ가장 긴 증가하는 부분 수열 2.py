import sys

input = sys.stdin.readline

in_n = int(input())
seq_a = list(map(int, input().split()))
table_dp = [0]
for n in range(in_n):
    temp_low, temp_high = 0, len(table_dp) - 1
    while temp_low <= temp_high:
        temp_center = (temp_low + temp_high) // 2
        if table_dp[temp_center] < seq_a[n]:
            temp_low = temp_center + 1
        else:
            temp_high = temp_center - 1
    if temp_low >= len(table_dp):
        table_dp.append(seq_a[n])
    else:
        table_dp[temp_low] = seq_a[n]

answer = len(table_dp) - 1
print(answer)
