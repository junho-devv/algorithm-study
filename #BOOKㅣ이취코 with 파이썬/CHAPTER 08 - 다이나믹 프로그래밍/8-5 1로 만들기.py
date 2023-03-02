import sys

in_x = int(sys.stdin.readline())

dpt = [0] * 30001

for x in range(2, in_x + 1):

    dpt[x] = dpt[x - 1] + 1

    if x % 5 == 0:
        dpt[x] = min(dpt[x], dpt[x // 5] + 1)

    if x % 3 == 0:
        dpt[x] = min(dpt[x], dpt[x // 3] + 1)

    if x % 2 == 0:
        dpt[x] = min(dpt[x], dpt[x // 2] + 1)

print(dpt[in_x])
