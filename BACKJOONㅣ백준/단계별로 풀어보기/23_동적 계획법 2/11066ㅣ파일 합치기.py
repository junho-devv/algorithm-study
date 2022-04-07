import sys


num_tc = int(sys.stdin.readline())
for _ in range(num_tc):
    in_k = int(input())
    list_k = list(map(int, input().split()))

    # accumulated_sum[k] = 1부터 k까지 합
    accumulated_sum = [0 for _ in range(in_k + 1)]
    for k in range(1, in_k + 1):
        accumulated_sum[k] = accumulated_sum[k - 1] + list_k[k - 1]

    # table_dp[a][b] = a부터 b까지 합의 최솟값
    table_dp = [[0 for _ in range(in_k + 1)] for _ in range(in_k + 1)]
    for n in range(2, in_k + 1):
        for i in range(1, in_k - n + 2):
            temp_min = int(1e9)
            for j in range(n - 1):
                temp_min = min(temp_min, table_dp[i][i + j] + table_dp[i + j + 1][i + n - 1])
            table_dp[i][i + n - 1] = temp_min + (accumulated_sum[i + n - 1] - accumulated_sum[i - 1])

    print(table_dp[1][in_k])
