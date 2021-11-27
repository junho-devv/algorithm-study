import sys


def floyd_warshall():
    for stopover in range(in_n):
        for start in range(in_n):
            for end in range(in_n):
                if start != end and map_bus[start][end] > map_bus[start][stopover] + map_bus[stopover][end]:
                    map_bus[start][end] = map_bus[start][stopover] + map_bus[stopover][end]


if __name__ == '__main__':
    INF = int(1e9)

    in_n = int(sys.stdin.readline())
    in_m = int(sys.stdin.readline())

    map_bus = [[INF for _ in range(in_n)] for _ in range(in_n)]
    map_prev = [[-1 for _ in range(in_n)] for _ in range(in_n)]
    for _ in range(in_m):
        in_a, in_b, in_c = map(int, sys.stdin.readline().split())
        map_bus[in_a - 1][in_b - 1] = in_c

