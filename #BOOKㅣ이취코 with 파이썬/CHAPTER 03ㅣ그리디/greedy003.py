def solution(n, m):

    answer = 0

    for x in range(n):

        data = list(map(int, input().split()))
        min_value = float('inf')

        for y in data:
            min_value = min(y, min_value)

        result = max(answer, min_value)

    return answer


if __name__ == "__main__":

    import sys

    in_n, in_m = map(int, sys.stdin.readline().split())

    print(solution(in_n, in_m))
