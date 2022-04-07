import sys


INF = int(1e9)

if __name__ == '__main__':
    in_v, in_e = map(int, sys.stdin.readline().split())

    matrix_v = [[INF for _ in range(in_v)] for _ in range(in_v)]
    for _ in range(in_e):
        in_a, in_b, in_c = map(int, sys.stdin.readline().split())
        matrix_v[in_a - 1][in_b - 1] = in_c

    for stopover in range(in_v):
        for start in range(in_v):
            for end in range(in_v):
                matrix_v[start][end] = min(matrix_v[start][end], matrix_v[start][stopover] + matrix_v[stopover][end])

    answer = INF
    for v in range(in_v):
        answer = min(answer, matrix_v[v][v])

    if answer == INF:
        print(-1)
    else:
        print(answer)
