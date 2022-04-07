import sys


in_n, in_m = map(int, sys.stdin.readline().split())
list_nm = [tuple(sys.stdin.readline().rstrip()) for _ in range(in_n)]
in_k = int(sys.stdin.readline())

set_nm = list(set(list_nm))
max_row = 0
for nm in set_nm:
    if nm.count('0') <= in_k and nm.count('0') % 2 == in_k % 2:
        max_row = max(max_row, list_nm.count(nm))

print(max_row)

