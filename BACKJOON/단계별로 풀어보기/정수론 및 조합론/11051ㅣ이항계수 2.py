in_n, in_k = map(int, input().split())

cache = [[0 for _ in range(in_k + 1)] for _ in range(in_n + 1)]

for i in range(in_n + 1):
    cache[i][0] = 1
for i in range(in_k + 1):
    cache[i][i] = 1

for i in range(1, in_n + 1):
    for j in range(1, in_k + 1):
        cache[i][j] = cache[i - 1][j] + cache[i - 1][j - 1]

print(cache[in_n][in_k] % 10007)
