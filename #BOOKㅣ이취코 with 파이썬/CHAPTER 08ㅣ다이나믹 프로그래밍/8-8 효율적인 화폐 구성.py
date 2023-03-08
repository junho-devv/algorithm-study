import sys


MAX = int(1e4) + 1

in_n, in_m = map(int, sys.stdin.readline().split())

mv = list()
for n in range(in_n):
    mv.append(int(sys.stdin.readline()))


dpt = [0] + [MAX] * in_m

for v in mv:
    for m in range(v, in_m + 1):
        if dpt[m - v] != MAX:
            dpt[m] = min(dpt[m - v] + 1, dpt[m])

if dpt[in_m] == MAX:
    print(-1)
else:
    print(dpt[in_m])
