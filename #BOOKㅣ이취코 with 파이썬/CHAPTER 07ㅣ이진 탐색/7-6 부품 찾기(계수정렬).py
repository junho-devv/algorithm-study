import sys


in_n = int(sys.stdin.readline())

array = [0] * (int(1e6) + 1)

for i in list(map(int, sys.stdin.readline().split())):
    array[i] = 1

in_m = int(sys.stdin.readline())
in_cm = list(map(int, sys.stdin.readline().split()))

for c in in_cm:
    if array[c] == 1:
        print("yes", end=' ')
    else:
        print("no", end=' ')
