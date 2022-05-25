def solution(str_a, str_b):

    table_dp = [[0] * (int(1e3) + 1) for _ in range(int(1e3) + 1)]

    for a in range(len(str_a)):
        for b in range(len(str_b)):

            if str_a[a] == str_b[b]:
                table_dp[a + 1][b + 1] = table_dp[a][b] + 1

            else:
                table_dp[a + 1][b + 1] = max(table_dp[a + 1][b], table_dp[a][b + 1])

    answer = table_dp[len(str_a)][len(str_b)]

    return answer


if __name__ == '__main__':

    import sys

    in_a = sys.stdin.readline()
    in_b = sys.stdin.readline()

    print(solution(in_a, in_b))
