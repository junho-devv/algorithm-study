import sys
from bisect import bisect_left


if __name__ == '__main__':
    in_n = int(sys.stdin.readline())
    seq_a = list(map(int, sys.stdin.readline().split()))

    seq_lis = [-int(1e9) - 1]
    lis_len = [0 for _ in range(in_n)]
    for n in range(in_n):
        temp_left, temp_right = 0, len(seq_lis) - 1
        while temp_left <= temp_right:
            temp_middle = (temp_left + temp_right) // 2

            if seq_lis[temp_middle] < seq_a[n]:
                temp_left = temp_middle + 1
            else:
                temp_right = temp_middle - 1

        if seq_lis[-1] < seq_a[n]:
            seq_lis.append(seq_a[n])
            lis_len[n] = len(seq_lis) - 1
        else:
            seq_lis[temp_left] = seq_a[n]
            lis_len[n] = temp_left

    max_lis = max(lis_len)
    answer = []
    for n in reversed(range(in_n)):
        if lis_len[n] == max_lis:
            answer.append(seq_a[n])
            max_lis -= 1
    answer.reverse()
    print(len(answer))
    print(*answer)
