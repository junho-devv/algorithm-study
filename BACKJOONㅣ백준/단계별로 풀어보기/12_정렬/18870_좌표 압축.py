import sys


def solution():

    num_x = int(sys.stdin.readline())

    list_x = list(map(int, sys.stdin.readline().split()))

    list_y = sorted(list(set(list_x)))

    dict_x = {list_y[i]: i for i in range(len(list_y))}

    for x in list_x:
        print(dict_x[x], end=' ')


solution()
