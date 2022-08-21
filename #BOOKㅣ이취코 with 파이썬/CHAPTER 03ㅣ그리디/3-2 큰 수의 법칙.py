def solution(n, m, k):

    answer = 0

    in_num.sort()

    max_1 = in_num[-1]
    max_2 = in_num[-2]

    while True:

        for _ in range(k):
            if m == 0:
                break

            answer += max_1
            m -= 1

        if m == 0:
            break

        answer += max_2
        m -= 1

    return answer


if __name__ == "__main__":

    import sys

    in_n, in_m, in_k = map(int, sys.stdin.readline().split())
    in_num = list(map(int, sys.stdin.readline().split()))

    in_num.sort()

    print(solution(in_n, in_m, in_k))
