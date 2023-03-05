import sys


in_n = int(sys.stdin.readline())

dpt = [0] * 1001

dpt[1], dpt[2] = 1, 3

for n in range(3, in_n + 1):
    dpt[n] = (dpt[n - 1] + 2 * dpt[n - 2]) % 796796

print(dpt[in_n])
