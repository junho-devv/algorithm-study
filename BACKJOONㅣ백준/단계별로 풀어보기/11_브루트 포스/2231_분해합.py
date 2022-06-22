def solution(n):

    answer = 0

    for i in range(1, n):

        int_n = i
        sum_n = i

        while True:

            if i // 10 == 0:
                sum_n += i % 10
                break

            sum_n += i % 10

            i = i // 10

        if sum_n == n:
            answer = int_n
            break

    print(answer)


if __name__ == "__main__":

    import sys

    in_n = int(sys.stdin.readline())

    print(solution(in_n))
