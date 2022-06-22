def solution(n):

    int_n = 666

    count_n = 0

    while count_n != n:

        if '666' in str(int_n):
            count_n += 1

        int_n += 1

    answer = int_n - 1
    return answer


if __name__ == "__main__":

    import sys

    in_n = int(sys.stdin.readline())

    solution(in_n)
