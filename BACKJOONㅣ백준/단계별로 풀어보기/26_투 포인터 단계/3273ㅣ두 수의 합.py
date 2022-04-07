import sys


in_n = int(sys.stdin.readline())
seq_n = list(map(int, sys.stdin.readline().split()))
in_x = int(sys.stdin.readline())


def find(para_seq):
    answer = 0
    para_seq.sort()
    temp_start, temp_end = 0, in_n - 1
    while temp_start < temp_end:
        temp_x = para_seq[temp_start] + para_seq[temp_end]
        if temp_x == in_x:
            answer += 1

        if temp_x < in_x:
            temp_start += 1
            continue

        temp_end -= 1

    return answer


print(find(seq_n))
