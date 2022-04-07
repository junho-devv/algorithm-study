import sys


if __name__ == '__main__':
    in_n = int(sys.stdin.readline())
    seq_a = list(map(int, sys.stdin.readline().split()))

    table_dp = [0 for _ in range(in_n)]
    dp_seq = [[a] for a in seq_a]
    for ref in range(in_n):
        for i in range(ref):
            if seq_a[ref] > seq_a[i] and table_dp[ref] < table_dp[i]:
                dp_seq[ref] = dp_seq[i] + [seq_a[ref]]
                table_dp[ref] = table_dp[i]
        table_dp[ref] += 1

    answer_len, answer_idx = 0, 0
    for n in range(in_n):
        if answer_len < table_dp[n]:
            answer_len = table_dp[n]
            answer_idx = n

    print(answer_len)
    print(*dp_seq[answer_idx])
