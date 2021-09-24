import sys


input = sys.stdin.readline

num_n = int(input())
in_n = list(input().rstrip())

sum_n = 0
for n in in_n:
    sum_n += int(n)

print(sum_n)
