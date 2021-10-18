import sys


in_s, in_k = map(int, sys.stdin.readline().split())

temp_div = in_s // in_k
temp_mod = in_s % in_k

cnt_k = 0
max_mul = 1
for _ in range(in_k):
    if cnt_k < temp_mod:
        max_mul *= (temp_div + 1)
        cnt_k += 1
    else:
        max_mul *= temp_div

print(max_mul)
