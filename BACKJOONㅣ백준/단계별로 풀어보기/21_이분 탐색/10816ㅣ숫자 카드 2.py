import sys

input = sys.stdin.readline

in_n = int(input())
list_n = list(map(int, input().split()))
in_m = int(input())
list_m = list(map(int, input().split()))


def binary_search(para_left, para_right, para_val):
    if para_left > para_right:
        return 0

    center = (para_left + para_right) // 2
    if list_n[center] == para_val:
        return dict_n[para_val]

    else:
        if list_n[center] > para_val:
            return binary_search(para_left, center - 1, para_val)
        else:
            return binary_search(center + 1, para_right, para_val)


list_n.sort()
dict_n = dict()
for n in list_n:
    try:
        dict_n[n] += 1
    except:
        dict_n[n] = 1

for m in list_m:
    print(binary_search(0, in_n - 1, m), end=' ')

# for m in list_m:
#     try:
#         print(dict_n[m], end=' ')
#     except:
#         print(0, end=' ')