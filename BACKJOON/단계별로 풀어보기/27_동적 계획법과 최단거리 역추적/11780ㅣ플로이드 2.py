import sys


def floyd_warshall():
    for stopover in range(in_n):
        for start in range(in_n):
            for end in range(in_n):
                if start != end and map_bus[start][end] > map_bus[start][stopover] + map_bus[stopover][end]:
                    map_bus[start][end] = map_bus[start][stopover] + map_bus[stopover][end]
                    map_stopover[start][end] = stopover


def track(para_row, para_col):
    answer = []

    temp_stopover = map_stopover[para_row][para_col]
    if temp_stopover == -1:
        return answer
    else:
        answer = track(para_row, temp_stopover) + [temp_stopover + 1] + track(temp_stopover, para_col)
        return answer


if __name__ == '__main__':
    INF = int(1e9)

    in_n = int(sys.stdin.readline())
    in_m = int(sys.stdin.readline())

    map_bus = [[INF for _ in range(in_n)] for _ in range(in_n)]
    map_stopover = [[-1 for _ in range(in_n)] for _ in range(in_n)]
    for _ in range(in_m):
        in_a, in_b, in_c = map(int, sys.stdin.readline().split())
        if map_bus[in_a - 1][in_b - 1] > in_c:
            map_bus[in_a - 1][in_b - 1] = in_c

    floyd_warshall()

    for row in map_bus:
        for i in row:
            print(0 if i == INF else i, end=' ')
        print()

    for row in range(in_n):
        for col in range(in_n):
            out_2 = [row + 1] + track(row, col) + [col + 1]
            out_1 = len(out_2)
            if map_bus[row][col] == INF:
                print(0)
            else:
                print(out_1, *out_2)
