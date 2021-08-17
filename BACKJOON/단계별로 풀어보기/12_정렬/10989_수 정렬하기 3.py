import sys

input_n = int(sys.stdin.readline())
arr_n = [0] * 10001

for i in range(input_n):

    input_m = int(sys.stdin.readline())

    arr_n[input_m] += 1

for i in range(10001):

    if arr_n[i] != 0:

        for j in range(arr_n[i]):
            print(i)
