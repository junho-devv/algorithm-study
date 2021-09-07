in_n = int(input())
in_p = list(map(int, input().split()))

in_p.sort()

min_time = 0
for x in range(in_n):
    for y in range(x):
        min_time += in_p[y]
    min_time += in_p[x]

print(min_time)