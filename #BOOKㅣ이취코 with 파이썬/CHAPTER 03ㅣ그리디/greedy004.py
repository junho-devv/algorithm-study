def solution(n, k):

    answer = 0

    while True:
        if n == 1:
            break

        if n % k == 0:
            n /= k
            answer += 1
        else:
            n -= 1
            answer += 1

    return answer


if __name__ == "__main__":

    import sys

    in_n, in_k = map(int, sys.stdin.readline().split())

    print(solution(in_n, in_k))
