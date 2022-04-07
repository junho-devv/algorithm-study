import sys


def solution():
    n = int(sys.stdin.readline())

    arr_x = []
    # 각 자릿수를 배열(arr_x)에 원소로 삽입하기
    while n // 10 != 0:
        arr_x.append(n % 10)
        n = n // 10
    arr_x.append(n)
    # 배열(arr_x)의 원소를 내림차순으로 정렬하기
    arr_x.sort(reverse=True)

    answer = 0
    # 배열의 각 원소를 각 자리수에 더하기
    for i in range(len(arr_x)):
        answer += arr_x[i] * (10 ** i)
    # 결과(answer) 출력하기
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
