import sys


if __name__ == '__main__':
    in_n, in_s = map(int, sys.stdin.readline().split())
    seq_n = list(map(int, sys.stdin.readline().split()))

    sum_n = [0 for _ in range(in_n + 1)]
    for i in range(1, in_n + 1):
        sum_n[i] = sum_n[i - 1] + seq_n[i - 1]

    start_n = 0
    end_n = 1
    min_len = int(1e6) + 1

    while start_n != in_n:
        if sum_n[end_n] - sum_n[start_n] >= in_s:
            if end_n - start_n < min_len:
                min_len = end_n - start_n
            start_n += 1
        else:
            if end_n < in_n:
                end_n += 1
            else:
                start_n += 1

    if min_len != int(1e6) + 1:
        print(min_len)
    else:
        print(0)
