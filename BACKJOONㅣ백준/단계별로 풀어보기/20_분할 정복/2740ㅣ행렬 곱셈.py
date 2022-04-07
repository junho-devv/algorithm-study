import sys


input = sys.stdin.readline

row_a, col_a = map(int, input().split())
matrix_a = []
for _ in range(row_a):
    matrix_a.append(list(map(int, input().split())))

row_b, col_b = map(int, input().split())
matrix_b = []
for _ in range(row_b):
    matrix_b.append(list(map(int, input().split())))

matrix_ab = [[0 for _ in range(col_b)] for _ in range(row_a)]
for a in range(row_a):
    for b in range(col_b):
        for k in range(col_a):
            matrix_ab[a][b] += matrix_a[a][k] * matrix_b[k][b]

for ab in matrix_ab:
    print(*ab)
