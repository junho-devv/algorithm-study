def w(para_a, para_b, para_c):

    if para_a <= 0 or para_b <= 0 or para_c <= 0:
        return 1

    elif para_a > 20 or para_b > 20 or para_c > 20:
        return w(20, 20, 20)

    elif table_dp[para_a][para_b][para_c]:
        return table_dp[para_a][para_b][para_c]

    elif para_a < para_b < para_c:
        table_dp[para_a][para_b][para_c] = \
            w(para_a, para_b, para_c - 1) + w(para_a, para_b - 1, para_c - 1) - w(para_a, para_b - 1, para_c)
        return table_dp[para_a][para_b][para_c]

    else:
        table_dp[para_a][para_b][para_c] = \
            w(para_a - 1, para_b, para_c) + w(para_a - 1, para_b - 1, para_c) + w(para_a - 1, para_b, para_c - 1) \
            - w(para_a - 1, para_b - 1, para_c - 1)
        return table_dp[para_a][para_b][para_c]


table_dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]

while True:

    input_a, input_b, input_c = map(int, input().split())

    if input_a == input_b == input_c == -1:
        break

    print(f"w({input_a}, {input_b}, {input_c}) = {w(input_a, input_b, input_c)}")
