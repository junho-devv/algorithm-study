import sys


def solution(numbers):
    answer = ''

    list_str = []
    for number in numbers:
        list_str.append(str(number)[0])

    print(list_str)

    return answer


if __name__ == '__main__':
    in_x = map(int, sys.stdin.readline().split())

    solution(in_x)
