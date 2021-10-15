import sys


in_n, in_m = map(int, sys.stdin.readline().split())
list_nm = [list(sys.stdin.readline().rstrip()) for _ in range(in_n)]

in_k = int(sys.stdin.readline())

temp_nm = [[] for _ in range(in_n)]
for m in range(in_m):
    for n in range(in_n):
        if list_nm[n][m] != '1':
            temp_nm[n].append(m)

print(temp_nm)