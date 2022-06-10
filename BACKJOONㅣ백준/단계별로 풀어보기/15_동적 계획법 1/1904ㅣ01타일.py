def solution():

    dynamic_table = [0] * (int(1e6) + 1)
    table_dp = [0] * (int(1e6) + 1)

    table_dp[1], table_dp[2] = 1, 2

    for i in range(3, input_n + 1):
        table_dp[i] = (table_dp[i - 1] + table_dp[i - 2]) % 15746

    print(table_dp[input_n])


    answer = 0
    return answer

if __name__ == "__main__":

    import sys

    in_n = int(sys.stdin.readline())

    print(solution(in_n))
