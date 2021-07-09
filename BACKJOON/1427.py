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


def solution2():
    # sys.stdin.readline() 입력 방식은 문자열 x(str_x)에 정수방식으로 삽입하는 과정이 되지 않았음
    n = input()
    str_x = [int(i) for i in n]
    str_x.sort(reverse=True)

    for i in str_x:
        print(i, end="")


solution()
