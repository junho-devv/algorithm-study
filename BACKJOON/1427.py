import sys


def solution():
    n = int(sys.stdin.readline())

    arr_x = []

    while n // 10 != 0:
        arr_x.append(n % 10)
        n = n // 10

    arr_x.append(n)
    arr_x.sort()

    answer = 0
    for i in range(len(arr_x)):
        answer += arr_x[i] * (10 ** i)
    print(answer)
    return


solution()
