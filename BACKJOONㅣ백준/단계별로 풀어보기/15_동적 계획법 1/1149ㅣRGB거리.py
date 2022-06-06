

if __name__ == "__main__":

    import sys

    input_n = int(sys.stdin.readline())

    table_dp = [[0, 0, 0] for _ in range(int(1e3) + 1)]

    for i in range(1, input_n + 1):
        red, green, blue = map(int, input().split())

        table_dp[i][0] = min(table_dp[i - 1][1] + red, table_dp[i - 1][2] + red)
        table_dp[i][1] = min(table_dp[i - 1][2] + green, table_dp[i - 1][0] + green)
        table_dp[i][2] = min(table_dp[i - 1][0] + blue, table_dp[i - 1][1] + blue)

    print(min(table_dp[input_n]))
