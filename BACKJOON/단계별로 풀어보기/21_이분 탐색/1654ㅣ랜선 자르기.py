import sys

input = sys.stdin.readline

in_k, in_n = map(int, input().split())
list_k = []
for _ in range(in_k):
    list_k.append(int(input()))


def find(para_left, para_right, para_val):

    center = (para_left + para_right) // 2
    temp_sum = 0
    for k in list_k:
        temp_sum += k // center

    if temp_sum == para_val:
        return center
    else:
        if temp_sum < in_n:
            return find(para_left, center - 1, para_val)
        else:
            return find(center + 1, para_right, para_val)


end = find(0, min(list_k), in_n - 1)
start = find(0, min(list_k), in_n)

answer = 0
for i in range(start, end):
    temp_sum = 0
    for k in list_k:
        temp_sum += k // i

    if temp_sum == in_n - 1:
        answer = i - 1
        print(answer)
        break
