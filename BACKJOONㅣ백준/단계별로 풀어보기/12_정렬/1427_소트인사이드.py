import sys


def solution():

    input_x = sys.stdin.readline()

    arr_x = []

    for i in range(len(input_x) - 1):
        arr_x.append(ord(input_x[i]) - 48)

    arr_x.sort(reverse=True)

    for i in arr_x:
        print(i, end='')


solution()
