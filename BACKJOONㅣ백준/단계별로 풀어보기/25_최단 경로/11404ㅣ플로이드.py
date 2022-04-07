import sys


INF = sys.maxsize
# n개의 도시 : in_n (2 <= in_n <= 100), m개의 버스 : in_m(1 <= m <= 10 ** 5)
in_n = int(sys.stdin.readline())
in_m = int(sys.stdin.readline())
graph_n = [[INF for _ in range(in_n)] for _ in range(in_n)]
for _ in range(in_m):
    in_a, in_b, in_c = map(int, sys.stdin.readline().split())
    if graph_n[in_a - 1][in_b - 1] > in_c:
        graph_n[in_a - 1][in_b - 1] = in_c


def floyd_warshall():
    for stopover in range(in_n):
        for start in range(in_n):
            for end in range(in_n):
                if start != end and graph_n[start][end] > graph_n[start][stopover] + graph_n[stopover][end]:
                    graph_n[start][end] = graph_n[start][stopover] + graph_n[stopover][end]


floyd_warshall()

for row in graph_n:
    for i in row:
        print(0 if i == INF else i, end=' ')
    print()
