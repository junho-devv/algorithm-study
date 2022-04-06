import sys


def solution(numbers):
    answer = ''

    list_str = []
    for number in range(0, len(numbers)):
        list_str.append([str(numbers[number])[0], number])

    print(list_str)
    list_str.sort(reverse=True, key=lambda x: x[0])
    print(list_str)

    return answer


if __name__ == '__main__':
    in_x = list(map(int, sys.stdin.readline().split()))

    solution(in_x)
