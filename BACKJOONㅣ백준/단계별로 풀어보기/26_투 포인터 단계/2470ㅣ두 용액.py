import sys


def solution(para_seq, para_n):
    answer = [0, 0]
    para_seq.sort()

    solution_a, solution_b = 0, para_n - 1
    min_ab = int(1e9) * 2
    while solution_a < solution_b:
        temp_ab = para_seq[solution_a] + para_seq[solution_b]
        if abs(temp_ab) <= abs(min_ab):
            min_ab = temp_ab
            answer[0] = para_seq[solution_a]
            answer[1] = para_seq[solution_b]
            if min_ab == 0:
                break
        if temp_ab < 0:
            solution_a += 1
        else:
            solution_b -= 1

    return answer


if __name__ == '__main__':
    in_n = int(sys.stdin.readline())
    seq_n = list(map(int, sys.stdin.readline().split()))

    print(*solution(seq_n, in_n))
