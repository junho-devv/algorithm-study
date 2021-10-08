import sys
from collections import deque

input = sys.stdin.readline

in_n, in_s, in_m = map(int, input().split())
list_v = list(map(int, input().split()))

que_v = deque([in_s])
for n in range(in_n):
    temp_list = []
    while que_v:
        temp_pop = que_v.popleft()
        if temp_pop - list_v[n] >= 0:
            temp_list.append(temp_pop - list_v[n])
        if temp_pop + list_v[n] <= in_m:
            temp_list.append(temp_pop + list_v[n])
    que_v.extend(temp_list)
    print(que_v)

print(max(que_v))
