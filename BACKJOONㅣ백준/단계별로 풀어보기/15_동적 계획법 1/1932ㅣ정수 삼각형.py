import sys

size_n = int(sys.stdin.readline())
triangle_n = [list(map(int, sys.stdin.readline().split())) for _ in range(size_n)]

for i in range(1, size_n):
    for j in range(len(triangle_n[i])):
        if j == 0:
            triangle_n[i][j] += triangle_n[i - 1][j]
        elif j == len(triangle_n[i]) - 1:
            triangle_n[i][j] += triangle_n[i - 1][j - 1]
        else:
            triangle_n[i][j] += max(triangle_n[i - 1][j], triangle_n[i - 1][j - 1])

print(max(triangle_n[size_n - 1]))
