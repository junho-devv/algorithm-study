def solution(N, triangle):
    for i in range(1, N):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i - 1][j]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i - 1][j - 1]
            else:
                triangle[i][j] += max(triangle[i - 1][j], triangle[i - 1][j - 1])

    answer = max(triangle[N - 1])
    return answer


if __name__ == "__main__":

    import sys

    in_n = int(sys.stdin.readline())
    in_t = [list(map(int, sys.stdin.readline().split())) for _ in range(in_n)]

    print(solution(in_n, in_t))
