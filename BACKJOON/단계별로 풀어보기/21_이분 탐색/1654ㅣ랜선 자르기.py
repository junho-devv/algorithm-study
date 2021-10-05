import sys

input = sys.stdin.readline

in_k, in_n = map(int, input().split())
list_k = []
for _ in range(in_k):
    list_k.append(int(input()))
sum_k = sum(list_k)

while True:
    answer = sum_k // in_n
    for k in range(in_k):

