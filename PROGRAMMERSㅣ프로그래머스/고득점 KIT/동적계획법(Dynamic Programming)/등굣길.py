def solution(m, n, puddles):

    dp_distance = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for y in range(1, n + 1):
        for x in range(1, m + 1):
            if x == 1 and y == 1:
                dp_distance[1][1] = 1

            if [x, y] in puddles:
                dp_distance[y][x] = 0
            else:
                dp_distance[y][x] = (dp_distance[y - 1][x] + dp_distance[y][x - 1]) % 1000000007

    answer = dp_distance[n][m]
    print(answer)
    return answer


if __name__ == '__main__':
    in_m = 3
    in_n = 2
    in_puddles = [[2, 2]]

    solution(in_m, in_n, in_puddles)
