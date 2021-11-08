import sys


in_tc = int(sys.stdin.readline())
for _ in range(in_tc):
    in_n, in_m, in_k = map(int, sys.stdin.readline().split())

    for _ in range(in_k):
        in_u, in_v, in_c, in_d = map(int, sys.stdin.readline().split())
