def solution(n, k):
    count = 0

    while True:
        if n == 1:
            break

        if n % k == 0:
            n /= k
            count += 1

        else:
            n -= 1
            count += 1

    return count


if __name__ == "__main__":

    import sys

    in_n, in_k = map(int, sys.stdin.readline().split())

    print(solution(in_n, in_k))
